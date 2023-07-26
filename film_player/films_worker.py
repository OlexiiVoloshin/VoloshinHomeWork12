import os


class Film:
    def __init__(
        self,
        title,
        description,
        director,
        writer,
        cast,
        running_time,
        country,
        language,
        imdb_rating,
        year,
        budget,
        box_office,
        profitable,
        oscar_nominated,
        oscar_win,
        trailer_link,
    ):
        self.title = title
        self.description = description
        self.director = director
        self.writer = writer
        self.cast = cast
        self.running_time = running_time
        self.country = country
        self.language = language
        self.imdb_rating = imdb_rating
        self.year = year
        self.budget = budget
        self.box_office = box_office
        self.profitable = profitable
        self.oscar_nominated = oscar_nominated
        self.oscar_win = oscar_win
        self.trailer_link = trailer_link
        self.storage_address = None  # Задаємо початково значення None
        self.upload_file()

    def upload_file(self):
        # Запускаємо цей метод при створенні нового екземпляру фільму
        # Цей метод створює txt файл з назвою фільму у film_storage у відповідній папці
        folder_name = self.title[
            0
        ].upper()  # Перша літера заголовку для визначення папки
        file_name = f"{self.title}.txt"

        film_storage_path = os.path.join(os.getcwd(), "film_player", "film_storage")
        if not os.path.exists(film_storage_path):
            os.mkdir(film_storage_path)

        letter_folder_path = os.path.join(film_storage_path, folder_name)
        if not os.path.exists(letter_folder_path):
            os.mkdir(letter_folder_path)

        file_path = os.path.join(letter_folder_path, file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(
                f"Title:\n  {self.title}\n\nDescription:\n  {self.description}\n\n"
                f"Director:\n  {self.director}\n\nWriter:\n  {self.writer}\n\n"
                f"Cast(actors):\n  {', '.join(self.cast)}\n\nRunning time:\n  {self.running_time} minutes\n\n"
                f"Country:\n  {self.country}\n\nLanguage:\n  {self.language}\n\n"
                f"IMDb RATING:\n  {self.imdb_rating}\n\nYear:\n  {self.year}\n\n"
                f"Budget:\n    {self.budget}\n\nBox office:\n  {self.box_office}\n\n"
                f"Profitable:\n  {self.profitable}\n\nOscar nominated:\n  {self.oscar_nominated}\n\n"
                f"Oscar win:\n  {self.oscar_win}\n\nTrailer:\n  {self.trailer_link}"
            )

        self.storage_address = file_path

    def get_film_address(self):
        # Повертає повний шлях до фільму у дерикторії
        return self.storage_address
