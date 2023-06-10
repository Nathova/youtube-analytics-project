import datetime

from src.video import PLVideo

if __name__ == '__main__':
    pl = PLVideo('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    assert pl.video_title == "Moscow Python Meetup №81"
    assert pl.video_id == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

    duration = pl.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0

    assert pl.show_best_video == "https://youtu.be/cUGyMzWQcGM"

