from tkinter import *
import requests
import json

root = Tk()
root.title('appliances controller')
root.geometry("350x300")

device_list = {
    "light" : "<your device id>" ,
    "nightlight" : "<your device id>",
    "airconditioner" : "<your device id>"
}

def button_click(type = '', device = ''):
    def inner():
        url = "https://api.switch-bot.com/v1.0/devices/" + device_list[device] + "/commands"
        headers = {
            "Content-Type" : "application/json; charset: utf8",
            "Authorization": "<your authorization header>"
        }
        data = {
            "command": type,
            "parameter": "default",
            "commandType": "command"
        }
        json_data = json.dumps(data).encode("utf-8")
        response = requests.post(url, data=json_data, headers=headers)
        if response.status_code != 200:
            print("POST ERROR")
    return inner

#ボタン
Button1 = Button(text=u'電気をつける', command=button_click("turnOn", "light"))
Button1.grid(row=1, column=1, padx=20, pady=20)

Button2 = Button(text=u'常夜灯をつける', command=button_click("turnOn", "nightlight"))
Button2.grid(row=1, column=2, padx=20, pady=20)

Button3 = Button(text=u'電気を消す', command=button_click("turnOff", "light"))
Button3.grid(row=1, column=3, padx=20, pady=20)

Button4 = Button(text=u'エアコンをつける', command=button_click("turnOn", "airconditioner"))
Button4.grid(row=2, column=1, padx=20, pady=20)

Button5 = Button(text=u'エアコンを消す', command=button_click("turnOff", "airconditioner"))
Button5.grid(row=2, column=2, padx=20, pady=20)

root.mainloop()
