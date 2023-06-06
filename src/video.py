import os
import datetime
import isodate
from googleapiclient.discovery import build
from datetime import timedelta

from helper.youtube_api_manual import youtube


class Video:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def __init__(self, video_id):
        try:
            self.video_info = youtube.get_video(video_id)
            self.video_id = self.video_info['items'][0]['id']
            self.video_title = self.video_info['items'][0]['snippet']['title']
            self.viewCount = self.video_info['items'][0]['statistics']['viewCount']
            self.likeCount = self.video_info['items'][0]['statistics']['likeCount']
        except IndexError:
            self.video_id = video_id
            self.video_info = None
            self.video_title = None
            self.viewCount = None
            self.likeCount = None
            print(f"Видеоролик с id {self.video_id} не найден/не существует")

    def __str__(self):
        return f'{self.video_title}'


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        try:
            self.video_info = youtube.get_video(video_id)
            self.video_id = self.video_info['items'][0]['id']
            self.video_title = self.video_info['items'][0]['snippet']['title']
            self.viewCount = self.video_info['items'][0]['statistics']['viewCount']
            self.likeCount = self.video_info['items'][0]['statistics']['likeCount']
        except IndexError:
            self.video_id = video_id
            self.video_info = None
            self.video_title = None
            self.viewCount = None
            self.likeCount = None
            print(f"Видео с id {self.video_id} не найдено")

    @property
    def total_duration(self, isodate=None):
        """Метод определения продолжительности плейлиста"""
        videos_info = youtube.get_videos_info(self.playlist_id)
        duration_total = datetime.timedelta()
        for video in videos_info['items']:
            duration_isodate = video['contentDetails']['duration']
            duration = isodate.parse_duration(duration_isodate)
            duration_total += duration
        return duration_total

    @property
    def show_best_video(self):
        return max(self.likeCount)

    @classmethod
    def likeCount(cls):
        pass









