url = "https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/"
from bs4 import BeautifulSoup
import re
import csv
import json
import requests
start = 1100693
end = 1100700

headers = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0',
          'cookie': 'G_ENABLED_IDPS=google; fpsend=149436; __zi=3000.SSZzejyD3CiaW_sbrKeErsE1gRkRH1QKFvEZf8a6188lrRBZnmC5ncNTjkp33K_1Ojp-xCSEJyPatFlg.1',
    }
       

out_file = open("test1.json", "a+", encoding = 'utf8') 
#Số lượng thí sinh từng tỉnh từ mã 01 - 64 (Hà nội,HCM....,Bắc Kạn)
soluongs = [100691, 86259, 23241, 12631, 5603, 4738, 3563, 7331, 8680, 9530, 2893, 14840, 8088, 11384, 16151, 13902, 16367, 17923, 16336, 22263, 12338, 9478, 9670, 20917, 22858, 11050, 40041, 34327, 17268, 11902, 8485, 13291, 16701, 11493, 4631, 15308, 13937, 9497, 19767, 13847, 14169, 10362, 12999, 5972, 9644, 12036, 30366, 16353, 10258, 11716, 12959, 16202, 13700, 12113, 13178, 11327, 8806, 9625, 6332, 10914, 6268, 6679, 6815]
matinhs  = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64']
for matinh in matinhs:
    for sbds in soluongs:
        for stt in range(1,100691):
            sbd = matinh + '0'*(6-len(str(stt))) + str(stt)
            url_page = url +str(sbd)+ ".json"
            response = requests.request("GET", url_page, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            data = str(soup)
            try:
                todic = json.loads(data)
                json.dump(todic, out_file,ensure_ascii = False, indent = 4, sort_keys = True)
            except:
                print("No")
            print("Done thi sinh: ",sbd)
            print("--------------")
