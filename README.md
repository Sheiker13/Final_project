# Final_project 🎬

Онлайн-платформа для оценки фильмов, аналогичная КиноПоиску или IMDb.  
Позволяет пользователям регистрироваться, ставить оценки, оставлять рецензии, фильтровать фильмы по жанрам и дате, а также добавлять фильмы в избранное.

## 🚀 Возможности

- Регистрация и аутентификация пользователей
- Оценки фильмов по 10-балльной шкале
- Добавление рецензий
- Сортировка и фильтрация фильмов (жанры, рейтинг, дата выхода)
- Избранное
- Роли пользователей: администратор, авторизованный, гость
- Админ-панель Django для управления контентом

## 🛠 Технологии

- Python, Django, Django Templates
- PostgreSQL
- Bootstrap (адаптивная верстка)
- Docker, Docker Compose
- CI/CD через GitHub Actions
- Мониторинг: Prometheus + Grafana

## 📦 Установка локально

```bash
git clone https://github.com/Sheiker13/Final_project.git
cd Final_project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 🐳 Запуск в Docker

```bash
docker-compose up --build
```

Доступ к сайту: `http://localhost:8000/`

## 🚢 Деплой на Render

- Используется Docker-режим
- В переменных окружения задать:
  - `DEBUG=False`
  - `SECRET_KEY=your_secret`
  - `POSTGRES_*` (из Render PostgreSQL)
  - `ALLOWED_HOSTS=your_render_url`

## ✅ CI/CD

- GitHub Actions
  - Проверка кода и тесты при push/pull
  - Используется PostgreSQL 14 в CI
- Автоматизация деплоя на Render (если нужно)

## 📊 Мониторинг

- Prometheus собирает метрики
- Grafana отображает графики
- Подключены к Docker-контейнерам

## 📈 Перспективы развития

- Рекомендательная система
- Интеграция с внешними API (TMDb, IMDb)
- Уведомления о новых рецензиях
- Расширенные профили пользователей
