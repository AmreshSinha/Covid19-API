# Covid19-API
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) 

An opensource Covid19 API (currently uses worldometer only)

## Output

### Examples

- Covid19 Every Country Data
    + Request URL
        ```
        <your-ip>/api/all
        ```
    + [Response](https://gist.github.com/AmreshSinha/d4baf9eb526eea77bec7e72aac7c0c58)

- Covid19 WorldWide Summarised Data
    + Request URL
        ```
        <your-ip>/api/world
        ```
    + [Response](https://gist.github.com/AmreshSinha/0044c62b2352f36cccf2b46f937f140d)

- Covid19 India Data
    + Request URL
        ```
        <your-ip>/api/country?req=ind
        ```
        or

        ```
        <your-ip>/api/country?req=in
        ```
        
    + [Response](https://gist.github.com/AmreshSinha/bea8419175170d5994300b690afe1001)
    

## Usage

On VPS (Unix Based Systems)

Without Docker

1. Clone the Repository
    + `git clone https://github.com/AmreshSinha/Covid19-API`
2. Install dependencies
    + `pip install -r requirements.txt`
2. Run `scraper.py`
    + `python scraper/scraper.py`
    + Note: The Scraper has a time interval of 1 hour by default
3. Run Flask App with Gunicorn or Waitress
    + Like for waitress the `waitress_server.py` is there
    + `python waitress_server.py`
4. If you want to host for web then update your rules in nginx accordingly and get one ssl certificate

With Docker

1. Clone the Repository
    + `git clone https://github.com/AmreshSinha/Covid19-API`
2. Build Docker Image
    + `docker build -t covid19-api:1.0 .`
3. Run Container
    + `docker container run --name covid19-api-web -p 80:80 covid19-api:1.0`
    + The container will start running with PORT 80 exposed to Public.
4. To Stop the Container
    + `docker container stop covid19-api-web`

## Contribution

There is a lot of work still remaining. Some of which:
1. Adding more sources
2. Cleaning Data
3. Adding provinces covid data under their parent country.
4. Making our own pycountry module fork according to our needs.

For Extra features (other than the above) you want to contribute, open an issue first.
