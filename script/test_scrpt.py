import requests, random, time, os, pygame, threading
import tkinter as tk
from dotenv import load_dotenv
from PIL import Image
from pathlib import Path
from tkinter import filedialog

# Supress message in command window
os.environ['TK_SILENCE_DEPRECATION'] = '1'


def start_script():
    # Variables definition
    global TOKEN, BOT_TOKEN, CHANNEL_URL, DM_URL, sendOwo

    root = tk.Tk()

    TOKEN_entry = tk.Entry(root)
    BOT_TOKEN_entry = tk.Entry(root)
    CHANNEL_URL_entry = tk.Entry(root)
    DM_URL_entry = tk.Entry(root)
    TOKEN = TOKEN_entry.get()
    BOT_TOKEN = BOT_TOKEN_entry.get()
    CHANNEL_URL = CHANNEL_URL_entry.get()
    DM_URL = DM_URL_entry.get()
    sendOwo = 'y' if send_owo_var.get() else 'n'
    
    # Run your script in a separate thread to avoid freezing the GUI
    script_thread = threading.Thread(target=run_script)
    script_thread.start()

def run_script():
    # universalise path definition for the image
    p1 = Path(__file__)
    p1 = p1.parent.parent.absolute()
    path = str(p1)
    print(path)

    #.env Variables
    load_dotenv()
    TOKEN = os.environ.get("TOKEN")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    CHANNEL_URL = os.environ.get("CHANNEL_URL")
    DM_URL = os.environ.get("DM_URL")

    # static Variables
    VERIFICATION_KEYWORD = "captcha"

    # ask user if bot is sending "owo"
    sendOwo = input(f"Would you like to send owo as well? (y/n)")

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
            owoIntervalNum2 = (random.randint(100,200))/100.0
            print('Seconds between each owo2 is:',owoIntervalNum2,'s')

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

            if sendOwo == "y":
                time.sleep(owoIntervalNum2)
                payload = {
                    'content': "owo"
                }
                r = requests.post(CHANNEL_URL, data=payload, headers=header)
            
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


# Create input fields and labels for .env variables
root = tk.Tk()
token_label = tk.Label(root, text="TOKEN:")
token_label.grid(row=0, column=0)
token_entry = tk.Entry(root)
token_entry.grid(row=0, column=1)

bot_token_label = tk.Label(root, text="BOT_TOKEN:")
bot_token_label.grid(row=1, column=0)
bot_token_entry = tk.Entry(root)
bot_token_entry.grid(row=1, column=1)

channel_url_label = tk.Label(root, text="CHANNEL_URL:")
channel_url_label.grid(row=2, column=0)
channel_url_entry = tk.Entry(root)
channel_url_entry.grid(row=2, column=1)

dm_url_label = tk.Label(root, text="DM_URL:")
dm_url_label.grid(row=3, column=0)
dm_url_entry = tk.Entry(root)
dm_url_entry.grid(row=3, column=1)

# Create a checkbox for sending 'owo'
send_owo_var = tk.BooleanVar()
send_owo_checkbox = tk.Checkbutton(root, text="Send 'owo'", variable=send_owo_var)
send_owo_checkbox.grid(row=4, column=0, columnspan=2)

# Create the start button
start_button = tk.Button(root, text="Start", command=start_script)
start_button.grid(row=5, column=0, columnspan=2)

root.mainloop()