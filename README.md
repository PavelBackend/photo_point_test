# Photo Point Test

## Описание

Проект предоставляет API для отправки уведомлений через Telegram и Email. Реализован с использованием Django, DRF, Celery и RabbitMQ.

Swagger UI доступен для удобного тестирования API.

---

---

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/PavelBackend/photo_point_test.git
```

2. Запустите проект через Docker Compose с указанием .env файла:
```bash
docker compose -f photo_point_test/deploy/docker-compose.yml --env-file .env up --build -d
```

3. Примените миграции:
```bash
docker compose -f deploy/docker-compose.yml --env-file .env run --rm web python manage.py migrate
```

Документация Swagger будет по адресу:
```bash
http://localhost:8000/api/docs/
```