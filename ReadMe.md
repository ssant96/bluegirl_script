# This script automates a discord game that sends out a visual and audio alert when the bot asks for a captcha.  

Who wants to actually send out bot commands on discord for a meaningless game that I don't even know why I keep playing?
Well here you are sitting like a dumbass like me but hey, this script will just do the job.

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


## Features in progress
- GUI
- Executable
- Captcha solver
-

## Browsing this Repository

1. The **script**: contains the script that has the script and .env file 
2. **beep.mp3** is the audio file used in the script for audio alert
3. **warning.jpg** is the image file used in the script for visual alert
4. **dependencies.txt** serves the purpose of installing all the dependencies needed for this script to run


# REMINDER: If you are using this script, you are fully responsible for your own actions. Also, botting is not allowed
# as per Discord and Owo policies which can potentially result in a ban. This project was done for research purposes only.