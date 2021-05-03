from alwan import *

from bs4 import BeautifulSoup

from func import _headers, out, Request, rmhttp, add_http

import re, os

import requests, json


def getinfo(website):
    website = rmhttp(website)

    url = f"https://www.whois.com/whois/{website}"

    try:

        request = Request(url, _timeout=5, _encode=None)

        bs = BeautifulSoup(request, 'html.parser')

        result = bs.find_all('pre', {'class': 'df-raw'})[0].text.encode('UTF-8')

        print(f"\r{c}{result.decode()}")



    except:

        out(v="!", c=g, d="Sorry, whois cannot be performed right now...!!! :[")




