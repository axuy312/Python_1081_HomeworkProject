import tkinter as tk
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import webbrowser
import time

def findKm(url):
    time.sleep(0.1)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    scr = str(soup.find_all('script'))
    line = scr.split('\n')
    for i in range(0, len(line)):
        if line[i].find("公里") != -1: 
            lineResult = line[i]
    find = lineResult.split('\\\"')
    for i in range(0, len(find)):
        if find[i].find("公里") != -1:
            finalFind = find[i].split(" ")
            break;
    return float(finalFind[0].replace(',', ''))

def run():
    global KmResult
    global urlResult
    KmResult = 0.0
    urlResult = ''
    middleResult = middleEnter.get(1.0, tk.END)
    result = middleResult.split('\n')
    leng = len(result) - 1
    sort(result, 0, leng)

global KmResult
KmResult = 0.0

global urlResult
urlResult = ''

def sort(result, k, leng):
    global KmResult
    global urlResult
    global openUrl
    endResult = endEnter.get()
    startResult = startEnter.get()
    url = URL
    if k == leng:
        temp = url + startResult + "/"
        url = temp
        for i in range(0, leng):
            temp = url + str(result[i]) + "/"
            url = temp
        temp = url + endResult + "/"
        url = temp
        print('URL: ' + url)
        print(str(findKm(url)) + ' KM')
        if float(KmResult) == 0:
            KmResult = findKm(url)
            urlResult = url
            var.set(str(KmResult) + " KM")
            var1.set(str(urlResult).replace(URL, ''))
            openUrl = url
            
        elif float(KmResult) > 0 :
            if compare(KmResult, findKm(url)):
                KmResult = findKm(url)
                urlResult = url
                var.set(str(KmResult) + " KM")
                var1.set(str(urlResult).replace(URL, ''))
                openUrl = url
                
    else:
        for i in range(k, leng):
            swap(result, i, k)
            sort(result, k + 1, leng)
            swap(result, i, k)

def swap(result, i, k):
    a = result[i]
    result[i] = result[k]
    result[k] = a    

def compare(result, x):
    if (result >= x):
        return True
    elif (result < x):
        return False

def openMap():
    webbrowser.open(openUrl, new=0, autoraise=True)
    
          
#視窗
window = tk.Tk() 
window.title('很廢的找路徑')
window.geometry('400x800')

#URL
openUrl = 'https://www.google.com/maps/dir/'
URL = 'https://www.google.com/maps/dir/'
finalresult = ''

#起點
start = tk.Label(window, text = "起點: ", font = ('Arial',18))
startEnter = tk.Entry(window, font = ('Arial',18))


#終點
end = tk.Label(window, text = "終點: ", font = ('Arial',18))
endEnter = tk.Entry(window, font = ('Arial',18))


#中繼站
middle = tk.Label(window, text = "中繼站: ", font = ('Arial',18))
middleEnter= tk.Text(window, font = ('Arial',18),width = 30, height = 15)

#按鈕
#開始
enterButton = tk.Button(window, text = "開始", width = 15, height = 2, command = run)
#開地圖
openButton = tk.Button(window, text = "開啟MAP", width = 15, height = 2, command = openMap)


#里程結果
var = tk.StringVar()
r = tk.Label(window, textvariable = var, font = ('Arial',18))

#路徑結果
var1 = tk.StringVar()
rou = tk.Label(window, textvariable = var1, font = ('Arial',18))

#排版
start.grid(row =1,column=1)
startEnter.grid(row =1,column=2)
end.grid(row =2,column=1)
endEnter.grid(row =2,column=2)
middle.grid(row =3,column=1)
middleEnter.grid(row =4,column=1, columnspan=2)
enterButton.grid(row=5, column=1)
r.grid(row=5, column=2)
openButton.grid(row=6, column=1)
rou.grid(row=6, column=2)

window.mainloop()

