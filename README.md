# (S)VoIP

(Synthetic) Voice over IP

To run, clone the repo (or click on "Download Zip" to your right and extract the content). Then, in src directory, enter:
> $ python main.py.

Inside the program, type "h" for help.

---
Dependencies:
- python 2.7 (Of course!)
- pactl (Must have PULSE_SINK & PULSE_SOURCE environmental variables available.)
- sox
- vlc (must be installed completely to have cvlc command available)
- Skype (You could change your messanger in config.txt)
- espeak (optional, if you don't want to use Watson or Google)
- pycrypto (optional, if you want to use AES functionality)
- Watson's Text to Speech synthesis app running on Bluemix (optional)
- [gTTS](https://pypi.python.org/pypi/gTTS/1.0.2)
- PyAudio + [SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition/)

---
To use Watson. You need to have text to speech application installed on your Bluemix account and replace the link to your application in config.txt

---

Disclaimer: Coding quality should not be ideal since this started a hackathon project [+](http://challengepost.com/software/watson-over-ip) (although design desicions have been changed) and also my second relatively non-trivial project ever.
