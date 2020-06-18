import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

page = requests.get('https://www.chucknorrisfacts.fr/facts/mtop')
soup = BeautifulSoup(page.content, 'html.parser')
body = soup.find(id = 'corps')
fact_list = body.find(id = 'factslist')
facts = fact_list.find_all(class_ = 'fact')

facts_nums = [re.sub(r"[^\w]", '', fact.find(class_ = 'head').get_text()) for fact in facts]
facts_bodies = [re.sub("Votez !", '', fact.find(class_ = 'factbody').get_text()) for fact in facts]

data = pd.DataFrame(
    {
        'id': facts_nums,
        'body': facts_bodies
    })

print(data.iloc[0, 1])

