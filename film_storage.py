import os
import string

# Шлях до папки "film_player"
film_player_path = os.path.join(os.getcwd(), "film_player")

# Шлях до папки "film_storage" у пакеті "film_player"
film_storage_path = os.path.join(film_player_path, "film_storage")

# Перевірка, чи існує папка "film_storage", якщо ні - створення папки
if not os.path.exists(film_storage_path):
    os.mkdir(film_storage_path)

# Створення папок від A до Z у папці "film_storage"
for letter in string.ascii_uppercase:
    letter_path = os.path.join(film_storage_path, letter)
    if not os.path.exists(letter_path):
        os.mkdir(letter_path)

print("Папки від A до Z створено успішно.")
