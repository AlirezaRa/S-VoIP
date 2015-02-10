import speech_recognition as sr
import subprocess


def sRecognizer():
    # speech_recognition only works with mono, not stereo.
    p = subprocess.Popen("sox ../data/temp/recording.wav ../data/temp/mono.wav channels 1", shell=True)
    p.communicate()
    r = sr.Recognizer()
    with sr.WavFile("../data/temp/mono.wav") as source:
        audio = r.record(source)
    try:
        thing = str(r.recognize(audio))
        return thing
    except LookupError:
        print "Speech is unintelligible."
        return False
