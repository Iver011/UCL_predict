import pandas as pd
from bs4 import BeautifulSoup
import requests


def get_matches(fase):
    web=f'https://en.wikipedia.org/wiki/2023-24_UEFA_Champions_League_{fase}'
    response=requests.get(web)
    content= response.text
    soup=BeautifulSoup(content,'lxml')
    matches=soup.find_all('div', class_="footballbox")
    home=[]
    score=[]
    away=[]

    for match in matches:
        home.append(match.find('th',class_='fhome').get_text())
        score.append(match.find('th',class_='fscore').get_text())
        away.append(match.find('th',class_='faway').get_text())


    dict_football={'Home':home,'Score':score,'Away':away}
    df_ucl=pd.DataFrame(dict_football)
    return df_ucl

ucl=['group_stage','knockout_phase']
uefa=[]
for fase in ucl:
    uefa_match=get_matches(fase)
    uefa.append(uefa_match)
    
df_uefa=pd.concat(uefa,ignore_index=True)
df_uefa.to_csv("UEFA_matches_2024.csv",index=False)
