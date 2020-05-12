#you will need the following library
#First we import SpeechToTextV1 from ibm_watson.For more information on the API,
from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import wget as wg
#The service endpoint is based on the location of the service instance, we store the information in the variable URL. 
# To find out which URL to use, view the service credentials.
url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ad1503f8-bcd4-4607-9602-31e5ef4f300d"
#You require an API key, and you can obtain the key 
iam_apikey_s2t = "2a5pItIM96XXDpiSTTP0AnnDY9ei6HAw3fSNVE6bi7iu"
#You create a Speech To Text Adapter object the parameters are the endpoint and API key.
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
print(s2t)
#Lets download the audio file that we will use to convert into text.
#url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/PolynomialRegressionandPipelines.mp3"
#We have the path of the wav file we would like to convert to text
#wg.download(url, 'G:\PIAIC\PIAIC AI COURSE\Quarter 1\Classes\Quarter 1\Python\A.I\PolynomialRegressionandPipelines.mp3')
filename='G:\PIAIC\PIAIC AI COURSE\Quarter 1\Classes\Quarter 1\Python\A.I\PolynomialRegressionandPipelines.mp3'
#We create the file object wav with the wav file using open ; 
# we set the mode to "rb" , 
# this is similar to read mode, but it ensures the file is in binary mode.
# We use the method recognize to return the recognized text. The parameter audio is the file object wav, 
# the parameter content_type is the format of the audio file.
with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
#The attribute result contains a dictionary that includes the translation:
#print(response.result)
from pandas.io.json import json_normalize
print(json_normalize(response.result['results'],"alternatives"))
print(response)
#We can obtain the recognized text and assign it to the variable recognized_text
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
#print(type(recognized_text))
print(recognized_text)