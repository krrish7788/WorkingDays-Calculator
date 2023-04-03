# WorkingDays-Calculator ( 

### This repository consists the Python code for a the problem "Calculate the number of working days from today to a future date" (default country: THAILAND)

## Usage:

> git clone https://github.com/krrish7788/WorkingDaysCalculator.git

### Method - 1: Using the Python library "holidays" to get the national holidays

> pip install holidays

> python3 using_library.py --check_date 2025-01-25  (normal usage)
> python3 using_library.py --check_date 2025-01-25 --sat  (to include saturday as a working day)
> python3 using_library.py --check_date 2025-01-25 --sat --country_code TH (country codes in https://pypi.org/project/holidays/ (default: Thailand:TH)) 
**python3 using_library.py --help or python3 using_library.py --h  (for help)**


### Method - 2: Using the Selenium to scrap the national holidays from https://www.timeanddate.com/calendar/

> pip install selenium
> pip install webdriver-manager
> pip install datefinder

> python3 using_scraper..py --check_date 2025-01-25  (normal usage)
> python3 using_scraper.py --check_date 2025-01-25 --sat  (to include saturday as a working day)
> python3 using_scraper.py --check_date 2025-01-25 --sat --country_code 68 (country codes in https://www.timeanddate.com/calendar/ (default: Thailand:68)) 
**python3 using_scraper.py --help or python3 using_scraper.py --h  (for help)**


**Cheers!**
