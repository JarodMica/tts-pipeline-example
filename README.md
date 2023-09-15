# tts-pipeline-example
Check out the YouTube tutorial that accompanies this repo: https://www.youtube.com/watch?v=MckT7z7W_qM

## Files included
- test_system_voice.py: Uses system voice as shown in the video
- test_tortoise.py: Uses tortoise API as shown in the video

The requirements.txt file **does NOT** include everything you need to run these examples. It simply contains sounddevice, soundfile, & pyttsx3.

## Considerations
**EVERYTHING in this example** has files located at the same directory level of the script.  Due to this, the string passed in for the name of the .pth file is simply "marine.pth".  However, please note that if you put the .pth file inside of a folder, the value that you pass into ```rvc_convert``` must reflect this.  For example, if you put it in a folder called "weights", your model_path would be
```model_path="weights/marine.pth```
instead of
```model_path="marine.pth```