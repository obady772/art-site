from alwan import *

import requests

import re

_headers = {

    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',

    'Accept-Encoding': 'gzip,deflate,sdch',

    'Accept-Language': 'en-US,en;q=0.8',

    'Connection': 'keep-alive'

}

empty_site = f"\n\t{r}[=] Please Enter A site :/\n\t\t{c}~ obady772 :)"

wrong_URL = f"\n\t{r}[=] Please Enter  Correct URL (i.e, hackthissite.org, hack.me)\n\t\t{c}obady__772 :)"

str_Ind = f"\n\t{r}[=] Please Input a Integer (i.e, 1, 2, 3) :\\\n\t\t{c}~ obady772 :)"

val_Select = f"\t{r}[$] Please Use The Index Value From The List\n\t\t[+] Not By Your Own :/\n\t\t\t ~ obady772  \n"


def site_note_empyt(site):
  
    if len(site) >= 1:

        return "valid"

    else:

        return "!valid"


def psite(site):


    web = site_note_empyt(site)

    if web is "valid":

        if not (re.match(r"(^(http://|https://)?([a-z0-9][a-z0-9-]*\.)+[a-z0-9][a-z0-9-]*$)", site)):
            exit(wrong_URL)



    else:

        exit(empty_site)


def clearsite(site):


    web = psite(site)

    site = site.replace("http://", "")
    site = site.replace("http://www.", "")
    site = site.replace("https://", "")
    site = site.replace("https://www.", "")
    site = site.replace("www.", "");
    return (site)


def rmhttp(site):


    site = clearsite(site);
    return (site)


def add_http(site):
  

    site = clearsite(site)

    site = ("http://" + site);
    return (site)


def out(v, c, d):
    if v == None:

        print(f"{c}{str(d)}")



    elif v != None:

        print(f"{w}[{g}{v}{w}]{c} {str(d)}")


def Request(site, _timeout=None, _encode=None):


    try:

        if _encode == None:

            return requests.get(site, headers=_headers, timeout=_timeout).content



        elif _encode == True:

            return requests.get(site, headers=_headers, timeout=_timeout).text.encode('utf-8')



    except requests.exceptions.MissingSchema:

        pass



    except requests.exceptions.ContentDecodingError:

        pass



    except requests.exceptions.ConnectionError:

        return fg + sb + "\n[$] Err0r: Sorry! You Entered A Wrong site 0r site Is 0ff"

        pass



    except Exception as e:

        return fc + sb + "[$] Err0r: " + fg + sb + str(e)

        pass
