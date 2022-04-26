from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="url")
parser.add_argument('-w', "--write-file" , help="file")
parser.add_argument('-f','--farmsparse',help='parses the modernfarmer site for new urls',action='store_true')
args = parser.parse_args()
print( "URL {} ".format(
        args.url
        ))

url = args.url
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





try:

    with open(args.write_file,'w') as f:

            if args.farmsparse == True:
                stateLnk = soup.find_all("li",{"class": "csa_record"})
                farmDict = dict()

                for list in stateLnk:
                    for line in list:

                        form = str('|- Name of Farm -|' + line.get_text()  + '|- Link -| ' + line.get('href')  + '|')
                        print(form)
                        f.write(form)
                        #print('|- Name of Farm -|',line.get_text() ,'|- Link -| ',line.get('href') , '|')
                        farmDict[line.get_text()] = line.get('href')
                        f.write('\n\n')


except:

    print(soup.prettify())

finally:

    from time import sleep
    import sys
    import progressbar

    bar = progressbar.ProgressBar(maxval=20, \
        widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    for i in range(20):
        bar.update(i+1)
        sleep(0.02)
    bar.finish()
    print('\tParser Complete',end='')

#this one works to parse sites
