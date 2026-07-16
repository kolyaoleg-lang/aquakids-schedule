"""
Читает raspisanie.csv из этого репозитория и публикует пост с расписанием
на стене группы VK через VK API (метод wall.post).

Нужны переменные окружения (задаются как GitHub Secrets в репозитории):
  VK_TOKEN    - токен доступа сообщества VK (Управление сообществом -> Работа с API -> Ключи доступа)
  VK_GROUP_ID - числовой id группы (без минуса), например 123456789

Запускается автоматически через .github/workflows/update-vk.yml
"""
import csv
import os
import sys
import requests

VK_TOKEN = os.environ.get("VK_TOKEN")
VK_GROUP_ID = os.environ.get("VK_GROUP_ID")
CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "raspisanie.csv")
VK_API_VERSION = "5.199"


def load_schedule(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def format_message(rows):
    lines = ["Расписание AquaKids:", ""]
    for row in rows:
        lines.append(
            "{day}, {time} - {group} ({trainer}, {hall})".format(
                day=row["День"],
                time=row["Время"],
                group=row["Группа"],
                trainer=row["Тренер"],
                hall=row["Зал"],
            )
        )
    return "\n".join(lines)


def post_to_wall(message):
    resp = requests.post(
        "https://api.vk.com/method/wall.post",
        data={
            "owner_id": "-" + VK_GROUP_ID,
            "from_group": 1,
            "message": message,
            "access_token": VK_TOKEN,
            "v": VK_API_VERSION,
        },
        timeout=15,
    )
    data = resp.json()
    if "error" in data:
        print("VK API error:", data["error"], file=sys.stderr)
        sys.exit(1)
    print("Опубликовано, post_id =", data["response"]["post_id"])


if __name__ == "__main__":
    if not VK_TOKEN or not VK_GROUP_ID:
        print("Не заданы VK_TOKEN / VK_GROUP_ID", file=sys.stderr)
        sys.exit(1)
    rows = load_schedule(CSV_PATH)
    message = format_message(rows)
    post_to_wall(message)
