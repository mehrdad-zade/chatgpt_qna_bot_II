import azure.cognitiveservices.speech as speechsdk
import time
import datetime
from secrets_custom import azure_speech2text_subscription_token, azure_speech2text_region

def azure_speech_to_text(audio_file_path):
    # Set up the speech configuration
    speech_config = speechsdk.SpeechConfig(subscription=azure_speech2text_subscription_token, region=azure_speech2text_region)
    
    # Set up the audio configuration
    audio_config = speechsdk.audio.AudioConfig(filename=audio_file_path)
    
    # Creates a recognizer with the given settings
    speech_config.speech_recognition_language="en-US"
    speech_config.request_word_level_timestamps()
    speech_config.enable_dictation()
    speech_config.output_format = speechsdk.OutputFormat(1)

    # Create a speech recognizer
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    
    '''
    speech to text service stops once there is a pause (or no talk, i.e. background music). 
    below code is to enforce the connection and prevent it from stopping while the audio file 
    hasn't finished yet 
    '''
    all_results = []

    def handle_final_result(evt):
        all_results.append(evt.result.text)    

    done = False

    def stop_cb(evt):
        print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True    

    #Appends the recognized text to the all_results variable. 
    speech_recognizer.recognized.connect(handle_final_result) 

    #Connect callbacks to the events fired by the speech recognizer & displays the info/status
    #Ref:https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-speech/azure.cognitiveservices.speech.eventsignal?view=azure-python   
    speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    speech_recognizer.start_continuous_recognition()

    while not done:
        time.sleep(.5)
        
    print("Printing all results:")
    print(all_results)    
    with open("source_of_knowledge/output.txt", "w") as f:
        f.write(', '.join(all_results))

# api call - doesn't work.
# def getText(audio_file_path):

#     # Set the headers
#     headers = {
#         'Ocp-Apim-Subscription-Key': azure_speech2text_subscription_token,
#         'Authorization': 'Bearer ' + getAccessToken(),
#         'Content-Type': 'audio/wav'
#     }

#     params = {
#         'language': 'en-US'
#     }

#     # Read the audio file as binary data
#     # with open(audio_file_path, 'rb') as f:
#     #     audio_data = f.read()
#     audio_data = open(audio_file_path, 'rb')

#     response = requests.post(azure_speech2text_api_endpoint, headers=headers, params=params, data=audio_data)
#     print(response.status_code)  
#     # print(response.json()['DisplayText'])
   
# the sdk doesn't need this.
# def getAccessToken():
#     headers = {
#         'Ocp-Apim-Subscription-Key': azure_speech2text_subscription_token
#     }
#     response = requests.post(azure_speech2text_access_token_endpoint, headers=headers)
#     access_token = str(response.text)
#     return access_token
#     #print('Access token:', access_token)

#print(json.dumps(response.json(), indent=4))    