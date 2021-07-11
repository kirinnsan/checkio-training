from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None) -> int:
    """
        how long the light bulb has been turned on
    """
    if start_watching is None and end_watching is None:
        els = els if len(els) % 2 == 0 else els[:-2]
        time_list = [els[i+1] - els[i] for i in range(0, len(els), 2)]
        total_time = sum([time.total_seconds() for time in time_list])
        return total_time
    else:
        start_index = 0
        end_index = -1
        for i, el in enumerate(els):
            if i % 2 == 0:
                # 点灯
                if start_watching >= els[i]:
                    els[i] = start_watching
                    start_index = i
            else:
                # 消灯
                if end_watching <= els[i]:
                    els[i] = end_watching
                    end_index = i
        if len(els) % 2 == 0 and end_index == -1:
            els.append(end_watching)
        elif len(els) % 2 == 0:
            els = els if len(els) % 2 == 0 else els[:-2]

        time_list = [els[i+1] - els[i]
                     for i in range(start_index, end_index, 2)]
        total_time = sum([time.total_seconds() for time in time_list])
        return total_time


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10)))

    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        start_watching=datetime(2015, 1, 12, 10, 0, 0),
        end_watching=datetime(2015, 1, 12, 10, 0, 10)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 7)) == 7

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 3),
        datetime(2015, 1, 12, 10, 0, 10)) == 7

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 10),
        datetime(2015, 1, 12, 10, 0, 20)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 30, 0),
        datetime(2015, 1, 12, 11, 0, 0)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 0)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 10)) == 20

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 9, 50, 0),
        datetime(2015, 1, 12, 10, 0, 10)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 9, 0, 0),
        datetime(2015, 1, 12, 10, 5, 0)) == 300

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 11, 5, 0),
        datetime(2015, 1, 12, 12, 0, 0)) == 310

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 11, 5, 0),
        datetime(2015, 1, 12, 11, 10, 0)) == 300

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 10)) == 20

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 10, 0),
        datetime(2015, 1, 12, 10, 20, 20)) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 10, 0),
        datetime(2015, 1, 12, 10, 20, 20)) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 9, 0),
        datetime(2015, 1, 12, 10, 0, 0)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 9, 0),
        datetime(2015, 1, 12, 10, 0, 10)) == 10

    print("The third mission in series is completed? Click 'Check' to earn cool rewards!")
