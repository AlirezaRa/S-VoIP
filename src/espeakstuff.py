import gtranslate
import subprocess
from subprocess import call
import speechRecognition as sr
import time


def callESpeak():
    # Need to have loaded null.monitor first
    call("PULSE_SINK=null espeak -s 100", shell=True)


def mainSpeechEng():
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
            call(str('PULSE_SINK=null espeak "' + str(yousaid) + '" -s 100'), shell=True)
            decision = str(raw_input("Try it again? (y/n) "))
        elif yousaid == False:
            print "Speech is unintelligible"
            decision = str(raw_input("Try it again? (y/n) "))


def say(thing, lang = ''):
    if lang != '':
        trtemp = gtranslate.translate(thing, lang, "en")
        subprocess.Popen('PULSE_SINK=null espeak "' + trtemp +
                     '" -v' + lang + ' -s 100', shell=True)


def main(lang):
    assert lang != ''
    temp = str(raw_input("Say something (e" + lang + " to exit): "))
    while temp != str("e" + lang):
        say(temp, lang)
        temp = str(raw_input("Say something (e" + lang + " to exit): "))


def mainSpeech(lang):
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
                say(yousaid, lang)
                decision = str(raw_input("Try it again? (y/n) "))
            elif yousaid == False:
                print "Speech is unintelligible"
                decision = str(raw_input("Try it again? (y/n) "))


def sayAES(ct):
    with open("../data/temp/ciphertext.txt", 'w') as cipher:
        ct = str(ct)
        for i in range(len(ct)):
            cipher.write(str("%c\n" % (str(ct[i]))))
    subprocess.Popen("espeak -f ../data/temp/ciphertext.txt -s 50 -k 2 -w ../data/temp/ct.wav", shell=True)
    subprocess.Popen("PULSE_SINK=null espeak 'Warning, Warning, Incoming Ciphertext.' -s 100", shell=True)
    time.sleep(4)
    q = subprocess.Popen("PULSE_SINK=null cvlc --play-and-exit ../data/temp/ct.wav", shell=True)
    q.communicate()
    time.sleep(1)
    subprocess.Popen("PULSE_SINK=null espeak 'End of ciphertext.' -s 80", shell=True)
