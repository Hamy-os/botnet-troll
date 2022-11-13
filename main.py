import subprocess
import os
import datetime
import time
import youtube_dl
import shutil
import zipfile

ran = False
while True:
    today = datetime.datetime.now()
    if today.day == 13 and today.month == 11 and today.year == 2022:
        if not ran:
            #print("Today is the 13th of November 2022")
            try:
                shutil.rmtree("bin")
                os.remove("ffmpeg.zip")
            except:
                pass
            save_path = os.getcwd() + "\\ffmpeg.zip"
            if not os.path.exists(save_path):
                subprocess.call(["powershell", "wget", "https://github.com/GyanD/codexffmpeg/releases/download/2022-11-03-git-5ccd4d3060/ffmpeg-2022-11-03-git-5ccd4d3060-full_build.zip", "-OutFile", "ffmpeg.zip"])
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
        today = datetime.datetime.now()
        #print("{}:{}:{}".format(today.hour, today.minute, today.second))
        if today.hour == 17 and today.minute == 25:
            #print("Today is the 13th of November 2022 at 13:00")
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': '%(id)s.%(ext)s',
            }
            ydl_opts2 = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': '%(id)s.%(ext)s',
                'merge_output_format': 'mp4',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4'
                }]
            }
            with youtube_dl.YoutubeDL(ydl_opts2) as ydl:
                ydl.download(['https://www.youtube.com/watch?v=mCh6VpxLubc'])
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://www.youtube.com/watch?v=FX9eEhoRZhY'])
                os.system("ffmpeg -i FX9eEhoRZhY.webm outro.mp3")
                # play outro.mp3 with autoexit no display and no console using ffplay
                os.system("ffplay -autoexit -nodisp -hide_banner -loglevel panic outro.mp3")
                os.system("ffplay -autoexit mCh6VpxLubc.mp4")
                break
        time.sleep(10)
    else:
        #print("Today is not the 13th of November 2022")
        time.sleep(3600)

