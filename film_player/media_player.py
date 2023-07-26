class Player:
    def __init__(self, name, video_link, duration):
        self.name = name
        self.video_link = video_link
        self.duration = duration
        self.is_playing = False
        self.last_time = 0
        self.quality = "HD"

    def play(self, file_path):
        # Метод може використовувати file_path, якщо потрібно звернутись до фільму на диску
        if self.video_link:
            self.is_playing = True
            print(f"Playing: {self.name}")
            return True
        return False

    def pause(self):
        if self.is_playing:
            self.is_playing = False
            print("Paused.")
        else:
            print("Nothing is playing to pause.")

    def save_last_time(self, current_time):
        if self.is_playing:
            self.last_time = current_time
            print(f"Last time saved: {self.last_time} seconds.")

    def change_quality(self, new_quality):
        self.quality = new_quality
        print(f"Quality changed to: {self.quality}")

    def __str__(self):
        return f"{self.name} ({self.duration} minutes)"
