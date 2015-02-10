# coding=utf-8

import subprocess
import sys
import espeakstuff
import watsonstuff
import gspeechstuff
import aes
import os
import ConfigParser
import pprint
from gtts import gTTS

configParser = ConfigParser.RawConfigParser()
configFilePath = r'../config.txt'
configParser.read(configFilePath)
MESSENGER = configParser.get('System', 'MESSENGER')


def checkDataDir():
    # r'../data/temp' directory is used to temporary storage of
    # to-be-transmitted audio-files.
    if not os.path.exists("../data/temp"):
        os.makedirs("../data/temp")


def loadNull():
    # Loading null-sink-module for the messanger.
    procID = subprocess.check_output("pactl load-module module-null-sink",
                                     shell=True)
    procID = procID.rstrip('\n')
    return int(procID)


def unloadNull(ID):
    subprocess.Popen("pactl unload-module " + str(ID), shell=True)


def callMessenger():
    # Must have used loadNull() first. Also, you may change the messenger type
    # in config.txt
    subprocess.Popen(str("PULSE_SOURCE=null.monitor " + MESSENGER), shell=True)


def testl2(language):
    # Simple test of two character abbreviation of a language. The error are
    # being handled by the programs like "espeak".
    if language in gTTS.LANGUAGES and language.lower() != "en":
        return True
    return False


if __name__ == "__main__":
    checkDataDir()
    pactlID = loadNull()
    if type(pactlID) != int:
        print "Loading module failed"
        sys.exit(0)
    while True:
        command = str(raw_input("Enter your command (Enter 'h' for help): "))
        if command == 'h':
            # Help
            print ("m:       Open up your messanger (Currently set to be: " +
                   os.path.basename(MESSENGER) + ")")
            print ">>> eSpeak:"
            print ("e:       Type in English, eSpeak synthesizes to speech" +
                   "(press Ctrl+D to exit espeak)")
            print ("el:      Type in English, Google translates it to a" +
                   "language of your choice, eSpeak synthesizes to speech")
            print ("et:      Talk in English, Google synthesizes it to text," +
                   "eSpeak synthesizes it back to speech")
            print ("etl:     Talk in English, Google synthesizes it to text " +
                   " and translates it to a language of your choice, eSpeak " +
                   "then synthesizes it back to speech")
            print ">>> Google:"
            print "g:       Type in English, Google synthesizes to speech"
            print ("gl:      Type in English, Google translates to a language" +
                   "of your choice and synthesizes back to speech")
            print ("gt:      Talk in English, Google synthesizes it to text " +
                   " and back to speech in her own voice")
            print ("gtl:     Talk in English, Google synthesizes it to text," +
                   "translates it to a language of your choice and " +
                   "synthesizes the result back to speech")
            print ">>> Watson:"
            print ("w:       Type in English, Watson synthesizes to speech" +
                   "(press w again to exit)")
            print ("wes:     Type in English, Google translates it to " +
                   "Spanish, Watson synthesizes to speech (press wes again" +
                   " to exit)")
            print ("wt:      Talk in English, Google synthesizes it to text," +
                   "Watson synthesizes it back to speech")
            print ("wtes:    Talk in English, Google synthesizes it to text " +
                   "and translates it to Spanish, Watson then synthesizes it " +
                   "back to speech")
            print ">>> AES:"
            print ("aesenc:  Encrypt text with AES 128-bits and recite" +
                   "ciphertext")
            print ("aesdec:  Decrypt text with AES 128-bits. No voice is" +
                   "transmitted")
            print "**********"
            print "l:       Available Languages"
            print "h:       Help"
            print "q:       Exit"
        elif command == 'm':
            # Calling Skype
            callMessenger()
        elif command == 'e':
            # Calling eSpeak
            espeakstuff.callESpeak()
        elif command == "el":
            language = str(raw_input("Enter the code of your language: "))
            if testl2(language):
                espeakstuff.main(language)
        elif command == "et":
            # Calling eSpeak + Speech
            espeakstuff.mainSpeechEng()
        elif command == "etl":
            # Calling eSpeak + Speech + Translate
            language = str(raw_input("Enter the code of your language: "))
            if testl2(language):
                espeakstuff.mainSpeech(language)
        elif command == 'g':
            # Calling Google
            gspeechstuff.main()
        elif command == "gl":
            # Calling google + translate
            language = str(raw_input("Enter the code of your language: "))
            if testl2(language):
                gspeechstuff.main(language)
        elif command == "gt":
            # Calling google + speech
            gspeechstuff.mainSpeech()
        elif command == "gtl":
            # Calling google + translate + speech
            language = str(raw_input("Enter the code of your language: "))
            if testl2(language):
                gspeechstuff.mainSpeech(language)
        elif command == 'w':
            # Calling Watson
            watsonstuff.mainWatson()
        elif command == "wes":
            # Calling Watson and translate to Spanish
            watsonstuff.mainSpanish()
        elif command == "wt":
            # Speech to Text + Watson (English)
            watsonstuff.mainSpeech()
        elif command == "wtes":
            # Speech to Text + Watson (English to Spanish)
            watsonstuff.mainSpanishSpeech()
        elif command == "aesenc":
            # AES Encryption
            aes.mainEnc()
        elif command == "aesdec":
            # AES Decryption
            aes.mainDec()
        elif command == 'l':
            choice = str(raw_input("Available languages for (g)oogle or " +
                                   "(e)speak?"))
            if choice == 'g':
                # Available languages (intersection of gtts and gtranslate)
                print ("Available Languages are below. The language codes are" +
                       " the abbreviated version of the language.")
                pprint.pprint(gTTS.LANGUAGES)
            elif choice == 'e':
                print("To see available languages of espeak, visit: " +
                      "http://espeak.sourceforge.net/languages.html")
            else:
                print "Invalid choice"
        elif command == 'q':
            # Quit
            unloadNull(pactlID)
            subprocess.Popen("rm ../data/temp/*", shell=True)
            sys.exit(0)
        else:
            print "Command not understood"
