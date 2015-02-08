import gtranslate
import subprocess
from subprocess import call
import ConfigParser

configParser = ConfigParser.RawConfigParser()
configFilePath = r'../config.txt'
configParser.read(configFilePath)
ESPEAK = configParser.get('System', 'ESPEAK_PATH')



def callESpeak():
    # Need to have loaded null.monitor first
    call("PULSE_SINK=null espeak -s 100", shell=True)



def sayFrench(thing):
    trtemp = gtranslate.translate(thing, "fr", "en")
    subprocess.Popen("PULSE_SINK=null " + ESPEAK +" '" + trtemp +
                     "' -ves -s 100", shell=True)


def saySpanish(thing):
    trtemp = gtranslate.translate(thing, "fr", "en")
    subprocess.Popen("PULSE_SINK=null " + ESPEAK + " '" + trtemp +
                     "' -vfr -s 100", shell=True)


def sayAES(ct):
    with open("../data/temp/ciphertext.txt", 'w') as cipher:
        cipher.write(str("listen, lhe coming cipher text is, " + ct))
    subprocess.Popen("espeak -f ../data/temp/ciphertext.txt -s 50 -k 2 -w ../data/temp/ct.wav", shell=True)
    q = subprocess.Popen("PULSE_SINK=null cvlc --play-and-exit ../data/temp/ct.wav", shell=True)
    q.communicate()
