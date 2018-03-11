import urllib.request              #import packages
from tkinter import *
from bs4 import BeautifulSoup
#=============GUI FORM==================

root=Tk()
root.geometry("1200x1200")
root.title("Current Weather")

TopFrame=Frame(root,width=1350,height=10,bd=14,relief='raise')
TopFrame.pack(side=TOP)

BottomFrame=Frame(root,width=350,height=50,bd=14,relief='raise')
BottomFrame.pack(side=BOTTOM)
LeftMidFrame=Frame(root,width=1350,height=1150,bd=14,relief="raise")
LeftMidFrame.pack(side=LEFT)


#======================TEXT FIELDS AND LEBLES===================
global city,weather;

city=StringVar()
weather=StringVar()
Title=Label(TopFrame,font=('arial',24,'bold'),text="Check the current temperature",bd=10,width=45,justify='center')
Title.grid(row=1,column=1)

enter=Label(LeftMidFrame,font=('arial',18,'bold'),text="Enter the name of a proper city in India :",bd=1,width=80,justify='left')
enter.grid(row=0,column=0)

cityname=Entry(LeftMidFrame,font=('arial',14,'bold'),textvariable=city,bd=10,width=30,relief="sunken")
cityname.grid(row=1,column=0)
output=Label(LeftMidFrame,font=('arial',14,'bold'),textvariable=weather,bd=10,width=50,relief="sunken")
output.grid(row=2,column=0)

#============function of button=============


def set_val():
    city=cityname.get()
    print(city)
    quote_page = "https://www.timeanddate.com/weather/india/"+city
    page = urllib.request.urlopen(quote_page)
    soup = BeautifulSoup(page, "html.parser")                                    #====scraping=======#
    name_box = soup.find("header",{'class':'fixed'})
    name = name_box.text.strip()
    temp_box = soup.find("div",{'class':'h2'})
    temp = temp_box.text.strip()
    outlook = soup.find("p")
    out = outlook.text.strip()
    time = soup.find("span",{'id':'wtct'})
    ti= time.text.strip()
    total=name+"\n"+"temperature :"+temp+"\n"+"Outlook :"+out+"\n"+"current date and time :"+ti
    print(total)
    weather.set(total)                                                                #---set value to the text field



btn=Button(BottomFrame,font=('arial',18,'bold'),text='Submit',bd=2,command=set_val)
btn.grid(row=1,column=0)
