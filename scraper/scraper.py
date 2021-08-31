import requests
from bs4 import BeautifulSoup
import os
import warnings
import time
import numpy as np
import pandas as pd
import pycountry
import string
import random
warnings.simplefilter(action='ignore', category=FutureWarning)

def findCountryAlpha2 (country_name):
    try:
        return pycountry.countries.get(name=country_name).alpha_2
    except:
        try:
            return (pycountry.countries.get(common_name=country_name).alpha_2)
        except:
            try:
                return (pycountry.countries.get(alpha_2=country_name).alpha_2)
            except:
                try:
                    return (pycountry.countries.get(alpha_3=country_name).alpha_2)
                except:
                    return (''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))
def findCountryAlpha3 (country_name):
    try:
        return pycountry.countries.get(name=country_name).alpha_3
    except:
        try:
            return pycountry.countries.get(common_name=country_name).alpha_3
        except:
            try:
                return (pycountry.countries.get(alpha_2=country_name).alpha_3)
            except:
                try:
                    return (pycountry.countries.get(alpha_3=country_name).alpha_3)
                except:
                    return (''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))
def findCountryNumeric (country_name):
    try:
        return pycountry.countries.get(name=country_name).numeric
    except:
        try:
            return pycountry.countries.get(common_name=country_name).numeric
        except:
            try:
                return (pycountry.countries.get(alpha_2=country_name).numeric)
            except:
                try:
                    return (pycountry.countries.get(alpha_3=country_name).numeric)
                except:
                    return (''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))

def findCountryOfficialName (country_name):
    try:
        return pycountry.countries.get(name=country_name).official_name
    except:
        try:
            return pycountry.countries.get(common_name=country_name).official_name
        except:
            try:
                return (pycountry.countries.get(alpha_2=country_name).official_name)
            except:
                try:
                    return (pycountry.countries.get(alpha_3=country_name).official_name)
                except:
                    return (''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))


while(True):
    page = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(page.content, 'lxml')

    table = soup.find('table', attrs={'id': 'main_table_countries_today'})
    rows = table.find_all("tr", attrs={"style": ""})
    data = []
    for i,item in enumerate(rows):

        if i == 0:

            data.append(item.text.strip().split("\n")[:13])

        else:
            data.append(item.text.strip().split("\n")[:12])

    dt = pd.DataFrame(data)
    df = pd.DataFrame(data[1:], columns=data[0][:12]) #Formatting the header
    world_ = df.loc[0, :].values
    world_ = np.insert(world_, 0, 0)
    world_ = np.delete(world_, -1, 0)
    world_ = pd.Series(world_, index=list(df))
    df.loc[0] = world_
    df.rename(columns = {"#":"id"}, inplace=True)
    df.drop(df.tail(1).index, inplace=True)
    df.sort_values('Country,Other', ignore_index=True, inplace=True)
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df.fillna(0, inplace=True)
    df['iso2'] = df.apply(lambda row: findCountryAlpha2(row['Country,Other']) , axis = 1)
    df['iso3'] = df.apply(lambda row: findCountryAlpha3(row['Country,Other']) , axis = 1)
    df['country_numeric'] = df.apply(lambda row: findCountryNumeric(row['Country,Other']) , axis = 1)
    
    # df = dd.from_pandas(dt,npartitions=1)

    df.to_csv('../data/data_latest.csv', index = False) # On Unix Based System
    # df.to_csv('./data/data_latest.csv', index = False) # On Windows System, Literally it sucks when it comes to hosting!
    # 1 Hour Time Delay
    time.sleep(3600)