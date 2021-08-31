# Covid19-API
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) 

An opensource Covid19 API (currently uses worldometer only)

## Usage

On VPS (Unix Based Systems)
1. Clone the Repository
    + `git clone https://github.com/AmreshSinha/Covid19-API`
2. Install dependencies
2. Run `scraper.py`
    + `python scraper.py`
    + Note: The Scraper has a time interval of 1 hour by default
3. Run Flask App with Gunicorn or Waitress
4. If you want to host for web then update your rules in nginx accordingly and get one ssl

## Contribution

There is a lot of work still remaining. Some of which:
1. Adding more sources
2. Cleaning Data
3. Adding provinces covid data under their parent country.
4. Making our own pycountry module fork according to our needs.

For Extra features you want to contribute open an issue first.
