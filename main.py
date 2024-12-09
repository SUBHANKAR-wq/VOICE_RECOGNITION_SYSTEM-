import speech_recognition as sr
import webbrowser
import pyttsx3
from youtubesearchpython import VideosSearch# this module is for searching video in yt
import wikipedia
import wikipediaapi # it gives wikipedia access
import datetime #to know am or pm
import pyjokes # gives joke
import newsfile
import generalgsp as gp


recognisor=sr.Recognizer()
engine=pyttsx3.init()
engine. setProperty('rate', 150)#it manage the speed of the text while the system is speaking

# speak functn
def speak(text):
    engine.say(text)
    engine.runAndWait()
#----------------------------------------COMMANDS GIVEN BY THE USER----------------------------------------------------
def  processcommand(c):
    


    if "how can you help" in c.lower():
        speak("i can help in you in your day to day activities like google search, opening applications , giving you other informations")
        speak("i can play jokes,play songs ,i can do roleplay and many more.")
        speak("do you want to listen my philosophy?")
        with sr.Microphone() as source:
            print("listening...")
            audio=r.listen(source)
            reply=r.recognize_google(audio)

        if reply:
            p=["let me make your day with gita's philosophies ","Dharma,Your Duty,Understand your role in life and fulfill it with dedication and integrity","Karma Yoga, Action in DevotionPerform your actions without attachment to the results","Bhakti Yoga, Devotion,Cultivate a deep connection with the Divine through love and surrender","Jnana Yoga,Knowledge,Seek wisdom and understanding through knowledge and contemplation","The Nature of the Soul,The soul is eternal, indestructible, and beyond the reach of birth and death","Mind Control,The mind is a powerful tool, but it can also be a source of suffering.","hope it will work , thankyou"]
            for i in range (0,8):
                speak(p[i])
    
    elif  c.lower().endswith("jokes"):
        print("listening....")
        jokes=pyjokes.get_joke()
        speak(jokes)

    elif c.lower().endswith("news"):
        x=c.lower().split(" ")[-1]
        speak(newsfile.hdln[x])

    elif "do a play" in c.lower():
        speak("i can be your job recruiter, so let us start")
        data=["How are you doing?","Could you please introduce yourself and give me a brief overview of your background?","Can you tell me more about the internships?","What was the most challenging project you worked on,"," That sounds like a valuable learning experience , What are the problems you have faced","What programming languages and tools are you most comfortable with?"," let you are a team leader , How will you handle any conflicts or differences in any opinion ?","How do you stay updated with the latest trends and technologies in computer science?"," Finally, why are you interested in this position, and what do you hope to achieve if you are hired?","let me think about you, thankyou","yes"]
        speak(data[0])
        j=0
        while data[j]!="let me think about you, thankyou":
            with sr.Microphone() as source:
                print("listening...")
                audio=r.listen(source)
                reply=r.recognize_google(audio)
                
            if reply:# thare reply re eta true heijauchi
                for i in range (1,11):
                    if reply:
                        speak(data[i])
                        with sr.Microphone() as source:
                            print("listening...")
                            audio=r.listen(source)
                            reply=r.recognize_google(audio)
                        print(reply)
                        
            j=j+1


    elif "open google" in c.lower():
        speak("do you want to search")
        with sr.Microphone() as source:
            print("listening...")
            audio=r.listen(source)
            reply=r.recognize_google(audio)  
       
        if(reply.lower()=="yes i want"):
            speak("please ask" )
            with sr.Microphone() as source:
                print("listening to ur query...")
                audio=r.listen(source)
                try:
                    cmd=r.recognize_google(audio) 
                    speak("searching for results")
                    url='https://www.google.co.in/search?q='
                    search=url+cmd
                    webbrowser.open(search)
                except:
                    print("can't recognize")
        else:
             webbrowser.open("https://google.com")


       
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    
    elif c.lower().startswith("play"):
        if "play a song" in c.lower():
            speak("which song do you want to play")
            with sr.Microphone() as source:
                print("listening...")
                audio=r.listen(source)
            query=r.recognize_google(audio)
            speak("recognizing your desired song...") 
        
            videos_search = VideosSearch(query, limit = 1) #this func search vdo in yt API='APPLIN PROGRAMING INTERFACE
            result = videos_search.result()
            url = result['result'][0]['link']
        
            webbrowser.open(url)
        else:
            with sr.Microphone() as source:
                print("listening...")
                audio=r.listen(source)
            query=r.recognize_google(audio)
            speak("recognizing the song...") 
        
            videos_search = VideosSearch(query, limit = 1) #this func search vdo in yt API='APPLIN PROGRAMING INTERFACE
            result = videos_search.result()
            url = result['result'][0]['link']
        
            webbrowser.open(url)
       
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")

    else:
        
        if "how are you" in c.lower() :
            data=["Everything's going great! Thanks for asking. How about you?","How's your day been?"," I understand. What kind of work do you do?","That sounds exciting! how is your family doing","what about your health?","are planning for picnics?","you should go for outing for refreshment and what is your favorite song?","what is your favorite movie?","do you know who is my maker?","i am done thankyou sir"]# if asked how are u
            speak(data[0])
            j=0
            while data[j]!="i am done thankyou sir":
                with sr.Microphone() as source:
                    print("listening...")
                    audio=r.listen(source)
                    reply=r.recognize_google(audio)
                
                if reply:
                    for i in range (1,11):
                        if reply:
                            speak(data[i])
                            with sr.Microphone() as source:
                                print("listening...")
                                audio=r.listen(source)
                                reply=r.recognize_google(audio)
                            print(reply)
                j=j+1
        else:
            with sr.Microphone() as source:
                etc=r.listen(source)
                try:
                    speak("getting some results")
                    cmd=r.recognize_google(etc) 
                    wiki_wiki = wikipediaapi.Wikipedia('english')
                    page = wiki_wiki.page(cmd)

                    if page.exists():
                        print(f"Title: {page.title}")
                        speak(f"Summary: {page.summary[:250]}")  # Print the first 500 characters of the summary
                    else:
                        speak("searching for results")
                        url="https://www.google.co.in/search?q="
                        search=url+cmd
                        webbrowser.open(search)
                except:
                    print("can't recognize")
        

        


   





#-----------------------------------------------------------------------------------------------------------------------
#---------------------SYSTEM WILL RECOGNIZE THE WAKE WORD AND THEN IT WILL TAKE COMMAND--------------------------------     
if __name__=="__main__":
    
    current_hour = datetime.datetime.now().hour#WILL GIVE CURENT HOUR SO THAT IT CAN GREET
    
    if 5 <= current_hour < 12:
        speak("good morning, its chintu here")
    elif 12 <= current_hour < 18:
        speak("good afternoon, its chintu here")
    else:
         speak("good evening, its chintu here")
   
    print("\nYOU HAVE TO SAY HEY CHINTU TO WAKE HIM...\n")
    
    while True:
        #listen to wake word CHINTU
        #obtain audio
        r=sr.Recognizer()
        
        print("recognizing...")

        try:
          
            with sr.Microphone() as source:
                print("listening...")
                audio=r.listen(source, timeout=2,phrase_time_limit=1) #system will recieve audio from user
            word=r.recognize_google(audio)  #this is for waking the system with word chintu      
            
            if(word.lower()==("hey chintu"or"chintu"or "hi chintu"or"hello chintu")):#if the wake word is  then it will take other command
                speak("how can i help")
                #listen for command
                with sr.Microphone() as source:
                    print("chintu is active....")
                    print("speak....")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processcommand(command)


        except Exception as e:
            print("error;{0}".format(e))

#--------------------------------RECOGNITION BLOCK----------------------------------------------------------------------      




























