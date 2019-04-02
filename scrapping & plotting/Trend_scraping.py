import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

link ="http://eciresults.nic.in/statewise{0}.htm"
ch = [{'code': 'S26', 'name': 'Chattisgarh', 'pages': 9}]
mp = [{'code': 'S12', 'name': 'Madhya Pradesh', 'pages': 23}]
miz = [{'code': 'S16', 'name': 'Mizoram', 'pages': 4}]
rajas = [{'code': 'S20', 'name': 'Rajasthan', 'pages': 20}]
telan = [{'code': 'S29', 'name': 'Telangana', 'pages': 12}]

for state in ch:
    list_records = []
    pages = state['pages']
    for i in range(pages):
        page = requests.get(link.format(state['code']+str('' if(i==0) else i)))
        soup = BeautifulSoup(page.content,'html.parser')
        data_tbody = soup.find("tbody", id="ElectionResult")
        for div in data_tbody.find_all("div", {'class':'tooltip'}):
            div.decompose()
        for span in data_tbody.find_all("span"):
            span.decompose()
        def get_first_child(soup_page, child):
            first_child = soup_page.find(child)
            all_child = [first_child] + first_child.find_next_siblings(child)
            return all_child
        all_trs = get_first_child(data_tbody, 'tr')
        imp_trs = all_trs[4:]
        for tr in imp_trs:
            all_tds = get_first_child(tr, 'td')
            constituency_dict = {
                        'State': state['name'], 'Constituency':all_tds[0].getText(),
                        'Const.No.': int(all_tds[1].getText()), 'Winner':all_tds[2].getText(),
                        'Winner_Party': all_tds[3].getText(), 'Loser':all_tds[4].getText(),
                        'Loser_Party': all_tds[5].getText(), 'Margin': int(all_tds[6].getText()),
                        'Previous_Winner':all_tds[8].getText(), 'Previous_Winner_Party': all_tds[9].getText(),
                        'Previous_Margin': int(all_tds[10].getText() if(all_tds[10].getText()!='') else 0)
                    }
            # print(constituency_dict)
            list_records.append(constituency_dict)
dataframe = pd.DataFrame(list_records)
dataframe.to_csv("trends_Chhattisgarh.csv")


for state in mp:
    list_records = []
    pages = state['pages']
    for i in range(pages):
        page = requests.get(link.format(state['code']+str('' if(i==0) else i)))
        soup = BeautifulSoup(page.content,'html.parser')
        data_tbody = soup.find("tbody", id="ElectionResult")
        for div in data_tbody.find_all("div", {'class':'tooltip'}):
            div.decompose()
        for span in data_tbody.find_all("span"):
            span.decompose()
        def get_first_child(soup_page, child):
            first_child = soup_page.find(child)
            all_child = [first_child] + first_child.find_next_siblings(child)
            return all_child
        all_trs = get_first_child(data_tbody, 'tr')
        imp_trs = all_trs[4:]
        for tr in imp_trs:
            all_tds = get_first_child(tr, 'td')
            constituency_dict = {
                        'State': state['name'], 'Constituency':all_tds[0].getText(),
                        'Const.No.': int(all_tds[1].getText()), 'Winner':all_tds[2].getText(),
                        'Winner_Party': all_tds[3].getText(), 'Loser':all_tds[4].getText(),
                        'Loser_Party': all_tds[5].getText(), 'Margin': int(all_tds[6].getText()),
                        'Previous_Winner':all_tds[8].getText(), 'Previous_Winner_Party': all_tds[9].getText(),
                        'Previous_Margin': int(all_tds[10].getText() if(all_tds[10].getText()!='') else 0)
                    }
            # print(constituency_dict)
            list_records.append(constituency_dict)
dataframe = pd.DataFrame(list_records)
dataframe.to_csv("trends_Madhayapradesh.csv")

for state in miz:
    list_records = []
    pages = state['pages']
    for i in range(pages):
        page = requests.get(link.format(state['code']+str('' if(i==0) else i)))
        soup = BeautifulSoup(page.content,'html.parser')
        data_tbody = soup.find("tbody", id="ElectionResult")
        for div in data_tbody.find_all("div", {'class':'tooltip'}):
            div.decompose()
        for span in data_tbody.find_all("span"):
            span.decompose()
        def get_first_child(soup_page, child):
            first_child = soup_page.find(child)
            all_child = [first_child] + first_child.find_next_siblings(child)
            return all_child
        all_trs = get_first_child(data_tbody, 'tr')
        imp_trs = all_trs[4:]
        for tr in imp_trs:
            all_tds = get_first_child(tr, 'td')
            constituency_dict = {
                        'State': state['name'], 'Constituency':all_tds[0].getText(),
                        'Const.No.': int(all_tds[1].getText()), 'Winner':all_tds[2].getText(),
                        'Winner_Party': all_tds[3].getText(), 'Loser':all_tds[4].getText(),
                        'Loser_Party': all_tds[5].getText(), 'Margin': int(all_tds[6].getText()),
                        'Previous_Winner':all_tds[8].getText(), 'Previous_Winner_Party': all_tds[9].getText(),
                        'Previous_Margin': int(all_tds[10].getText() if(all_tds[10].getText()!='') else 0)
                    }
            # print(constituency_dict)
            list_records.append(constituency_dict)
dataframe = pd.DataFrame(list_records)
dataframe.to_csv("trends_Mizoram.csv")

for state in rajas:
    list_records = []
    pages = state['pages']
    for i in range(pages):
        page = requests.get(link.format(state['code']+str('' if(i==0) else i)))
        soup = BeautifulSoup(page.content,'html.parser')
        data_tbody = soup.find("tbody", id="ElectionResult")
        for div in data_tbody.find_all("div", {'class':'tooltip'}):
            div.decompose()
        for span in data_tbody.find_all("span"):
            span.decompose()
        def get_first_child(soup_page, child):
            first_child = soup_page.find(child)
            all_child = [first_child] + first_child.find_next_siblings(child)
            return all_child
        all_trs = get_first_child(data_tbody, 'tr')
        imp_trs = all_trs[4:]
        for tr in imp_trs:
            all_tds = get_first_child(tr, 'td')
            constituency_dict = {
                        'State': state['name'], 'Constituency':all_tds[0].getText(),
                        'Const.No.': int(all_tds[1].getText()), 'Winner':all_tds[2].getText(),
                        'Winner_Party': all_tds[3].getText(), 'Loser':all_tds[4].getText(),
                        'Loser_Party': all_tds[5].getText(), 'Margin': int(all_tds[6].getText()),
                        'Previous_Winner':all_tds[8].getText(), 'Previous_Winner_Party': all_tds[9].getText(),
                        'Previous_Margin': int(all_tds[10].getText() if(all_tds[10].getText()!='') else 0)
                    }
            # print(constituency_dict)
            list_records.append(constituency_dict)
dataframe = pd.DataFrame(list_records)
dataframe.to_csv("trends_Rajasthan.csv")

for state in telan:
    list_records = []
    pages = state['pages']
    for i in range(pages):
        page = requests.get(link.format(state['code']+str('' if(i==0) else i)))
        soup = BeautifulSoup(page.content,'html.parser')
        data_tbody = soup.find("tbody", id="ElectionResult")
        for div in data_tbody.find_all("div", {'class':'tooltip'}):
            div.decompose()
        for span in data_tbody.find_all("span"):
            span.decompose()
        def get_first_child(soup_page, child):
            first_child = soup_page.find(child)
            all_child = [first_child] + first_child.find_next_siblings(child)
            return all_child
        all_trs = get_first_child(data_tbody, 'tr')
        imp_trs = all_trs[4:]
        for tr in imp_trs:
            all_tds = get_first_child(tr, 'td')
            constituency_dict = {
                        'State': state['name'], 'Constituency':all_tds[0].getText(),
                        'Const.No.': int(all_tds[1].getText()), 'Winner':all_tds[2].getText(),
                        'Winner_Party': all_tds[3].getText(), 'Loser':all_tds[4].getText(),
                        'Loser_Party': all_tds[5].getText(), 'Margin': int(all_tds[6].getText()),
                        'Previous_Winner':all_tds[8].getText(), 'Previous_Winner_Party': all_tds[9].getText(),
                        'Previous_Margin': int(all_tds[10].getText() if(all_tds[10].getText()!='') else 0)
                    }
            # print(constituency_dict)
            list_records.append(constituency_dict)
dataframe = pd.DataFrame(list_records)
dataframe.to_csv("trends_Telangana.csv")


