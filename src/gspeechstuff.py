from gtts import gTTS
import gtranslate
import subprocess
import speechRecognition as sr
import time
import os
import string


def say(thing, language = ''):
    if language == '':
        language = "en"
    if language != "en":
        thing = gtranslate.translate(thing, language, "en")
    tts = gTTS(text=str(thing), lang=language)
    tts.save("../data/temp/google.mp3")
    if not os.path.exists("../data/temp/google.mp3"):
        print "Something went wrong with Google synthesizing your text"
        return False
    p = subprocess.Popen("PULSE_SINK=null cvlc --play-and-exit ../data/temp/google.mp3", shell=True)
    p.communicate()


def main(lang = ''):
    thing = str(raw_input("Say Something (g" + lang + " to exit): "))
    while thing != str("g" + lang):
        say(thing, lang)
        thing = str(raw_input("Say Something (g" + lang + " to exit): "))


def mainSpeech(lang = ''):
    decision = str(raw_input("Are you sure? (y/n) "))
    while decision == 'y':
        print "Say an English sentence."
        subprocess.Popen("sox -t alsa default ../data/temp/recording.wav silence 1 0.1 5% 1 1.0 5%", shell=True)
        print "*******"
        stop = str(raw_input("Enter 'y' when you've finished with a sentence"))
        print "*******"
        if stop == 'y':
            pid = subprocess.Popen("pkill sox", shell=True)
            pid.communicate()
            yousaid = sr.sRecognizer()
        if yousaid != False:
            say(yousaid, lang)
            decision = str(raw_input("Try it again? (y/n) "))
        elif yousaid == False:
            print "Speech is unintelligible"
            decision = str(raw_input("Try it again? (y/n) "))


def sayAES(ct):
    templist = []
    for element in ct:
        if element in string.ascii_uppercase:
            templist.append(str("Capital " + element))
        else:
            templist.append(element)
    tempct = ','.join(templist)
    tts = gTTS(text="Warning, Warning, Incoming Ciphertext", lang="en")
    tts.save("../data/temp/googlewarning.mp3")
    tts = gTTS(text=str(tempct), lang="en")
    tts.save("../data/temp/googlect.mp3")
    tts = gTTS(text="End of Ciphertext", lang="en")
    tts.save("../data/temp/googleend.mp3")
    if not os.path.exists("../data/temp/googlect.mp3"):
        print "Something went wrong with Google synthesizing your ciphertext"
        return False
    p = subprocess.Popen("PULSE_SINK=null cvlc --play-and-exit ../data/temp/googlewarning.mp3", shell=True)
    p.communicate()
    time.sleep(1)
    p = subprocess.Popen("PULSE_SINK=null cvlc --play-and-exit ../data/temp/googlect.mp3", shell=True)
    p.communicate()
    p = subprocess.Popen("PULSE_SINK=null cvlc --play-and-exit ../data/temp/googleend.mp3", shell=True)
    p.communicate()
