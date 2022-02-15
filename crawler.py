from bs4 import BeautifulSoup
import re
import ssl
from urllib.request import Request, urlopen
import csv  



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Retrieving the page
for i in range(2018,2021):
    year = str(i)
    
    for j in range(1,13):
        month = str(j)
        if j < 10:
            month = '0' + str(j)

        for k in range(1,32):
            day = str(k)
            if k < 10:
                day = '0' + str(k)

            url="https://www.noticiasagricolas.com.br/cotacoes/cafe/cafe-arabica-mercado-fisico-tipo-6-duro/" + year + "-" + month + "-" + day
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

            try:
                web_byte = urlopen(req).read()

            except:
                print("Page not found: " + url)
                continue
            webpage = web_byte.decode('utf-8')

            soup = BeautifulSoup(webpage, "html.parser")
            table = soup.find('table', {'class': 'cot-fisicas'})
            if(table is None):
                continue
            table = table.findAll('tr')
            i = 0
            for row in table:
                if(i == 0):
                    i += 1
                    continue
                row = row.text
                row = row.split('\n')
                data = [year,month,day,row[1], row[2], row[3]]
                print("Retrieving data from: " + url)
                with open('cotacoes.csv', 'a', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
                f.close()








