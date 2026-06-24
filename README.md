# Kyrgyzstan Atlas — Nomad's Atlas

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&pause=1000&color=58A6FF&center=false&vCenter=true&width=550&lines=Python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA;Telegram+%D0%B1%D0%BE%D1%82%D1%8B;%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F;OSINT+%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B;Backend+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA;API+%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F;Django+%2F+FastAPI)](https://git.io/typing-svg)

Интерактивный путеводитель по Кыргызстану. Сайт знакомит с историей, культурой, кухней, природой и достопримечательностями страны.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) 

## 📌 Возможности

- **Главная** — общая информация о стране, населении, языке и национальных играх.
- **Бишкек** — вводная информация и каталог мест (парки, музеи, базары, рестораны).
- **История** — эпохи, ключевые события и культура (с поддержкой аудио и видео).
- **Кухня** — национальные блюда и традиционные напитки.
- **Природа** — статьи о природе с фото-галереей и подробным описанием.
- **Достопримечательности** — интересные локации по всему Кыргызстану.
- **Гид** — полезные приложения, советы, экстренные контакты.
- **Двуязычность** — бесшовное переключение между русским и английским языками.

---

## 🛠 Стек технологий

* **Языки и фреймворки:** Python 3.10+, Django 6.0
* **Базы данных:** SQLite (разработка) / PostgreSQL (продакшн)
* **Локализация и перевод:** `django-modeltranslation` (база данных), стандартная интернационализация Django (шаблоны)
* **Инфраструктура и деплой:** WhiteNoise (статика), Gunicorn (WSGI-сервер), Heroku
* **Медиа:** Pillow (обработка изображений)

---

## 🚀 Установка и запуск (Локально)

Убедитесь, что у вас установлены `Git` и `Python`.

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/Ainazik111/project.git
   cd project
   ```

2. **Создайте и активируйте виртуальное окружение (рекомендуется):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Примените миграции:**
   ```bash
   python manage.py migrate
   ```

5. **Запустите сервер:**
   ```bash
   python manage.py runserver
   ```

Сайт будет доступен по адресу: `http://127.0.0.1:8000`.

---

## 🔑 Использование

* **Язык по умолчанию (Русский):** `http://127.0.0.1:8000/`
* **Английская версия:** `http://127.0.0.1:8000/en/`
* **Панель администратора:** `http://127.0.0.1:8000/admin/`
  * Логин: `admin`
  * Пароль: `admin`

> *Примечание:* Для смены языка используйте переключатель в правом верхнем углу навигационной панели сайта.

---

## 🏗 Структура проекта

```text
project/
├── core/              # Настройки Django (settings, urls, wsgi)
├── home/              # Главная страница
├── bishkek/           # Бишкек (intro + места)
├── food/              # Кухня (блюда + напитки)
├── guide/             # Гид (приложения, советы, контакты)
├── history/           # История (эпохи, события, культура)
├── nature/            # Природа (статьи)
├── places/            # Достопримечательности
├── templates/         # Базовый шаблон (base.html)
├── static/            # CSS, стили, изображения
├── media/             # Загруженные файлы (фото, аудио)
├── locale/            # Файлы переводов (.po / .mo)
└── requirements.txt
```

---

## 🌐 Локализация и переводы

В проекте реализованы два механизма перевода:

1. **Интерфейс и статические строки (`{% trans %}`):** Переводы хранятся в `locale/en/LC_MESSAGES/django.po`.
2. **Контент базы данных:** Используется `django-modeltranslation` (поля моделей расширяются суффиксами `_ru` и `_en`, переводы заполняются через административную панель).

**Команды для обновления переводов (файлы `.po`):**

```bash
# Сборка сообщений для перевода на английский
python manage.py makemessages -l en

# (После редактирования файла .po)
python manage.py compilemessages
```

---

## ☁️ Деплой и продакшн

Проект оптимизирован для деплоя на платформу **Heroku**.

```bash
heroku create
git push heroku main
heroku run python manage.py migrate
```

**Обязательные переменные окружения (Environment Variables):**

* `SECRET_KEY` — секретный ключ вашего проекта Django
* `DEBUG` — `True` или `False`
* `ALLOWED_HOSTS` — список разрешенных хостов (через запятую)

---

## 👥 Авторы и контрибьюторы

Проект создан совместной командой разработчиков:

* **Хантемир Мирланов** — автор проекта, бэкенд-разработка
* **Айназик Мирланова** — автор проекта, архитектура и фронтенд
* **Ратмир** — интернационализация, настройка `django-modeltranslation`, перевод на английский язык

---

💡 *Если у вас есть идеи по улучшению проекта, смело создавайте Issues или отправляйте Pull Requests!*
