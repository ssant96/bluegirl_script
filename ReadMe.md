# This script automates a discord game that sends out a visual and audio alert when the bot asks for a captcha.  

Little bit about the script:
This script will ask user for discord authentication token and channel URL hunt and battle commands into a specified channel. It will also
send out alerts whenever it sees "captcha" word in the channel so make sure to delete "captcha" in the channel before starting the script again.
The alerts are:
- Dm from an alt account (which is why its asking for BOT auth token and DM URL)
- Open an alert image for visual cue
- Play a sound to alert user

## Features in V 1.0
- Send owoh & owob in random realistic intervals
- Takes in user input for authorization token and channel URL
- Ask user if he/she/they want to send 'owo' as well
- Finds 'captcha' in the channel to send out alerts
- DM's your main account if triggered (finds 'captcha' in the channel)
- Opens an image for visual alert if triggered (finds 'captcha' in the channel)
- Plays a sound 10 times for warning if triggered (finds 'captcha' in the channel)
- GUI 
- .exe file available

## Features in progress
- Captcha solver
-

## Browsing this Repository

1. The **script**: contains the script that has the script and .env file 
2. **beep.mp3** is the audio file used in the script for audio alert
3. **warning.jpg** is the image file used in the script for visual alert
4. **dependencies.txt** serves the purpose of installing all the dependencies needed for this script to run

## Environment file and variables 
--- This section shows teaches you how to access all the variables needed---
To acceess token and channel URL, simply log in to the respective discord account on 
any web browser and open the web inspector > network (for some browsers you might need to enable
developer tools). Once network tab is selected click on the message option which will open 
a new window that will show the channel URL and the authorization (header section).
*NOTE: This .env file will be edited on the script so you don't need to add anything else.*
*If information was entered incorrectly, please delete everything in the .env file and try again*

## --- This section shows a sample of what the user input should look like---
TOKEN = 6TyrFg4MTA4NDUwOPx0OTkx.GpbtzP.aCQyhSxVS2v0AxgqxYc0KV3wiHEwuwN2PNQAtI
CHANNEL_URL = https://discord.com/api/v9/channels/321983247234643613/messages
BOT_TOKEN = 94r4ODg4MTA4NDUwOPx0OTkx.GpbtzP.aCQyhSxVS2v0AxgqxYc0KV3wiHEwuwN2PNQAtI
DM_URL = https://discord.com/api/v9/channels/931984142153132413/messages
SEND_OWO=yes


*REMINDER: If you are using this script, you are fully responsible for your own actions. Also, botting is not allowed*
*as per Discord and Owo policies which can potentially result in a ban. This project was done for research purposes only*