import holidays
from datetime import date, datetime, timedelta
from collections import OrderedDict
import argparse


# Function to check the input date format
def date_format_checker(check_date):
    try:
        check_date = datetime.strptime(check_date, "%Y-%m-%d")
    except:
        raise argparse.ArgumentTypeError(f'Input date {check_date} does not match format yyyy-mm-dd')

    return check_date


# Function to check working days
def is_workday(d, sat):
    no = 6 if sat else 5
    return True if d.weekday() < no else False


def get_days(check_date, sat, country_code):
    thai_holidays, weekends, working_days = 0, 0, 0

    # Get the national holidays of Thailand
    th_holidays = holidays.country_holidays(country_code)
    date_today = datetime.strptime(str(date.today()), "%Y-%m-%d")

    # Check the date is in past or present
    if date_today < check_date:
        start, end = date_today, check_date
    else:
        start, end = check_date, date_today

    days = OrderedDict(((start + timedelta(_)), None) for _ in range((end - start).days + 1)).keys()

    for day in days:
        # Check for working days
        if is_workday(day, sat):
            # Check for holidays
            if day not in th_holidays:
                working_days += 1
            else:
                thai_holidays += 1
        else:
            weekends += 1

    return f"Number of Working Days: {working_days}\nNumber of Holidays: {thai_holidays}\n" \
           f"Number of Weekends: {weekends}"


# Command line args
def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check_date', type=date_format_checker, default="2023-12-31", help='Enter a date, for '
                                                                                             'example: yyyy-mm-dd')
    parser.add_argument('--sat', default=False, action='store_true', help='Include saturday as a working day')
    parser.add_argument('--country_code', type=str, default="TH", help=f'Country codes in '
                                                                       f'https://pypi.org/project/holidays/ '
                                                                       f'(default: Thailand:TH)')
    opt = parser.parse_args()
    return opt


if __name__ == '__main__':
    print(get_days(**vars(parse_opt())))
