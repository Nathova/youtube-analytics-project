import json
import os
import isodate

from googleapiclient.discovery import build

import isodate


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    @classmethod
    def get_service(cls):
        """Класс-метод, возвращающий объект для работы с YouTube API"""
        return cls.youtube

    def __init__(self, __channel_id: str) -> None
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = str(__channel_id)
        channel = Channel.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        self.title = channel["items"][0]["snippet"]["title"]
        self.description = channel["items"][0]["snippet"]["description"]
        self.url = channel["items"][0]["snippet"]["thumbnails"]["default"]["url"]
        self.subscriber_count = channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = channel["items"][0]["statistics"]["videoCount"]
        self.view_count = channel["items"][0]["statistics"]["viewCount"]



    @property
    def channel_id(self):
        """Геттер для приватного атрибута channel_id"""
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
       """Сеттер для приватного атрибута channel_id"""
       self.__channel_id = channel_id


    def __str__(self):
        """Выведение названия канала и ссылки"""
        return f'{self.title}, {self.url}'

    def __add__(self, other):
        """Метод для сложения колличества подписчиков каналов"""
        return self.subscriber_count + other.number_of_subscribers

    def __sub__(self, other):
        """Метод для операции вычитания"""
        return self.subscriber_count - other.number_of_subscribers

    def __lt__(self, other):
        """Для операции сравнения «меньше»"""
        return self.subscriber_count < other.number_of_subscribers

    def __le__(self, other):
        """Для сравнения «меньше» или «равно»"""
        return self.subscriber_count <= other.number_of_subscribers

    def __gt__(self, other):
        """Метод для операции сравнения «больше»"""
        return self.subscriber_count > other.number_of_subscribers

    def __ge__(self, other):
        """Метод для операции сравнения «больше» или «равно»"""
        return self.subscriber_count >= other.number_of_subscribers


    def print_info(self) -> None:
        """Выводит информацию о канале"""
        channel = Channel.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        info = json.dumps(channel, indent=2, ensure_ascii=False)
        print(info)

    def to_json(self, file_name):
        yt_dict = {}
        yt_dict["id"] = self.__channel_id
        yt_dict["title"] = self.title
        yt_dict["description"] = self.description
        yt_dict["url"] = self.url
        yt_dict["subscriber_count"] = self.subscriber_count
        yt_dict["video_count"] = self.video_count
        yt_dict["view_count"] = self.view_count
        with open(file_name, 'w', encoding="UTF-8") as file:
            json.dump(yt_dict, file, indent=2, ensure_ascii=False)


