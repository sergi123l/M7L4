import pytest
import sqlite3
import os
from registration.registration import create_db, add_user, authenticate_user, display_users

@pytest.fixture(scope="module")
def setup_database():
    """Фикстура для настройки базы данных перед тестами и её очистки после."""
    # Функция create_db() создает базу данных users.db и инициализирует схему
    create_db()
    yield
    # Очистка после выполнения тестов
    os.remove('users.db')

def test_create_db(setup_database):
    """Тест создания базы данных и таблицы пользователей."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Проверяем, существует ли таблица users
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    table_exists = cursor.fetchone()
    conn.close()
    assert table_exists, "Таблица 'users' должна существовать в базе данных."

def test_add_new_user(setup_database):
    """Тест добавления нового пользователя."""
    add_user('testuser', 'testuser@example.com', 'password123')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username='testuser';")
    user = cursor.fetchone()
    conn.close()
    assert user, "Пользователь должен быть добавлен в базу данных."

# Возможные варианты тестов:
def test_authenticat_user(steup_database):
    """Тест аутентификации пользователя с неправильным паролем."""

    assert authenticate_user("testuser","333") == False

    

