from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None) -> int:

    if len(els) % 2:
        els.append(datetime.max)

    sw = start_watching or els[0]
    ew = end_watching or datetime.max

    return int(sum((min(ew, els[i + 1]) - max(sw, els[i])).total_seconds()
                   for i in range(0, len(els), 2) if sw <= els[i + 1] and ew >= els[i]))
