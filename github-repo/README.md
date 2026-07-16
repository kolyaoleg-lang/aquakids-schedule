# aquakids-schedule (тестовый образец)

Одна таблица `raspisanie.csv` — источник данных и для сайта, и для VK.

## Разовая настройка (делаете сами, 5-10 минут)

1. **Создать репозиторий на GitHub**
   - github.com → New repository → назвать, например, `aquakids-schedule` → Public → Create.
2. **Загрузить в него все файлы из этой папки** (`raspisanie.csv`, `.github/`, `scripts/`, `README.md`) — через "Add file → Upload files" в браузере, перетаскиванием.
3. **Получить raw-ссылку на CSV**
   - Открыть `raspisanie.csv` в репозитории → кнопка "Raw" → скопировать URL из адресной строки.
   - Вставить этот URL в `tilda-snippet.html`, заменив `CSV_URL`.
4. **Вставить `tilda-snippet.html` в Тильду**
   - На странице aquakids.ru рядом с якорем `#raspisanie` добавить блок T123 (HTML-код) и вставить содержимое файла.
5. **Настроить VK (для автопостинга)**
   - В своём сообществе VK: Управление → Работа с API → Ключи доступа → создать ключ с правами `wall`.
   - Скопировать id группы (число в ссылке типа vk.com/club**123456789**).
   - В репозитории на GitHub: Settings → Secrets and variables → Actions → New repository secret:
     - `VK_TOKEN` = токен сообщества
     - `VK_GROUP_ID` = id группы (без минуса)

## Как это работает дальше

- Меняете строки в `raspisanie.csv` в репозитории (прямо на GitHub, через "Edit") → коммитите.
- Сайт (Тильда) на следующей загрузке страницы сразу подтянет новые данные — ничего дополнительно делать не нужно.
- GitHub Actions (`.github/workflows/update-vk.yml`) сам запустится при коммите в `raspisanie.csv` (и ещё раз в сутки по расписанию) и опубликует новый пост в VK с актуальным расписанием.
- Проверить вручную: вкладка "Actions" репозитория → workflow "Update VK wall from schedule" → "Run workflow".
