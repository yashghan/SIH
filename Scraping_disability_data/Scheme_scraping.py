import requests
import bs4
import pandas as pd
States_UT=[]
Disability=[]
Scheme=[]
Benefits=[]
TypeofBenefits=[]
Doc=[]

def scrape():
    for i in range(1,7):
        url="https://www.swavlambancard.gov.in/schemes/search/{}"
        response = requests.get(url.format(i))
        soup = bs4.BeautifulSoup(response.text,'lxml')
        Rows=soup.find_all('tr')
        for i in range(1,len(Rows)):
            States_UT.append(Rows[i].find_all('td')[0].text)
            Disability.append(Rows[i].find_all('td')[1].text.rstrip().lstrip())
            Scheme.append(Rows[i].find_all('td')[2].text)
            Benefits.append(Rows[i].find_all('td')[3].text)
            TypeofBenefits.append(Rows[i].find_all('td')[4].text)
            Doc.append("https://www.swavlambancard.gov.in"+Rows[i].find_all('td')[5].a['href'])
scrape()
schemes_df=pd.DataFrame({"State / UTs Name":States_UT,"Disability Type":Disability,'Scheme Name':Scheme,
                         'Disability Benefits Criteria':Benefits,"Type of Benefits":TypeofBenefits,"Document":Doc}) 
schemes_df.to_excel('Schemes.xlsx')       
    