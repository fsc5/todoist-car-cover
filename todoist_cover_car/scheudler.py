from datetime import datetime
import schedule
import time
import sys
from config import Config
from todoist_api_python.api import TodoistAPI
import logging
from weather_api import WeatherApi
import weather_calc

CONFIG_PATH = "./config.yaml"


class CoverCarScheudler:
    config: Config
    todoist_api: TodoistAPI
    weather: WeatherApi

    def __init__(self, config: Config, log_file_path: str) -> None:
        self.config = config
        self.todoist_api = TodoistAPI(config.todoist_key)
        self.weather = WeatherApi(config.openweather_key, config.wake_up_time)

    def exportCoverTask(self) -> None:
        self.todoist_api.add_task(
            content=config.task_content,
            section_id=config.section_id,
            project_id=config.project_id,
            due_string="today",
            priority=4)

    def check(self) -> None:
        weather_stats = self.weather.load_weather(
            config.latitude, config.longitude)
        if weather_calc.is_cover_needed(weather_stats):
            logging.info("Creating task!")
            self.exportCoverTask()

    def run(self) -> None:
        schedule.every().day.at(config.checking_time).do(self.check)
        while True:
            try:
                schedule.run_pending()
            except Exception as e:
                logging.error(str(e))
            time.sleep(60)


if __name__ == "__main__":
    config = Config()
    config.load(CONFIG_PATH)
    log_file_path = f'{config.log_folder}{config.log_base_name}{datetime.now().strftime("%m%d%Y")}.log'
    logging.basicConfig(filename=log_file_path,
                        level=logging.DEBUG,
                        filemode="a",
                        format="%(asctime)s %(levelname)s:%(message)s")
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    scheulder = CoverCarScheudler(config, log_file_path)
    scheulder.run()
