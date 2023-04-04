from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date, datetime, timedelta
import argparse
import datefinder
from collections import OrderedDict

country_codes = ['Australia: 29', 'Canada: 27', 'India: 35', 'Ireland: 32', 'New Zealand: 30', 'United Kingdom: 9', 'United States: 1', 'Afghanistan: 160', 'Albania: 93', 'Algeria: 123', 'American Samoa: 207', 'Andorra: 97', 'Angola: 127', 'Anguilla: 217', 'Antigua and Barbuda: 221', 'Argentina: 37', 'Armenia: 102', 'Aruba: 177', 'Australia: 29', 'Austria: 36', 'Azerbaijan: 85', 'Bahamas: 110', 'Bahrain: 133', 'Bangladesh: 233', 'Barbados: 112', 'Belarus: 83', 'Belgium: 31', 'Belize: 193', 'Benin: 148', 'Bermuda: 113', 'Bhutan: 198', 'Bolivia: 53', 'Bosnia and Herzegovina: 86', 'Botswana: 144', 'Brazil: 33', 'British Virgin Islands: 224', 'Brunei: 79', 'Bulgaria: 73', 'Burkina Faso: 165', 'Burundi: 166', 'Cambodia: 140', 'Cameroon: 134', 'Canada: 27', 'Cape Verde: 157', 'Cayman Islands: 111', 'Central African Republic: 167', 'Chad: 161', 'Chile: 43', 'China: 41', 'Colombia: 46', 'Comoros: 172', 'Congo DR: 84', 'Cook Islands: 208', 'Costa Rica: 58', 'Croatia: 28', 'Cuba: 51', 'Curaçao: 189', 'Cyprus: 94', 'Czechia: 3', 'Denmark: 2', 'Djibouti: 153', 'Dominica: 229', 'Dominican Republic: 52', 'Ecuador: 49', 'Egypt: 80', 'El Salvador: 55', 'Equatorial Guinea: 61', 'Eritrea: 168', 'Estonia: 72', 'Ethiopia: 81', 'Falkland Islands: 219', 'Faroe Islands: 175', 'Fiji: 180', 'Finland: 24', 'France: 5', 'French Guiana: 235', 'French Polynesia: 205', 'Gabon: 150', 'Gambia: 149', 'Georgia: 87', 'Germany: 8', 'Ghana: 118', 'Gibraltar: 119', 'Greece: 11', 'Greenland: 138', 'Gregorian calendar: 22', 'Grenada: 182', 'Guadeloupe: 236', 'Guam: 188', 'Guatemala: 50', 'Guernsey: 191', 'Guinea: 169', 'Guinea-Bissau: 173', 'Guyana: 227', 'Haiti: 103', 'Honduras: 54', 'Hong Kong: 42', 'Hungary: 12', 'Iceland: 88', 'India: 35', 'Indonesia: 65', 'Iran: 75', 'Iraq: 109', 'Ireland: 32', 'Isle of Man: 234', 'Israel: 34', 'Italy: 13', 'Ivory Coast: 125', 'Jamaica: 117', 'Japan: 26', 'Jersey: 192', 'Jordan: 44', 'Julian calendar: 23', 'Kazakhstan: 82', 'Kenya: 105', 'Kiribati: 194', 'Kosovo: 120', 'Kuwait: 108', 'Kyrgyzstan: 136', 'La Réunion: 176', 'Laos: 200', 'Latvia: 89', 'Lebanon: 121', 'Lesotho: 163', 'Liberia: 129', 'Libya: 124', 'Liechtenstein: 96', 'Lithuania: 90', 'Luxembourg: 17', 'Macau: 186', 'Madagascar: 156', 'Malawi: 162', 'Malaysia: 69', 'Maldives: 201', 'Mali: 152', 'Malta: 95', 'Marshall Islands: 213', 'Martinique: 181', 'Mauritania: 210', 'Mauritius: 143', 'Mayotte: 171', 'Mexico: 40', 'Micronesia: 211', 'Moldova: 91', 'Monaco: 99', 'Mongolia: 185', 'Montenegro: 101', 'Montserrat: 220', 'Morocco: 106', 'Mozambique: 126', 'Myanmar: 190', 'Namibia: 130', 'Nauru: 215', 'Nepal: 187', 'New Caledonia: 204', 'New Zealand: 30', 'Nicaragua: 57', 'Niger: 158', 'Nigeria: 77', 'Norfolk Island: 237', 'North Korea: 183', 'North Macedonia: 92', 'Northern Mariana Islands: 225', 'Norway: 18', 'Oman: 135', 'Pakistan: 64', 'Palau: 212', 'Panama: 60', 'Papua New Guinea: 202', 'Paraguay: 56', 'Peru: 47', 'Philippines: 67', 'Poland: 14', 'Portugal: 15', 'Puerto Rico: 114', 'Qatar: 107', 'Republic of the Congo: 151', 'Romania: 19', 'Russia: 20', 'Rwanda: 128', 'Saint Barthélemy: 232', 'Saint Helena: 170', 'Saint Kitts and Nevis: 226', 'Saint Lucia: 218', 'Saint Martin: 231', 'Saint Pierre and Miquelon: 228', 'Saint Vincent and the Grenadines: 222', 'Samoa: 206', 'San Marino: 98', 'São Tomé and Príncipe: 174', 'Saudi Arabia: 74', 'Senegal: 147', 'Serbia: 38', 'Seychelles: 154', 'Sierra Leone: 164', 'Singapore: 63', 'Sint Maarten: 230', 'Slovakia: 39', 'Slovenia: 45', 'Solomon Islands: 209', 'Somalia: 137', 'South Africa: 62', 'South Korea: 70', 'South Sudan: 146', 'Spain: 16', 'Sri Lanka: 116', 'Sudan: 145', 'Suriname: 178', 'Swaziland: 155', 'Sweden: 21', 'Switzerland: 10', 'Syria: 132', 'Taiwan: 71', 'Tajikistan: 197', 'Tanzania: 115', 'Thailand: 68', 'The Netherlands: 25', 'Timor-Leste: 199', 'Togo: 159', 'Tonga: 195', 'Trinidad and Tobago: 104', 'Tunisia: 122', 'Turkey: 4', 'Turkmenistan: 196', 'Turks and Caicos Islands: 223', 'Tuvalu: 214', 'U.S. Virgin Islands: 179', 'Uganda: 139', 'Ukraine: 76', 'United Arab Emirates: 66', 'United Kingdom: 9', 'United States: 1', 'Uruguay: 59', 'Uzbekistan: 184', 'Vanuatu: 203', 'Vatican City: 100', 'Venezuela: 48', 'Vietnam: 78', 'Wallis and Futuna: 216', 'Yemen: 131', 'Zambia: 142', 'Zimbabwe: 141']


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

    # Setting up the chrome driver
    options = Options()
    options.headless = True
    exe_path = '/home/krrish/.wdm/drivers/chromedriver/linux64/110.0.5481/chromedriver'
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    date_today = datetime.strptime(str(date.today()), "%Y-%m-%d")

    # Check the date is in past or present
    if date_today < check_date:
        start, end = date_today, check_date
    else:
        start, end = check_date, date_today

    days = OrderedDict(((start + timedelta(_)), None) for _ in range((end - start).days + 1)).keys()
    tmp_year_list = list(OrderedDict.fromkeys([_.year for _ in days]))

    for tmp_year in tmp_year_list:
        # Scrap Thai holidays from https://www.timeanddate.com/calendar/ based on the year
        url = f"https://www.timeanddate.com/calendar/custom.html?year={tmp_year}&country={country_code}&df=1&hol=9"
        driver.get(url)
        main_table = driver.find_element(By.XPATH, "//table[@id='ch1']/tbody/tr/td/table")  # XPATH of the holidays data
        holidays = list(datefinder.find_dates(main_table.text))
        holidays = list(OrderedDict.fromkeys([(day.day, day.month) for day in holidays]))  # holiday list
        for tmp_day in days:
            if tmp_year == tmp_day.year:
                # Check for working days
                if is_workday(tmp_day, sat):
                    # Check for holidays
                    if (tmp_day.day, tmp_day.month) not in holidays:
                        working_days += 1
                    else:
                        thai_holidays += 1
                else:
                    weekends += 1

    driver.quit()
    return f"Number of Working Days: {working_days}\nNumber of Holidays: {thai_holidays}\n" \
           f"Number of Weekends: {weekends}"


# Command line args
def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check_date', type=date_format_checker, default="2023-12-31", help='Enter a date, for '
                                                                                             'example: yyyy-mm-dd')
    parser.add_argument('--sat', default=False, action='store_true', help='Include saturday as a working day')
    parser.add_argument('--country_code', type=int, default=68, help=f'Country codes in '
                                                                     f'https://www.timeanddate.com/calendar/ '
                                                                     f'(default: Thailand:68) {country_codes}')
    opt = parser.parse_args()
    return opt


if __name__ == '__main__':
    print(get_days(**vars(parse_opt())))