from gtts import gTTS
import gtranslate
import subprocess
import speechRecognition as sr
import time
import os
import string


def say(thing, language=''):
    # granslate, translates stuff and tts creates an mp3 which is to be
    # streamed by cvlc.
    if language == '':
        language = "en"
    if language != "en":
        thing = gtranslate.translate(thing, language, "en")
    try:
        tts = gTTS(text=str(thing), lang=language)
    except:
        print "Language Not Supported"
        return False
    tts.save("../data/temp/google.mp3")
    if not os.path.exists("../data/temp/google.mp3"):
        print "Something went wrong with Google synthesizing your text"
        return False
    p = subprocess.Popen(str("PULSE_SINK=null cvlc --no-repeat --no-loop " +
                             "--play-and-exit ../data/temp/google.mp3"),
                         shell=True)
    p.communicate()


def main(lang=''):
    # Front-end that is called from main.py
    thing = str(raw_input("Say Something (g" + lang + " to exit): "))
    while thing != str("g" + lang):
        say(thing, lang)
        thing = str(raw_input("Say Something (g" + lang + " to exit): "))


def mainSpeech(lang=''):
    # For the sake of accuracy, sox records each of your sentence and saves it
    # in temp. speechRecognition then returns a string of the content. That is
    # passed for synthesis to speech. Since sox has to record only one sentence,
    # it needs to be killed at some point. It would be killed if you press 'y'
    # and hit enter by @stop variable. @decision is required to prevent
    # sox record and save stuff if not wanted.
    decision = str(raw_input("Are you sure? (y/n) "))
    while decision == 'y':
        print "Say an English sentence."
        subprocess.Popen(str("sox -t alsa default ../data/temp/recording.wav"),
                         shell=True)
        print "*******"
        stop = str(raw_input("Enter 'y' when you've finished with a sentence"))
        print "*******"
        if stop == 'y':
            pid = subprocess.Popen("pkill sox", shell=True)
            pid.communicate()
            yousaid = sr.sRecognizer()
        if yousaid:
            say(yousaid, lang)
            decision = str(raw_input("Try it again? (y/n) "))
        elif not yousaid:
            print "Speech is unintelligible"
            decision = str(raw_input("Try it again? (y/n) "))


def sayAES(ct):
    # Tranforms the ciphertext into another string which is eventually identical
    # to the original, yet Google translate says each character one by one and
    # says x for x and Capitcal x for X where x and X are letters of the
    # alphabet.
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
    p = subprocess.Popen(str("PULSE_SINK=null cvlc --no-repeat --no-loop " +
                             "--play-and-exit ../data/temp/googlewarning.mp3"),
                         shell=True)
    p.communicate()
    time.sleep(1)
    p = subprocess.Popen(str("PULSE_SINK=null cvlc --no-repeat --no-loop " +
                             "--play-and-exit ../data/temp/googlect.mp3"),
                         shell=True)
    p.communicate()
    p = subprocess.Popen(str("PULSE_SINK=null cvlc --no-repeat --no-loop " +
                             "--play-and-exit ../data/temp/googleend.mp3"),
                         shell=True)
    p.communicate()
