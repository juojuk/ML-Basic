# from abc import ABC, abstractmethod
from datetime import datetime
# from typing import Optional

# === Базовый класс ===
class MediaFile():
    def __init__(self, name: str, size: int, created_at: datetime, owner: str):
        self.name = name
        self.size = size
        self.created_at = created_at
        self.owner = owner

    # @abstractmethod
    def get_metadata(self) -> dict:
        raise NotImplementedError("Этот метод должен быть переопределён.")

    def delete(self):
        print(f"Удаление файла: {self.name}")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        print(f"Файл {self.name} обновлён.")

# === Аудио ===
class AudioFile(MediaFile):
    def __init__(self, name: str, size: int, created_at: datetime, owner: str, duration: float, codec: str):
        super().__init__(name, size, created_at, owner)
        self.duration = duration
        self.codec = codec

    def get_metadata(self) -> dict:
        return {
            "type": "audio",
            "name": self.name,
            "duration": self.duration,
            "codec": self.codec
        }

    def convert(self, new_codec: str):
        print(f"Конвертация аудио {self.name} в формат {new_codec}")
        self.codec = new_codec

# === Видео ===
class VideoFile(MediaFile):
    def __init__(self, name: str, size: int, created_at: datetime, owner: str, resolution: str, frame_rate: float):
        super().__init__(name, size, created_at, owner)
        self.resolution = resolution
        self.frame_rate = frame_rate

    def get_metadata(self) -> dict:
        return {
            "type": "video",
            "name": self.name,
            "resolution": self.resolution,
            "frame_rate": self.frame_rate
        }

    def extract_frames(self):
        print(f"Извлечение кадров из видео {self.name}")

# === Фото ===
class PhotoFile(MediaFile):
    def __init__(self, name: str, size: int, created_at: datetime, owner: str, resolution: str, color_mode: str):
        super().__init__(name, size, created_at, owner)
        self.resolution = resolution
        self.color_mode = color_mode

    def get_metadata(self) -> dict:
        return {
            "type": "photo",
            "name": self.name,
            "resolution": self.resolution,
            "color_mode": self.color_mode
        }

    def extract_features(self):
        print(f"Извлечение признаков из изображения {self.name}")


# Проверяем
audioFile = AudioFile("Песня", 50, datetime.now(), "User1", 180.0, "mp3")
audioFile.convert("wav")