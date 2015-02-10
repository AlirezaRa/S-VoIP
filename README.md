# [S]VoIP

[Synthetic] Voice over IP

To run, clone the repo (or click on "Download Zip" to your right and extract the content). Then, in src directory, run main.py:
> $ python main.py

---
Basically, this program takes advantage of creating a virtual audio device for streaming audio from sources other
than the microphone. It creates a virtual audio device. Text to speech synthesis softwares sink their output there
and a messanger sources its input from there. Since the initial sufficient input is text i.e. a string, anything 
that can be considered as one or be transformed to one could be transfered. e.g. you may type what you want to say
or talk and Google synthesizes your speech to text which could be passed without alteration or be translated to
another language etc.

---
Example usage:
Inside SVoOP, type 'm' to start the messenger. Type 'e' to run espeak. Call someone inside the messenger. 
After sucessfully establishing a call, type inside the program and hit enter. The other side should be hearing the 
voice not you. Press "Ctrl-D" to exit espeak and return to the program.

You may want to type 'h' for other available options.

---
Warning:
YOU MUST USE 'q' COMMAND TO EXIT THE PROGRAM TO PROPERLY UNLOAD PULSEAUDIO NULL-SYNC. Otherwise, you should
unload module-null-sync yourself to go back to previous settings of the messanger or anything else you've loaded
inside. To do that, go back to the first thing that appeared in the program, you'll see the index number printed
there. Let n be that index number, the command to unload the module is:

> $ pactl unload-module n

All changes are in the memory, so if you don't know which modules to unload and are unable to use pulseaudio to do
that in GUI, just restart your system and everything should be fine.

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

Disclaimer: Coding quality should not be ideal since this started a hackathon project at [HopHacks Spring 2015](http://challengepost.com/software/watson-over-ip) (although design desicions have been
changed) and also my second relatively non-trivial project ever.
