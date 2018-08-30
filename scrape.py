#! /usr/local/bin/python3
from bs4 import BeautifulSoup
import requests

RT_BASE_URL = "https://www.rottentomatoes.com/m/{}"

def get_from_RT(title):
    r = requests.get(RT_BASE_URL.format(title))
    return r.content

def get_synopsis(content):
    html = BeautifulSoup(content, 'html.parser')
    return html.find(id='movieSynopsis').text

def get_rating(content):
    html = BeautifulSoup(content, 'html.parser')
    meter = html.find(id='tomato_meter_link')
    meter_wrapper = meter.find_all('span', class_='meter-value')[0]
    return meter_wrapper.find_all('span')[0].text


ct = get_from_RT('shining')
print(get_synopsis(ct))
print("Rating: {}".format(get_rating(ct)))
