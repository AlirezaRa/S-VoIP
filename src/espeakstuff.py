import gtranslate
import subprocess
from subprocess import call
import speechRecognition as sr
import time


def callESpeak():
    # Must be used after main.loadNull()
    call("PULSE_SINK=null espeak -s 100", shell=True)


def mainSpeechEng():
    # For the sake of accuracy, sox records each of your sentence and saves it in temp. speechRecognition then returns 
    # a string of the content. That is passed for synthesis to speech. Since sox has to record only one sentence, it needs to be killed 
    # at some point. It would be killed if you press 'y' and hit enter by @stop variable. @decision is required to prevent
    # sox record and save stuff if not wanted.
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
    # Equivalent of callESpeak but for other languages.
    if lang != '':
        trtemp = gtranslate.translate(thing, lang, "en")
        p = subprocess.Popen('PULSE_SINK=null espeak "' + trtemp +
                             '" -v' + lang + ' -s 100', shell=True)
        p.communicate()


def main(lang):
    # Front-end called from main.py
    assert lang != ''
    temp = str(raw_input("Say something (e" + lang + " to exit): "))
    while temp != str("e" + lang):
        say(temp, lang)
        temp = str(raw_input("Say something (e" + lang + " to exit): "))


def mainSpeech(lang):
    # For the sake of accuracy, sox records each of your sentence and saves it in temp. speechRecognition then returns 
    # a string of the content. That is passed for synthesis to speech by say() for languages other than English. Since sox has to record only one sentence, it needs to be killed 
    # at some point. It would be killed if you press 'y' and hit enter by @stop variable. @decision is required to prevent
    # sox record and save stuff if not wanted.
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
    # Writes every character of the ciphertext in a newline inside a textfile so that espeak reads characters one by one
    # Also espeak is used with -k 2 so that it reads x for x and Capical x for X where x and X are letters of the alphabet.
    with open("../data/temp/ciphertext.txt", 'w') as cipher:
        ct = str(ct)
        for i in range(len(ct)):
            cipher.write(str("%c\n" % (str(ct[i]))))
    p = subprocess.Popen("espeak -f ../data/temp/ciphertext.txt -s 50 -k 2 -w ../data/temp/ct.wav", shell=True)
    p.communicate()
    p = subprocess.Popen("PULSE_SINK=null espeak 'Warning, Warning, Incoming Ciphertext.' -s 100", shell=True)
    p.communicate()
    time.sleep(2)
    p = subprocess.Popen("PULSE_SINK=null cvlc --play-and-exit ../data/temp/ct.wav", shell=True)
    p.communicate()
    time.sleep(1)
    p = subprocess.Popen("PULSE_SINK=null espeak 'End of ciphertext.' -s 80", shell=True)
    p.communicate()
