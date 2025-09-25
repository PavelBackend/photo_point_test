# Photo Point Test

## Описание

- Гарантированна доставка уведомлений at least once по двум каналам — Email и Telegram. Реализуется через ретраи, acks_late в Celery и durable очереди в RabbitMQ. Даже при падении Celery или RabbitMQ сообщение будет доставлено после перезапуска сервисов
- Реализованна модель pub/sub для обеспечения мастшабируемости
- Асинхронная обработка сообщений, чтобы не блокировать основной поток
- Добавление новых каналов, SMS напрмиер, требует только создание нового адаптера, благодаря чистой архитектуре и паттерну Strategy
- Логирование каждого шага и запись в базу статусов нотификаций

P.S.
- Убрал .env из .gitignore для легкого запуска тестового, в реальный проектах так не делаю, конечно
- SMS не смог добавить, так как не нашел подходящего для тестового задания оператора

Допущения:
- Любая почта считается валидной и на нее будет попытка отправить сообщение (в теории можно добавить регулрку готовую для валидации почты, но решил оставить такое допущение)
- В приоритете - отправка уведомления в тг

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

## Тестирование

Документация Swagger будет по адресу:
```bash
http://localhost:8000/api/docs/
```

После запуска проекта локально перейдите по ссылке ниже и нажмите start, чтобы получить chat_id, он нужен для отправки уведомления в тг
```bash
https://t.me/Photo_point_test_bot
```

4. Остановить проект:
```bash
docker compose -f photo_point_test/deploy/docker-compose.yml --env-file photo_point_test/.env down
```
(-v в последний раз добавьте, чтобы базы данных в следующих тестовых заданиях создавались автоматически заново)
