# Photo Point Test

## Описание

- Гарантированна надежная доставка уведомления по 2 каналам - Email и Telegram. Гарантия осуществляется через повторы отправки сообщений в каналы и гарантии доставки на уровне RabbitMQ.
- Реализованна модель pub/sub для обеспечения мастшабируемости.
- Асинхронная обработка сообщений, чтобы не блокировать основной поток
- Добавление новых каналов, SMS напрмиер, требует только создание нового адаптера, благодаря чистой архитектуре и паттерну Strategy
- Логирование каждого шага и запись в базу статусов нотификаций

P.S.
- Убрал .env из .gitignore для легкого запуска тестового, в реальный проектах так не делаю, конечно
- SMS не смог добавить, так как не нашел подходящего для тестового задания оператора

---

---

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/PavelBackend/photo_point_test.git
```

2. Запустите проект через Docker Compose с указанием .env файла:
```bash
docker compose -f photo_point_test/deploy/docker-compose.yml --env-file photo_point_test/.env up --build -d
```

3. Примените миграции:
```bash
docker compose -f photo_point_test/deploy/docker-compose.yml --env-file photo_point_test/.env run --rm main_service python manage.py migrate
```

Документация Swagger будет по адресу:
```bash
http://localhost:8000/api/docs/
```

4. Остановить проект:
```bash
docker compose -f photo_point_test/deploy/docker-compose.yml --env-file photo_point_test/.env down (-v в последний раз добавить, чтобы базы следующих тестовых создавались автоматически заново)
```
