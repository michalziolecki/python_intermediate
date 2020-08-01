def get_day_of_week_by_number(val: int) -> str:
    days = {
        1: 'Mon',
        2: 'Tue',
        3: 'Wed',
        4: 'Thu',
        5: 'Fri',
        6: 'Sat',
        7: 'Sun'
    }

    return days.get(val, 'INCORRECT_VAL')

