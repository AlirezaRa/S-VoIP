# Synthetic VoIP
[Synthetic] Voice over IP

---

Voice modulation devices, while attempting to anonymize the voice by changing the pitch, usually leak information such as the accent of the speaker, intonation, environmental noise etc. 
This hack uses a synthetic voice (espeak) to eliminate these leakages.

## How does it work
A virtual audio device is made whose input is the output of espeak and whose output is the input of a messenger like Skype. Therefore by typing into the espeak, the generated sound would be passed through Skype.

It's trivial to add speech recognition and pass the result to espeak, I may do it in the future.

## Dependencies:
- pactl
- espeak
- A messenger capable of making an audio call like Skype

## How to work with it
Clone the repo. Give src/svoip executable permission. Do `PATH-TO-SVOIP/src/svoip -m MESSENGER` where `MESSENGER` is a messenger capable of making an audio call like Skype (it should be in your paths e.g. if the MESSENGER is Skype, then typing `skype` into the terminal should execute the program). You may also add `-s WORDS_PER_MINUTE` which would be the speed of espeak in terms of word sper minute.

After the execution of the program, make the call through the opened up messenger and when the call is established, type into the terminal.

To exit, do `CTRL+D` as it is indicated within the main loop.

## Warning:
YOU MUST EXIT THE PROGRAM WITH A CTRL+C TO PROPERLY UNLOAD PULSEAUDIO NULL-SYNC. Otherwise you need to get the module index number of the module-null-sink that was loaded by the program and unload it manually.

To get the index, do `pactl list short modules | grep SVOIP`. If an index is `n`, then do `pactl unload-module n`.

Nevertheless all changes done by the program are temporary and a restart should fix the problem as well!



## Disclaimer
This was originally a project [HopHacks Spring 2015](http://challengepost.com/software/watson-over-ip). The current version is a hugely simplified version of the version demoed at the hackathon.
