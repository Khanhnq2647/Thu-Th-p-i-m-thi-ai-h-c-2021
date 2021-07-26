url = "https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/"
from bs4 import BeautifulSoup
import re
import csv
import requests
start = 1000001
end = 1101000
#3508718
headers = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0',
          'cookie': 'G_ENABLED_IDPS=google; fpsend=149436; __zi=3000.SSZzejyD3CiaW_sbrKeErsE1gRkRH1QKFvEZf8a6188lrRBZnmC5ncNTjkp33K_1Ojp-xCSEJyPatFlg.1',
    }
        
file = open("raw_data2021.txt", mode = "a+", encoding ="utf8")

for sbd in range(start,end+1):
    url_page = url +"0"+ str(sbd)+ ".json"
    
    response = requests.request("GET", url_page, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    file.write(str(soup) + "\n")
    print("Done thi sinh: ",sbd)
    print("--------------")

