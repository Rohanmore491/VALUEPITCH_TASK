import requests
from bs4 import BeautifulSoup
import csv
# import pandas as pd
headers ={'User-Agent':'Mozilla/5.0','Referer': 'https://main.sci.gov.in/case-status'}

captcha_url ='https://main.sci.gov.in/php/captcha_num.php'
r = requests.get(captcha_url)
cap=r.text
# print(cap)
file='data.csv'

with open(file,'a',newline='') as f:
    writer = csv.DictWriter(f, fieldnames =['Diary No.','Case No.' ,'Present/Last Listed On','Status/Stage','Disp.Type','Category','Act','Petitioner(s)','Respondent(s)','Pet. Advocate(s)','Resp. Advocate(s)','U/Section'])
    writer.writeheader()

for Dnum in range(1,11):
    for Dyr in range(2000,2021):
        CaseDiaryNumber = {
        "d_no": Dnum,
        "d_yr":Dyr,
        "ansCaptcha":cap
        }

        url = 'https://main.sci.gov.in/php/case_status/case_status_process.php'

        number =requests.post(url,data=CaseDiaryNumber,headers=headers)
        soup  = BeautifulSoup(number.content,'lxml')

        tables =soup.find('table')
        td = tables.find_all('td')
        tdata=[]
        for j in range(len(td)):
            if j%2 !=0:
                tdata.append(td[j].text.strip())
        
        with open(file, 'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(tdata)







