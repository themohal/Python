#install library by typing command in cmd or terminal: pip install gTTS
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 

  
# The text that you want to convert to audio 
mytext = 'خوش آمدیدفرجاد،میں آرٹیفیشل انٹیلی جنس ہوں'
  
# Language in which you want to convert 
language = 'ur'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
current_path=os.path.dirname(os.path.abspath(__file__))
myobj.save(current_path+"\welcome_urdu.mp3") 
# Playing the converted file 
os.startfile(current_path+"\welcome_urdu.mp3")