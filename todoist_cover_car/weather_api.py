from dataclasses import dataclass
from datetime import datetime, timedelta
import requests


@dataclass
class WeatherStat:
    temp: int
    time: datetime


class WeatherApi:
    api_key: str
    wake_up: datetime

    def __init__(self, api_key: str, wake_up: datetime) -> None:
        self.api_key = api_key
        self.wake_up = wake_up

    def load_weather(self, lat: str, lon: str) -> list[WeatherStat]:
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude=current,minutely,daily,alerts&appid={self.api_key}")
        if data.status_code != 200:
            raise IOError(
                f"Openweather responded with error {data.status_code}")

        hourly_data = data.json()['hourly']
        all_stats = [WeatherStat(stat['temp'], datetime.utcfromtimestamp(
            stat['dt'])) for stat in hourly_data]

        # get wake up time of next day
        end_time = (all_stats[0].time + timedelta(days=1)
                    ).replace(hour=self.wake_up.hour, minute=self.wake_up.minute)
        # use only stats that are before that point
        return [stat for stat in all_stats if stat.time <= end_time]
