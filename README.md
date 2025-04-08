
# 🎬 Final Movie Catalog Project

Этот Django-проект представляет собой дипломную платформу для работы с каталогом фильмов: с отзывами, оценками, фильтрацией и изображениями. Разработано студентом **Димой**.

## 🚀 Функциональность

- 📚 Каталог фильмов с фильтрацией по жанру и дате
- ⭐ Рейтинги от пользователей (1–10)
- 📝 Рецензии на фильмы
- 🖼️ Поддержка изображений (постеров)
- 🔐 JWT-аутентификация
- 🧪 Полное тестирование всех функций
- 🐳 Поддержка Docker и PostgreSQL
- 📑 Документация API через Swagger и ReDoc

## ⚙️ Установка

1. Клонируй репозиторий:

```bash
git clone https://github.com/your-username/Final_project.git
cd Final_project
```

2. Запусти через Docker:

```bash
docker-compose up --build
```

3. Примени миграции:

```bash
docker-compose exec web python manage.py migrate
```

4. Создай суперпользователя:

```bash
docker-compose exec web python manage.py createsuperuser
```

5. Загрузить тестовые данные:

```bash
docker-compose exec web python manage.py loaddata Final_posters_image_field.json
```

## 🧪 Запуск тестов

```bash
docker-compose exec web pytest
```

Все тесты покрывают:
- модели
- views
- фильтрацию
- формы
- отзывы и оценки
- авторизацию и выход из системы

## 🌐 Документация API

- Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## 📂 Структура проекта

```
Final_project/
├── config/                 # Настройки Django
├── movies/                 # Основное приложение
│   ├── models.py           # Модели
│   ├── views.py            # Представления
│   ├── templates/          # HTML-шаблоны
│   ├── tests/              # Все тесты
│   └── fixtures/           # Фикстуры с постерами
├── media/                  # Изображения фильмов
├── static/                 # Статические файлы (по необходимости)
├── docker-compose.yml
├── requirements.txt
└── README.md
```

