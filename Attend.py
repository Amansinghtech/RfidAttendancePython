from os import truncate
from flask import Flask, json
from datetime import date, datetime

app = Flask(__name__)

filename = "Attendence.json"

users = [
    {
    "name":"Deepak Yadu",
    "UID":"138213210128",
    "emailID":"deepak@oceanparrot.com",
    "entry": ""
    },
    {
    "name":"Aman Singh",
    "UID":"10224920441",
    "emailID":"aman@oceanparrot.com",
    "entry": ""
    }
]

devices =['dev101', 'dev102', 'dev103', '1fc7f0bcf657e828']


def checkUserTime(user):
    if user['entry'] == "":
        user['entry'] = datetime.now()
    else: 
        if (datetime.now() - user['entry']).total_seconds() >= 60:
            return False 
        else:
            return True

@app.route('/')
def main():
    return "Connected! Hurray"

@app.route('/entry/<string:UID>/<string:DeviceID>', methods=['GET', 'POST'])
def entry(UID, DeviceID): 
    print(UID, DeviceID)  
    if DeviceID in devices :
        for user in users:
            if user['UID'] == UID:
                stayed = checkUserTime(user)
                if stayed:
                    with open(filename, 'a') as file:
                        now = datetime.now()
                        data = { 
                            "Time": now.strftime("%d/%m/%Y %H:%M:%S"),
                            "Name": user['name'],
                            "Email": user['emailID'],
                            "UID" : user['UID']
                        }
                        json.dump(data, file)
                        file.write('\n')
                        file.close()
                        "Nikal BSDK"
                    return "Attendance Added"
                else: 
                    print("Ruk ja kya jaldi h")
        else:
            return "Invalid UID detected"
    else:
          return "Invalid Device ID"

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=4444)