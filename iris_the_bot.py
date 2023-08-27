import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 
import requests
import json
from googlesearch import search
from tkinter import *
converter=pyttsx3.init()
voices=converter.getProperty('voices')
converter.setProperty('rate', 150)
converter.setProperty('volume', 0.7) 
converter.setProperty('voice',voices[1].id)
class robo:
    def __init__(self) -> None:
        self.in_Put=''
        self.out_put=0
    def take_input(self,audio):
        if 'quit' in audio:
            converter.say('good bye  sir thanks for using')
            converter.runAndWait()
            exit()
        elif 'exit' in audio:
            converter.say('good bye  sir thanks for using')
            converter.runAndWait()
            exit()
        elif 'stop' in audio:
            converter.say('good bye  sir thanks for using')
            converter.runAndWait()
            exit()
        elif 'who are you' in audio :
            converter.say('i am irish 2 point o the chat bot')
            converter.runAndWait()
        elif 'what is your name' in audio :
            converter.say('i am irish 2 point o the chat bot')
            converter.runAndWait()
        elif 'yourself' in audio :
            converter.say('i am irish 2 point o the chat bot')
            converter.runAndWait()
        elif 'time now' in audio:
            current_hour=str(datetime.datetime.now().hour)
            current_minute=str(datetime.datetime.now().minute)
            current_second=str(datetime.datetime.now().second)
            time=current_hour+' '+current_minute+"  "
            converter.say(f'the  current time is {time}')
            converter.runAndWait()
            current_hour=int(current_hour)
            current_minute=int(current_minute)
            current_second=int(current_second)
            if(current_hour>=0 and current_hour<=11 and current_minute>=1 and current_minute<=59 and current_second>=0 and current_second<=59):
                converter.say("its morning now")
                converter.runAndWait()
            elif(current_hour>=12 and current_hour<=15 and current_minute>=0 and current_minute<=59 and current_second>=0 and current_second<=59):
                converter.say("its mid day now")
                converter.runAndWait()
            elif(current_hour>=16 and current_hour<=20 and current_minute>=0 and current_minute<=59 and current_second>=0 and current_second<=59):
                converter.say("its evening now")
                converter.runAndWait()
            else:
                converter.say("its night now")
            print(f'the  current time is {time}')            
        elif 'date' in audio:
            current_day=str(datetime.datetime.now().day)
            current_month=str(datetime.datetime.now().month)
            current_year=str(datetime.datetime.now().year)
            date=current_day+" "+current_month+" "+current_year
            datetime_object = datetime.datetime.strptime(current_month, "%m")
            full_month_name = datetime_object.strftime("%B")                
            converter.say(f' to day the date is{full_month_name} {current_day} {current_year}')
            print(f'to day the date is{current_day}-{current_month}-{current_year}')        
            converter.runAndWait()
            date1=str(date)
            day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            day = datetime.datetime.strptime(date1, '%d %m %Y').weekday()
            converter.say(f'{day_name[day]}')
            converter.runAndWait()
            print(day_name[day])
        elif 'day' in audio:
            current_day=str(datetime.datetime.now().day)
            current_month=str(datetime.datetime.now().month)
            current_year=str(datetime.datetime.now().year)
            date=current_day+" "+current_month+" "+current_year
            datetime_object = datetime.datetime.strptime(current_month, "%m")
            full_month_name = datetime_object.strftime("%B")                
            converter.say(f' to day the date is{full_month_name} {current_day} {current_year}')
            print(f'to day the date is{current_day}-{current_month}-{current_year}')        
            converter.runAndWait()
            date1=str(date)
            day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            day = datetime.datetime.strptime(date1, '%d %m %Y').weekday()
            converter.say(f'{day_name[day]}')
            converter.runAndWait()
            print(day_name[day])
        elif 'wikipedia' in audio :
             converter.say('searching wikipedia')
             converter.runAndWait()                             
             result=wikipedia.summary(audio)            
             converter.say(f"according to wikipedia {result}")                                                       
             converter.runAndWait()
        elif 'open google' in audio:
            converter.say('opening google')
            converter.runAndWait()
            webbrowser.open('google.com')
        elif 'open youtube' in audio:
            converter.say('opening youtube')
            converter.runAndWait()
            webbrowser.open('https://www.youtube.com/') 
              
        elif 'open geeks for geeks' in audio:
            converter.say('opening geeks for geeks')
            converter.runAndWait()
            webbrowser.open('geeksforgeeks.com')           
       
        elif 'open stack over flow' in audio:
            converter.say('opening wikipedia')
            converter.runAndWait()
            webbrowser.open('stackoverflow.com')
        elif 'open spotify' in audio:
            webbrowser.open('spotify.com')        
        elif 'open hackerrank' in audio:
            webbrowser.open('https://www.hackerrank.com/dashboard')
        elif 'open nptel' in audio:
            webbrowser.open('https://swayam.gov.in/mycourses')
        elif 'show some picture'in audio:
            webbrowser.open('https://www.pngegg.com/en/search?q=free+download')           
        elif 'pngegg'in audio:
            webbrowser.open('https://www.pngegg.com/en/search?q=free+download')           
        elif 'search'in audio:
            l1=[]
            l1=(str(audio).split(" "))
            l1.remove(l1[0])
            new_audio=''
            for i in l1:
                new_audio=new_audio+" "+i
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                print(j)
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                webbrowser.open(j)
                converter.say('there are some results')
                converter.runAndWait()
                break           
        elif 'picture' in audio:
            l1=[]
            l1=(str(audio).split(" "))
            l1.remove(l1[0])
            new_audio=''
            for i in l1:
                new_audio=new_audio+" "+i
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                print(j)
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                webbrowser.open(j)
                converter.say('there are some results')
                converter.runAndWait()
                break           
        elif 'photo' in audio:
            l1=[]
            l1=(str(audio).split(" "))
            l1.remove(l1[0])
            new_audio=''
            for i in l1:
                new_audio=new_audio+" "+i
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                print(j)
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                webbrowser.open(j)
                converter.say('there are some results')
                converter.runAndWait()
                break   
        elif 'show' in audio:
            l1=[]
            l1=(str(audio).split(" "))
            l1.remove(l1[0])
            new_audio=''
            for i in l1:
                new_audio=new_audio+" "+i
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                print(j)
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                webbrowser.open(j)
                converter.say('there are some results')
                converter.runAndWait()
                break  
        elif 'open' in audio:
            l1=[]
            l1=(str(audio).split(" "))
            l1.remove(l1[0])
            new_audio=''
            for i in l1:
                new_audio=new_audio+" "+i
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                print(j)
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                webbrowser.open(j)
                converter.say('there are some results')
                converter.runAndWait()
                break
        elif 'visit' in audio:
            l1=[]
            l1=(str(audio).split(" "))
            l1.remove(l1[0])
            new_audio=''
            for i in l1:
                new_audio=new_audio+" "+i
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                print(j)
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                webbrowser.open(j)
                converter.say('there are some results')
                converter.runAndWait()
                break                                       
        
        elif 'play' in audio:
            l1=[]
            l1=(str(audio).split(" "))
            l1.remove(l1[0])
            new_audio=''
            for i in l1:
                new_audio=new_audio+" "+i
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                print(j)
            for j in search(new_audio, tld="co.in", num=10, stop=10, pause=2):
                webbrowser.open(j)
                converter.say('there are some results')
                converter.runAndWait()
                break 
        elif 'sing' and 'song' in audio:
            if 'hindi' in audio:
                converter.say('Humein toh loot liya milke  Ishq walon ne , Bahut hi tang kiya ab tak Inn khayalon ne , Nasha chadha jo shareefi ka Utaar phenka hai , Besharam rang kahan dekha Duniya walon ne')
                print("Humein toh loot liya milke\nIshq walon ne\nBahut hi tang kiya ab tak\nInn khayalon ne\nNasha chadha jo\nshareefi ka Utaar phenka hai\nBesharam rang kahan dekha Duniya walon ne...\n--By Iris")
                converter.runAndWait()
            elif 'english' in audio:
                converter.say('My patience is waning is,this entertaining,Our patience is waning is,this entertaining,I got this feeling,yeah you know,Where im losing,all control,cause theres magic,in my bones,')                
                print('My patience is waning is,this entertaining\nOur patience is waning is\nthis entertaining,I got this feeling,yeah you know,Where im losing,all control,cause theres magic\nin my bones\n--By Iris')              
                converter.runAndWait()
            elif 'bengali' in audio:
                converter.say('Tomar namer ruddure,Ami dubechi somuddure,Jani na jabo kot-dure ekhono,Amar pura kopale,Ar amar shondhe shokale,Tumi keno ele jani na ekhono,Fondi aate mon palabar,Bondhi ache kache se tomar\nJodi sotti jante chao,Tomake chai tomake chai,Jodi mitthe mante chao,Tomakei chai')                
                print('Tomar namer ruddure\nAmi dubechi somuddure\nJani na jabo kot-dure ekhono\nAmar pura kopale\nAr amar shondhe shokale\nTumi keno ele jani na ekhono\nFondi aate mon palabar\nBondhi ache kache se tomar\nJodi sotti jante chao\nTomake chai tomake chai\nJodi mitthe mante chao\nomakei chai\n--By Iris')
                converter.runAndWait()
            elif 'tamil' in audio:
                converter.say('Appadi Podu Podu Podu,Asathi Podu Kannalae,Ipdi Podu Podu Podu,Izhuthu Podu Kaiyaalae')                
                print('Appadi Podu Podu Podu\nAsathi Podu Kannalae\nIpdi Podu Podu Podu\nIzhuthu Podu Kaiyaalae')              
                converter.runAndWait()
            else:
                converter.say('sorry,ask your friend for sing this song')
                print("sorry,failed to sing....")
                converter.runAndWait()



              
        
                
    def wish_me(self):
            hour=int(datetime.datetime.now().hour)
            min=int(datetime.datetime.now().minute)
            sec=int(datetime.datetime.now().second)
            if(hour>=0 and hour<=11 and min>=1 and min<=59 and sec>=0 and sec<=59):
                converter.say("good morning sir!!")
            elif(hour>=12 and hour<=15 and min>=0 and min<=59 and sec>=0 and sec<=59):
                converter.say("Good Afternoon sir!!")
            elif(hour>=16 and hour<=20 and min>=0 and min<=59 and sec>=0 and sec<=59):
                converter.say("Good Evening sir!!")
            else:
                converter.say("Good evening sir!!")
            converter.say('i am irish')
            converter.say('tell me how can i help you')
            converter.runAndWait()        
    def give_output(self):
        pass
    def take_command(self):
        r = sr.Recognizer()
        mymic = sr.Microphone(device_index=1) 
        with mymic as source:
                print("Say now.....")
                r.adjust_for_ambient_noise(source) 
                audio = r.listen(source) 
               
                try:
                    print("recognizing....")
                    quary=r.recognize_google(audio)
                    print(f"user quary : {quary}\n")
                except:
                    print('say that agin please!!')
                    return 'None'
        return quary
if __name__ == '__main__':
    waiting_key=0    
    obj=robo()
    obj.wish_me()
    while 1:
        if(waiting_key==1):
            waiting_key=int(input())
            converter.say('i am active now')
            converter.runAndWait()      
        audio=obj.take_command().lower()
        if 'wait' in audio:
            waiting_key=1
            converter.say('i am waiting , press zero for active me')
            print("i am waiting , press zero for active me.....")
            converter.runAndWait()                   
        if 'temperature' in audio:
            l=[]
            l.append(audio.split(" "))
            City=l[0]
            city=City[len(City)-1]
            url=f"https://api.weatherapi.com/v1/current.json?key=98da8c08b8614621a9d33754230204&q={city}"
            r=requests.get(url)
            w_dic=json.loads(r.text)
            converter.say(f"tempareture of {city} is {w_dic['current']['temp_c']} degree celsius")
            converter.runAndWait()
        if 'weather' in audio:
            l=[]
            l.append(audio.split(" "))
            City=l[0]
            city=City[len(City)-1]
            url=f"https://api.weatherapi.com/v1/current.json?key=98da8c08b8614621a9d33754230204&q={city}"
            r=requests.get(url)
            w_dic=json.loads(r.text)
            print(f'{city} weather conition')
            print('-------------------------------')
            print(f"tempareture : {w_dic['current']['temp_c']} d_c")
            print(f"cloud : {w_dic['current']['cloud']}%")
            print(f"humidity : {w_dic['current']['humidity']}%")
            print(f"wind_kph : {w_dic['current']['wind_kph']}km/hr")
            print(f"wind_dir : {w_dic['current']['wind_dir']}")
            print(f"pressure_mb : {w_dic['current']['pressure_mb']}mb")
            converter.say(f"tempareture of {city} is {w_dic['current']['temp_c']} degree celsius")
            converter.runAndWait()
            converter.say(f"humidity of {city} is {w_dic['current']['humidity']} %")
            converter.runAndWait()
            converter.say(f"cloud {w_dic['current']['cloud']} %")
            converter.runAndWait()
            humidity=int(w_dic['current']['humidity'])
            tempareture=int(w_dic['current']['temp_c'])
            cloud=int(w_dic['current']['cloud'])
            if humidity<=0 and humidity>30:
                 if tempareture>=39:
                     converter.say("too hot weather carry umbrella,cap,sun glasses when go outside")
                     print("too hot weather carry umbrella,cap,sun glasses when go outside")
                     converter.runAndWait()
                 else:
                     converter.say("no chance of rain")
                     print("no chance of rain")
                     converter.runAndWait()
            elif humidity>=30 and humidity<=70:
                converter.say("normal weather condition for going outside")
                print("normal weather condition for going outside")
                converter.runAndWait()
            elif humidity>70 and humidity<=100:
                converter.say("there will be a chance for rain today carry rain coat or umbrella")
                print("there will be a chance for rain today carry rain coat or umbrella")
                converter.runAndWait()
            elif tempareture<=10:
                converter.say("too cold outside , take protection")
                print("too cold outside , take protection")
                converter.runAndWait()
            else:
                pass
        elif 'news' in audio:
            converter.say("type category of news")
            converter.runAndWait()
            print("type category of news[sports,business,politics,science,\ntechnology,entertainment, health] : ")
            category=str(input())            
            url=f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey=60f2e52c48214ec29271a1f22487ac42"
            news=requests.get(url).json()
            article=news["articles"]
            news_article=[]
            for arti in article:
                news_article.append(arti['title'])
            for i in range(10):
                print(news_article[i])
            for i in range(10):
                converter.say(news_article[i])
                converter.runAndWait()                
        else:
            obj.take_input(audio)
            obj.give_output()

