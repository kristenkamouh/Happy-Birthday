# Happy-Birthday
Happy Birthday using turtle and pygame

## How to use it

### direct download 
download the latest version from the release page

## Setup yourself
### clone the repository
- first install the requirements
```bash
pip install turtle
```
```bash
pip install pygame
```
- edit the python file (change colors, change the displayed sentence, ...)
- change the theme song (change the directory/name in the main file)
- if you want to remove the song delete these lines:
  
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
- run ```auto-py-to-exe``` in your terminal
- add the file directory 
- choose if you want the app to be window or console based
- add an icon (optional)
- add extra files (add the .mp3 file for the background music)
- click on generate
- the output should be in a folder named 'output' in the directory you chose
