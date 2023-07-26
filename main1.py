from film_player.films_worker import Film

film_data_1 = {
    "title": "Crazy, Stupid, Love.",
    "description": "A middle-aged husband's life changes dramatically when his wife asks him for a divorce. "
    "He seeks to rediscover his manhood with the help of a newfound friend, Jacob, "
    "learning to pick up girls at bars.",
    "director": ["Glenn Ficarra", "John Requa"],
    "writer": "Dan Fogelman",
    "cast": ["Steve Carell", "Ryan Gosling", "Julianne Moore"],
    "running_time": "118 minutes",
    "country": "United States",
    "language": "English",
    "imdb_rating": "7.4",
    "year": "2011",
    "budget": "$50 million",
    "box_office": "$145 million",
    "profitable": "Yes",
    "oscar_nominated": "No",
    "oscar_win": "No",
    "trailer_link": "https://www.imdb.com/video/vi3722091801/",
}
film_data_2 = {
    "title": "Stupid, Love.",
    "description": "A middle-aged husband's life changes dramatically when his wife asks him for a divorce. "
    "He seeks to rediscover his manhood with the help of a newfound friend, Jacob, "
    "learning to pick up girls at bars.",
    "director": ["Glenn Ficarra", "John Requa"],
    "writer": "Dan Fogelman",
    "cast": ["Steve Carell", "Ryan Gosling", "Julianne Moore"],
    "running_time": "118 minutes",
    "country": "United States",
    "language": "English",
    "imdb_rating": "8,8",
    "year": "2018",
    "budget": "$50 million",
    "box_office": "$145 million",
    "profitable": "Yes",
    "oscar_nominated": "No",
    "oscar_win": "No",
    "trailer_link": "https://www.imdb.com/video/vi3722091801/",
}

# Створюємо екземпляри класу Film для кожного фільму
film_1 = Film(**film_data_1)
film_2 = Film(**film_data_2)

# Доступ до адрес файлів інформації про фільми
print(f"Film 1 storage address: {film_1.get_film_address()}")
print(f"Film 2 storage address: {film_2.get_film_address()}")
