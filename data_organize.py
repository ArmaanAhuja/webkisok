import json
import os
# import module
from bs4 import BeautifulSoup

list_ =  [] 

for path in os.listdir('./extract'):

    info = ''
    with open("./extract/" + path + "/personal_info.html") as html:
        # print(html)
        info = info + html.read()
    
    info = info.replace("\\n" , '\n')
    info = info.replace("\\r" , '\r')
    info = info.replace("\\t" , '\t')
    # print(info)
    # parse html content
    soup = BeautifulSoup( info , 'html.parser')
    
    tds = soup.find_all('td')
    td = tds[1]
    name = td.text.strip()

    list_.append({"name": name,"roll_no": path})
    print("Name:" + name + " \n Roll:" + path + "\n\n")




write = open('./extract.json','w+');

write.write(json.dumps(list_))