from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="url")
args = parser.parse_args()
#print( "URL {} ".format(
#        args.url
#        ))

url = 'https://modernfarmer.com/2020/03/were-compiling-a-list-of-csas-in-all-50-states/'


#spoofs my user agent
req = Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
)
#request page as normal without 403 error
uClient = uReq(req)
soup = BeautifulSoup(uClient.read(),'html.parser')


    #if tag.get('class')[0] == 'grid-10':
    #    print(tag.contents)
#print(soup.find_all('div',class_='grid-10'))
mydivs = soup.find_all("div", {"class": "grid-10"})

stateLnk = soup.find_all("li",{"class": "csa_record"})

#prints list of farms from this list and their associated names
with open('F:\CUDA-Documents\ASU Spring 2021-2022\GHY 3814\Final_Project\\farmLinks.txt','w') as f:


    farmDict = dict()
    for list in stateLnk:
        for line in list:
            form = str('|- Name of Farm -|' + line.get_text()  + '|- Link -| ' + line.get('href')  + '|')
            print(form , type(form))
            f.write(form)
            #print('|- Name of Farm -|',line.get_text() ,'|- Link -| ',line.get('href') , '|')
            farmDict[line.get_text()] = line.get('href')

            f.write('\n\n')


#client = uReq(url)  # grabs the page
#soup = BeautifulSoup(client.read(), 'html.parser')
