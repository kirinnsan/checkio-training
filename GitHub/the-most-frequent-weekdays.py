from collections import defaultdict, Counter
from datetime import datetime, timedelta
DAYS = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']


def most_frequent_days(year):
    date = datetime(year, 1, 1)
    d = defaultdict(int)
    while date < datetime(year + 1, 1, 1):
        d[DAYS[date.weekday()]] += 1
        date += timedelta(days=1)
    return sorted([i for i in d if d[i] == max(d.values())], key=DAYS.index)
    
    # q_ty_of_days = [0, 0, 0, 0, 0, 0, 0]
    # days = ['Monday', 'Tuesday', 'Wednesday',
    #         'Thursday', 'Friday', 'Saturday', 'Sunday']
    # answer = []
    # for month in range(1, 13):
    #     calendar_of_month = calendar.monthcalendar(year, month)
    #     for week in calendar_of_month:
    #         for day_of_the_week in range(7):
    #             if week[day_of_the_week]:
    #                 q_ty_of_days[day_of_the_week] += 1
    # start = 0
    # max_value = max(q_ty_of_days)
    # for i in range(q_ty_of_days.count(max_value)):
    #     day = q_ty_of_days.index(max_value, start)
    #     answer.append(days[day])
    #     start = day + 1
    # return answer

    # week_dict = {}
    # for month in range(1, 13, 1):
    #     calendar_of_month = calendar.monthcalendar(year, month)
    #     for i, week in enumerate(calendar_of_month):
    #         for day in week:
    #             # these are empty days in a monthly calendar
    #             if day[0] == 0 and i != 0:
    #                 break
    #             day_name_index = day[1]
    #             if day_name_index not in week_dict:
    #                 week_dict[day_name_index] = 0
    #             week_dict[day_name_index] += 1
    # max_day_name_index_list = [
    #     kv[0] for kv in week_dict.items() if kv[1] == max(week_dict.values())]
    # return [calendar.day_name[max_day_name_index]
    #         for max_day_name_index in max_day_name_index_list]


if __name__ == '__main__':
    print("Example:")
    print(most_frequent_days(1084))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']
    print("Coding complete? Click 'Check' to earn cool rewards!")
