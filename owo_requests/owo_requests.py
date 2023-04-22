# pip install -r dependencies.txt
import requests, random, time, os, pygame
from dotenv import load_dotenv
from PIL import Image
from pathlib import Path

# universalise path definition for the image
p1 = Path(__file__)
p1 = p1.parent.parent.absolute()
path = str(p1)

# static Variables
VERIFICATION_KEYWORD = "captcha"
MESSAGE_LIMIT= 5

# .env Variables
load_dotenv()
TOKEN = os.environ.get("TOKEN")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_URL = os.environ.get("CHANNEL_URL")
DM_URL = os.environ.get("DM_URL")


for i in range(7):
    rangeNumber = random.randint(30,57)
    print('--------------------------------------------------------------------------')
    print('')         
    print('                           PROGRAM IS RUNNING!                            ')
    print('') 
    print('--------------------------------------------------------------------------')

    print('I am going to run this',rangeNumber,'times and take a break')
    count = 0
    for i in range(rangeNumber): 
        # random interval times owoh & owob are sent
        intervalNum = (random.randint(1500,2500))/100.0
        print('Interval number is:',intervalNum,'s')

        # random time inverval times between owoh & owob
        owoIntervalNum = (random.randint(100,200))/100.0
        print('Seconds between each owo is:',owoIntervalNum,'s')

        # random time inverval times between owoh & owob
        # owoIntervalNum2 = (random.randint(100,200))/100.0
        # print('Seconds between each owo2 is:',owoIntervalNum2,'s')

        header = {
            'authorization': TOKEN,
        }
        payload = {
            'content': "owoh"
        }

        r = requests.post(CHANNEL_URL, data=payload, headers=header)
        time.sleep(owoIntervalNum)
        
        payload = {
            'content': "owob"
        }

        r = requests.post(CHANNEL_URL, data=payload, headers=header)

        ## Send "owo" only
        #time.sleep(owoIntervalNum2)
        # payload = {
        #     'content': "owo"
        # }
        # r = requests.post(CHANNEL_URL, data=payload, headers=header)
        
        # displays count number
        count += 1
        print('This was run',count)
        print('--------------------------------------------------------------------------')

        # checks for keyword to stop script
        r = requests.get(CHANNEL_URL, headers=header)
        messages = r.json()
            
        for message in messages:
            if VERIFICATION_KEYWORD.lower() in message['content'].lower():
                print('--------------------------------------------------------------------------')
                print('')        
                print(f"          OWO IS ASKING FOR CAPTCHA!: {message['content']}")
                print('')
                print('--------------------------------------------------------------------------')
                
                # send a DM using alt account
                header = {
                    'authorization': BOT_TOKEN,
                }
                payload = {
                    'content': "OWO is asking for CAPTCHA!"
                }
                r = requests.post(DM_URL, data=payload, headers=header)

                # shows image
                image = Image.open(path + "/warning.jpg")
                image.show()

                # play beep sound 
                def play_sound(file_path):
                    pygame.mixer.init()
                    pygame.mixer.music.load(file_path)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        time.sleep(1)

                if __name__ == "__main__":
                    audio_file = path + "/beep.mp3"
                    for i in range(50):
                        play_sound(audio_file)
                        time.sleep(1)

                print('--------------------------------------------------------------------------')
                print('')         
                print('                        PROGRAM EXIT SUCCESSFUL!                          ')
                print('') 
                print('--------------------------------------------------------------------------')
                exit(0)
        time.sleep(intervalNum)


    # random breaks values
    breakPeriod = (random.randint(900000,1800000))/1000.0
    breakPeriodInMinutes = breakPeriod/60
    print('I am going to take a break for',breakPeriodInMinutes, 'min')
    print('Start break at:', time.ctime())
    time.sleep(breakPeriod)
    print('End break at:', time.ctime())
    print('--------------------------------------------------------------------------')
