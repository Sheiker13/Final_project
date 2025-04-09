# 🎬 Final Project — Онлайн-КиноПлатформа

Платформа для оценки и обзора фильмов, вдохновлённая КиноПоиском. Поддерживает регистрацию, JWT-аутентификацию, рецензии, избранное, REST API, деплой через Docker и автоматическое тестирование.

---

## 🚀 Возможности

- 📚 Каталог фильмов с фильтрацией по жанрам и годам
- ⭐ Рейтинг фильмов от пользователей
- 💬 Комментарии и рецензии
- ❤️ Избранные фильмы и личные подборки
- 👤 Авторизация / регистрация пользователей (через HTML)
- 🔐 JWT-аутентификация (через DRF)
- 🌐 REST API на DRF (`/api/` подключен)
- 🐳 Docker + PostgreSQL + Nginx + Prometheus
- 🧪 Тестирование через Pytest
- 🚀 CI/CD на GitHub Actions

---

## ⚙️ Установка и запуск (локально через Docker)

```bash
# Клонируем репозиторий
https://github.com/Sheiker13/Final_project
cd Final_project

# Создаём файл окружения
cp env.example .env

# Собираем и запускаем контейнеры
docker-compose up --build
```

Открой в браузере:
- Django: http://localhost:8000
- Админка: http://localhost:8000/admin/
- Prometheus: http://localhost:9090

---

## 🧪 Запуск тестов

```bash
docker-compose exec web pytest
```

Тестируются:
- Авторизация
- Фильтрация фильмов
- Формы и валидация

---

## 🔑 Авторизация JWT (DRF)

- Получение токена: `POST /api/token/`
- Обновление токена: `POST /api/token/refresh/`

Пример тела запроса:
```json
{
  "username": "youruser",
  "password": "yourpass"
}
```

---

## 📂 Структура проекта (сокращённо)

```
Final_project/
├── movies/             # Приложение с моделями и views
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── api_urls.py  ← ✅ Добавлен API-маршрутизатор
│   └── forms.py
├── templates/          # HTML-шаблоны (Bootstrap)
│   ├── base.html
│   ├── index.html
│   └── catalog.html и др.
├── static/             # CSS/JS и постеры
├── media/              # Загружаемые изображения
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
├── .github/workflows/python.yml
└── README.md
```

---
