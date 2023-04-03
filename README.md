# Working Days Calculator 

Python code for a the problem **"Calculate the number of working days from today to a future date"** (country: THAILAND)


## Usage:

```
git clone https://github.com/krrish7788/WorkingDaysCalculator.git
```

### Method - 1: Using the Python library "holidays" to get the national holidays

**Requirnments**
```
pip install holidays
```
**Usage**
```
python using_library.py --check_date 2025-01-25
```
**Args**
```
[--help] or [--h] for help 
[--check_date] to input the date, format: yyyy-mm-dd
[--sat] to include saturday as a working day
[--country_code] to select the country based on the codes in https://pypi.org/project/holidays/ (default: Thailand: TH)
```

### Method - 2: Using the Selenium to scrap the national holidays from https://www.timeanddate.com/calendar/

**Requirnments**
```
pip install selenium
pip install datefinder
pip install webdriver-manager
```
**Usage**
```
python3 using_scraper.py --check_date 2025-01-25
```
**Args**
```
[--help] or [--h] for help
[--check_date] to input the date, format: yyyy-mm-dd
[--sat] to include saturday as a working day
[--country_code] to select the country based on the codes in https://www.timeanddate.com/calendar/ (default: Thailand: 68)
```

### Cheers!
