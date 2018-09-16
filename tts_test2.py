

from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    username='c7f77f05-d0d0-4b9c-8344-487b4e3a9d81',
    password='ma1M8GmcFKZn')

#print(json.dumps(text_to_speech.list_voices(), indent=2))

with open(join(dirname(__file__), 'output.wav'),'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize('Hello world!', accept='audio/wav',
                                  voice="en-US_AllisonVoice").content)

os.system("aplay oupput.wav")

#print(json.dumps(text_to_speech.get_pronunciation('Watson', format='spr'), indent=2))

#print(json.dumps(text_to_speech.list_voice_models(), indent=2))
