import json
import os
import isodate

from googleapiclient.discovery import build

import isodate

from helper.youtube_api_manual import printj

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = str(channel_id)

    def print_info(self, dict_to_print, indent, ensure_asci) -> None:
        """Выводит в консоль информацию о канале."""
        return json.dumps(dict_to_print, indent=2, ensure_ascii=False)

        @classmethod
        def get_service():
            return Channel

    def to_json(title, video_count, url):
        file = open("file.json", "w")
        file.write(title, video_count, url)
        return file

