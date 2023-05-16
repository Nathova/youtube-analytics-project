import json
import os
import isodate

from googleapiclient.discovery import build



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


