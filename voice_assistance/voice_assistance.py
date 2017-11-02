#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import speech_recognition as sr

import pyaudio;audio=pyaudio.PyAudio();print([audio.get_device_info_by_index(i) for i in range(audio.get_device_count())])

# Record Audio
r = sr.Recognizer()
with sr.Microphone(device_index=14) as source:
    print("Say something!")
    audio = r.listen(source, timeout=1, phrase_time_limit=10)
    print(audio)

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".
        format(e))

if __name__ == "__main__":
    pass
