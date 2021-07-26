url = "https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/"
from bs4 import BeautifulSoup
import re
import csv
import requests
start = 1000001
end = 3508718
#3508718
headers = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0',
          'cookie': 'G_ENABLED_IDPS=google; fpsend=149436; __zi=3000.SSZzejyD3CiaW_sbrKeErsE1gRkRH1QKFvEZf8a6188lrRBZnmC5ncNTjkp33K_1Ojp-xCSEJyPatFlg.1',
    }
        
#raw_data = []
file = open("raw_data2021.txt", mode = "w", encoding ="utf8")
for sbd in range(start,end+1):
    url_page = url +"0"+ str(sbd)+ ".json"
    print(url_page)
    response = requests.request("GET", url_page, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
	#raw_data.append(soup)
    file.write(str(soup) + "\n")

