
# Final Project — Movie Catalog Platform 🎬

## Описание проекта

Веб-приложение для работы с каталогом фильмов: просмотр, отзывы, оценки, избранное.  
Реализовано на Django с использованием PostgreSQL и Docker.

## 🚀 Возможности

- Список фильмов (каталог)
- Детальные страницы фильмов
- Оценки и рецензии
- Админпанель Django
- Bootstrap-стилизация
- Docker-контейнеризация

---

## 🏗 Стек технологий

- Python 3.11
- Django 5.1
- PostgreSQL
- Docker & Docker Compose
- Bootstrap 5
- Django Templates

---

## ⚙️ Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/Sheiker13/Final_project.git
cd Final_project
```

### 2. Настройте `.env` файл

Создайте файл `.env` и добавьте:

```env
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 3. Запуск в Docker

```bash
docker-compose up --build
```

### 4. Примените миграции

```bash
docker-compose exec web python manage.py migrate
```

### 5. Загрузите тестовые данные

```bash
docker-compose exec web python manage.py loaddata movies/fixtures/initial_data.json
```

### 6. Создайте суперпользователя (если нужно)

```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 🧪 Тестовые пользователи

| Роль           | Логин | Пароль |
|----------------|-------|--------|
| Администратор  | test  | test   |

---

## 📂 Структура проекта

- `config/` — настройки проекта
- `movies/` — основное приложение (фильмы, рецензии, рейтинги)
- `templates/` — шаблоны сайта
- `fixtures/` — фикстуры с тестовыми данными

---

## 📌 Авторизация и роли

- Неавторизованный пользователь может просматривать каталог и фильмы
- Авторизованный пользователь — оставлять отзывы и оценки
- Администратор — управляет всем через админку
- (Модератор добавляется на следующем этапе)

---

