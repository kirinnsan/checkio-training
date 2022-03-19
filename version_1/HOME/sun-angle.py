from typing import Union
from datetime import datetime


def sun_angle(time_str: str) -> Union[int, str]:
    target_time = datetime.strptime(time_str, '%H:%M')
    start_time = datetime.strptime('06:00', '%H:%M')
    end_time = datetime.strptime('18:00', '%H:%M')
    if target_time < start_time or target_time > end_time:
        return "I don't see the sun!"
    one_hor_angle = 90 / 6
    one_minute_angle = one_hor_angle / 60
    progress_minute = (target_time - start_time).seconds / 60
    result_angle = round(progress_minute * one_minute_angle, 2)
    return result_angle


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
