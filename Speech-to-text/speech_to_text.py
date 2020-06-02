#first install library using command in terminal or cmd:pip install SpeechRecognition
import speech_recognition as sr
from gtts import gTTS 
import os 
import webbrowser
check=0
from playsound import playsound
import winsound
import sys
import re
import vlc
player = vlc.MediaPlayer('G:\PIAIC\PIAIC AI COURSE\Speech-to-text\_serhatdermis.mp4')


# Function to convert text to 
# speech 
def SpeakText(text): 
      # The text that you want to convert to audio 
    mytext = text
    
    # Language in which you want to convert 
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    # Saving the converted audio in a mp3 file named 
    # welcome  
    #current_path=os.path.dirname(os.path.abspath(__file__))
    myobj.save("recognized.mp3") 
    # Playing the converted file 
    os.startfile("recognized.mp3")
    
def RecognizeVoice():
    r = sr.Recognizer()                                                                                   

        # get audio from the microphone                                                                       
    with sr.Microphone() as source:                                                                       
        print("Listening ...")         
        # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
        r.adjust_for_ambient_noise(source, duration=0.2)                                                                           
        audio = r.listen(source)   
        
# Using ggogle to recognize audio 
    try:
        MyText = r.recognize_google(audio) 
        if(MyText!=''):
            MyText = MyText.lower()

    except sr.UnknownValueError:
            RecognizeVoice()

        
        
    try:
        print("You said " + r.recognize_google(audio))
        check=1
       
        if MyText.find("phoenix")>=0 or MyText.find("Phoenix") >=0:
            file= os.path.dirname(os.path.abspath(__file__))
            #os.startfile()
            playsound('G:\PIAIC\PIAIC AI COURSE\Speech-to-text\phoenix.mp3',False)
            RecognizeVoice()
        elif MyText.find('open')>=0 or MyText.find('Open')>=0 and MyText.find("youtube")>=0 or MyText.find('Youtube')>=0:
            webbrowser.open("https://www.youtube.com/")
            playsound('G:\PIAIC\PIAIC AI COURSE\Speech-to-text\open.mp3',False)
            RecognizeVoice()
        elif MyText.endswith("google"):
            webbrowser.open("https://www.google.com.pk/")
            playsound('G:\PIAIC\PIAIC AI COURSE\Speech-to-text\open.mp3',False)
            RecognizeVoice()
        elif MyText.find('search')>=0 or MyText.find('Search')>=0 and MyText.find('youtube')>=0 or MyText.find('Youtube')>=0:
            result = re.search('search(.*)on', MyText)
            print(result.group(1))
            to_search=result.group(1)
            webbrowser.open('https://www.youtube.com/results?search_query='+to_search)
            RecognizeVoice()
        elif MyText.endswith('Bye') or MyText.endswith('bye'):
            playsound("G:\PIAIC\PIAIC AI COURSE\Speech-to-text\slamakhri.mp3")
            sys.exit()
            #SpeakText(MyText)
        elif MyText.find('favorite')>=0 or MyText.find('Favorite')>=0 and MyText.find('song')>=0 or MyText.find('song')>=0 and MyText.find('play')>=0 or MyText.find('Play')>=0:
            #webbrowser.open('https://www.youtube.com/watch?v=65opYxvceP8&start=72&end=208')
            player.play()
            RecognizeVoice()
        elif MyText.find('turn off')>=0 and MyText.find('music'):
            player.stop()
            RecognizeVoice()

        else:
            print('Say again!')
            RecognizeVoice()

    except sr.UnknownValueError as un:
        print("Could not understand audio".format(un))
        RecognizeVoice()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        RecognizeVoice()
    except sr.WaitTimeoutError as wte:
        RecognizeVoice()
      

RecognizeVoice();