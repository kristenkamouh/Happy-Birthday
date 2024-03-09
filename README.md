# Happy-Birthday
Happy Birthday using python turtle and pygame

## Setup yourself

# direct download 
download the latest version from the release page

# clone the repository
- edit the python file (change colors, change the displayed sentece, ...)
- change the theme song (change the directory/name in the main file)
- if you want to remove the song reove thos lines:
```python
from pygame import mixer
mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load("hbd-song.mp3") #add your music file name or path
```

## Convert to exe
```bash
pip install auto-py-to-exe
```
- run ```bash auto-py-to-exe``` in your terminal
- add the file directory 
- choose if you want the app to be window or console based
- add an icon (optional)
- add extra files (in this case the .mp3 file for the background music)
- click on generate
- the output should be in a folder named 'output' in the folder you are in

