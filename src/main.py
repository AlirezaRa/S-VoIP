# coding=utf-8

import subprocess
import sys
import espeakstuff
import watsonstuff
import speechRecognition as sr
import aes
import getpass


def loadNull():
    procID = subprocess.check_output("pactl load-module module-null-sink",
                                     shell=True)
    procID = procID.rstrip('\n')
    return int(procID)


def unloadNull(ID):
    subprocess.Popen("pactl unload-module " + str(ID), shell=True)


def callSkype():
    # Need to have loaded null.monitor first
    subprocess.Popen("PULSE_SOURCE=null.monitor skype", shell=True)


if __name__ == "__main__":
    pactlID = loadNull()
    if type(pactlID) != int:
        print "Loading module failed"
        sys.exit(0)
    while True:
        command = str(raw_input("Enter your command (Enter 'h' for help): "))
        if command == 'h':
            # Help
            print "s: Open up Skype"
            print "w: Use Watson to do English (press w again to exit)"
            print "wes: Use Watson to do Spanish (press wes again to exit)"
            print "tw: Talk in English and use Watson"
            print "tws: Talk in English, use Watson and translate to Spanish"
            print "e: Open eSpeak and do English (press Ctrl+D to exit espeak)"
            print "es: Open eSpeak and do Spanish (enter es again to exit)"
            print "fr: Open eSpeak and do French (enter fr again to exit)"
            print "aesenc: Encrypt text with AES 128-bits and recite ciphertext"
            print "aesdec: Decrypt text with AES 128-bits. No voice is transmitted"
            print "h: help"
            print "q: Exit"
        elif command == 's':
            # Calling Skype
            callSkype()
        elif command == 'e':
            # Calling eSpeak
            espeakstuff.callESpeak()
        elif command == "es":
            # eSpeak in spanish
            temp = str(raw_input("Say something in Spanish (es to exit): "))
            while temp != "es":
                espeakstuff.saySpanish(temp)
                temp = str(raw_input("Say something in Spanish (es to exit): "))
        elif command == "fr":
            # eSpeak in French
            temp = str(raw_input("Say something in French (fr to exit): "))
            while temp != "fr":
                espeakstuff.sayFrench(temp)
                temp = str(raw_input("Say something in French (fr to exit): "))
        elif command == "w":
            # Calling Watson
            thing = str(raw_input("Say Something (w to exit): "))
            while thing != "w":
                watsonstuff.callWatson(thing)
                thing = str(raw_input("Say Something (w to exit): "))
        elif command == "wes":
            # Calling Watson and translate to Spanish
            thing = str(raw_input("Say Something in Spanish (wes to exit): "))
            while thing != "wes":
                watsonstuff.saySpanish(thing)
                thing = str(raw_input("Say Something in Spanish (wes to exit): "))
        elif command == "tw":
            # Speech to Text + Watson (English)
            decision = str(raw_input("Are you sure? (y/n) "))
            while decision == 'y':
                print "Say an English sentence."
                p = subprocess.Popen("sox -t alsa default ../data/temp/recording.wav silence 1 0.1 5% 1 1.0 5%", shell=True)
                stop = str(raw_input("Enter 'y' when you've finished with a sentence"))
                if stop == 'y':
                    pid = subprocess.Popen("pkill sox", shell=True)
                    pid.communicate()
                yousaid = sr.sRecognizer()
                if yousaid != False:
                    watsonstuff.callWatson(yousaid)
                    decision = str(raw_input("Try it again? (y/n) "))
                elif yousaid == False:
                    print "Speech is unintelligible"
                    decision = str(raw_input("Try it again? (y/n) "))
        elif command == "tws":
            # Speech to Text + Watson (English to Spanish)
            decision = str(raw_input("Are you sure? (y/n) "))
            while decision == 'y':
                print "Say an English sentence."
                p = subprocess.Popen("sox -t alsa default ../data/temp/recording.wav silence 1 0.1 5% 1 1.0 5%", shell=True)
                stop = str(raw_input("Enter 'y' when you've finished with a sentence"))
                if stop == 'y':
                    pid = subprocess.Popen("pkill sox", shell=True)
                    pid.communicate()
                yousaid = sr.sRecognizer()
                if yousaid != False:
                    watsonstuff.saySpanish(yousaid)
                    decision = str(raw_input("Try it again? (y/n) "))
                elif yousaid == False:
                    print "Speech is unintelligible"
                    decision = str(raw_input("Try it again? (y/n) "))
        elif command == "aesenc":
            # AES Encryption
            message = str(raw_input("What's your secret message? "))
            key = getpass.getpass("Enter your key (shadowed input): ")
            ciphertext = aes.encrypt(message, key)
            espeakstuff.sayAES(ciphertext)
        elif command == "aesdec":
            # AES Decryption
            ciphertext = str(raw_input("What did you hear? "))
            key = getpass.getpass("Enter the key (shadowed input): ")
            message = aes.decrypt(ciphertext, key)
            d = str(raw_input("Show message? (y/n) "))
            if d == 'y':
                print message
            elif d != 'y':
                pass
        elif command == 'q':
            # Quit
            unloadNull(pactlID)
            subprocess.Popen("rm ../data/temp/*", shell=True)
            sys.exit(0)
        else:
            print "Command not understood"
