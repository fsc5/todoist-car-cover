import logging
from weather_api import WeatherStat


FREEZE_TEMP = 0

# Temperature that is very near to the freeze point so
# you might want to cover even if it wont hit the freeze point
NEAR_FREEZE_TEMP = 2

# Number of times it is okay to hit the near freeze point
ACCEPTED_NEAR_FREEZE_TIMES = 5


def is_cover_needed(stats: list[WeatherStat]) -> bool:
    times_near_freeze = 0
    drop_zero = False
    for stat in stats:
        if stat.temp <= 0:
            time_str = stat.time.strftime("%H:%M:%S")
            logging.info(
                f"Temperature is dropping to {stat.temp} at {time_str}")
            drop_zero = True
            break
        elif stat.temp <= NEAR_FREEZE_TEMP:
            times_near_freeze += 1
    logging.info(f"Near freeze is hit {times_near_freeze} times!")
    return drop_zero or times_near_freeze > ACCEPTED_NEAR_FREEZE_TIMES
