import gtranslate
import subprocess
import ConfigParser
import urllib
import os

configParser = ConfigParser.RawConfigParser()
configFilePath = r'../config.txt'
configParser.read(configFilePath)
BM = configParser.get('System', 'BM_TEXT2SPEECH_LINK')


def callWatson(thing):
    # Need to have loaded null.monitor first
    urllib.urlretrieve(BM + "synthesize?text=" + str(thing),
                       "../data/temp/eng.ogg")
    if not os.path.exists("../data/temp/eng.ogg"):
        print "Something went wrong with with Watson synthesizing your text"
        return False
    p = subprocess.Popen("PULSE_SINK=null cvlc --play-and-exit ../data/temp/eng.ogg", shell=True)
    p.communicate()


def saySpanish(thing):
    trtemp = gtranslate.translate(thing, "fr", "en")
    urllib.urlretrieve(BM + "synthesize?text=" + str(trtemp) +
                       "&voice=VoiceEsEsEnrique", "../data/temp/es.ogg")
    if not os.path.exists("../data/temp/es.ogg"):
        print "Something went wrong with Watson synthesizing your text"
        return False
    p = subprocess.Popen("PULSE_SINK=null cvlc --play-and-exit ../data/temp/es.ogg",
                     shell=True)
    p.communicate()
