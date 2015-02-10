import gtranslate
import subprocess
import ConfigParser
import urllib
import os
import speechRecognition as sr


configParser = ConfigParser.RawConfigParser()
configFilePath = r'../config.txt'
configParser.read(configFilePath)
BM = configParser.get('System', 'BM_TEXT2SPEECH_LINK')


def callWatson(thing):
    # Need to have loaded null.monitor first
    urllib.urlretrieve(BM + "synthesize?text=" + str(thing),
                       "../data/temp/eng.ogg")
    if not os.path.exists("../data/temp/eng.ogg"):
        print "Something went wrong with Watson synthesizing your text"
        return False
    p = subprocess.Popen("PULSE_SINK=null cvlc --play-and-exit ../data/temp/eng.ogg", shell=True)
    p.communicate()


def mainWatson():
    thing = str(raw_input("Say Something (w to exit): "))
    while thing != 'w':
        callWatson(thing)
        thing = str(raw_input("Say Something (w to exit): "))


def mainSpeech():
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
            callWatson(yousaid)
            decision = str(raw_input("Try it again? (y/n) "))
        elif yousaid == False:
            print "Speech is unintelligible"
            decision = str(raw_input("Try it again? (y/n) "))


def saySpanish(thing):
    trtemp = gtranslate.translate(thing, "es", "en")
    urllib.urlretrieve(BM + "synthesize?text=" + str(trtemp) +
                       "&voice=VoiceEsEsEnrique", "../data/temp/es.ogg")
    if not os.path.exists("../data/temp/es.ogg"):
        print "Something went wrong with Watson synthesizing your text"
        return False
    p = subprocess.Popen("PULSE_SINK=null cvlc --play-and-exit ../data/temp/es.ogg", shell=True)
    p.communicate()


def mainSpanish():
    thing = str(raw_input("Say Something (wes to exit): "))
    while thing != "wes":
        saySpanish(thing)
        thing = str(raw_input("Say Something (wes to exit): "))


def mainSpanishSpeech():
    decision = str(raw_input("Are you sure? (y/n) "))
    while decision == 'y':
        print "**********"
        print "Say an English sentence."
        print "**********"
        subprocess.Popen("sox -t alsa default ../data/temp/recording.wav silence 1 0.1 5% 1 1.0 5%", shell=True)
        print "**********"
        stop = str(raw_input("Enter 'y' when you've finished with a sentence"))
        print "**********"
        if stop == 'y':
            pid = subprocess.Popen("pkill sox", shell=True)
            pid.communicate()
            yousaid = sr.sRecognizer()
            if yousaid != False:
                saySpanish(yousaid)
                decision = str(raw_input("Try it again? (y/n) "))
            elif yousaid == False:
                print "Speech is unintelligible"
                decision = str(raw_input("Try it again? (y/n) "))
