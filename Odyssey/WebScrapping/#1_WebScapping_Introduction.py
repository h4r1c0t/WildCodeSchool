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
facts_bodies = [re.sub("Votez !\n\n\n", ' ', fact.find(class_ = 'factbody').get_text()) for fact in facts]
facts_bodies = [re.sub("\n", "", fact).strip() for fact in facts_bodies]


data = pd.DataFrame(
    {
        'id': facts_nums,
        'body': [re.sub("\d.\d+ / 10", "", fact).strip() for fact in facts_bodies],
        'note': [re.search("\d.\d+ / 10", fact).group(0) for fact in facts_bodies]
    })

data = data.iloc[:9, :]