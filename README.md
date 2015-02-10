# (S)VoIP

(Synthetic) Voice over IP

This program has only been tested on Ubuntu 14.10 Linux. To run, clone the repo and in src directory, enter "python main.py".

---
Dependencies:
- python 2.7 (Of course!)
- pactl (Must have PULSE_SINK & PULSE_SOURCE environmental variables available.)
- sox
- vlc (must be installed completely to have cvlc command available)
- espeak (optional, if you don't want to use Watson)
- pycrypto (optional, if you want to use AES functionality)
- Text to Speech synthesis app running on Bluemix (optional)
- (gTTS)[https://pypi.python.org/pypi/gTTS/1.0.2]
- PyAudio + [SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition/)

---
To use Watson. You need to have text to speech application installed on your Bluemix account and replace the link to your application in config.txt

---

Disclaimer: This started a hackathon project (+)[http://challengepost.com/software/watson-over-ip] and also my second relatively non-trivial project, so the coding quality is probably not ideal.
