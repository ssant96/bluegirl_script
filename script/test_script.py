# To install all the needed dependencies please run 'pip install -r dependencies.txt'
import requests, random, time, os, pygame, threading, sys
import tkinter as tk
from dotenv import load_dotenv
from PIL import Image
from pathlib import Path
from tkinter import ttk
from tkinter import messagebox

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

image_file = resource_path("warning.jpg")
beep_file = resource_path("beep.mp3")
env_file = resource_path("script/.env")

# Load .env variables
exe_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
# construct the path to the .env file
env_path = os.path.join(exe_dir, "script", ".env")
env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(env_file)

# Save user given data to .env file
def save_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    script_dir = os.path.join(parent_dir, "script")

    if not os.path.exists(script_dir):
        os.makedirs(script_dir)

    env_path = os.path.join(script_dir, ".env")
    
    with open(env_path, 'w') as file:
        file.write(f"TOKEN={TOKEN.get()}\n")
        file.write(f"CHANNEL_URL={CHANNEL_URL.get()}\n")
        file.write(f"BOT_TOKEN={BOT_TOKEN.get()}\n")
        file.write(f"DM_URL={DM_URL.get()}\n")
        file.write(f"SEND_OWO={SEND_OWO.get()}\n")
    messagebox.showinfo("Good Shit", "Data saved!")

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

image_file = resource_path("warning.jpg")
beep_file = resource_path("beep.mp3")

def print_to_text_widget(text):
    output_text.insert(tk.END, text + '\n')
    output_text.see(tk.END)

def run_script():
    # universalise path definition for the image
    p1 = Path(__file__)
    p1 = p1.parent.parent.absolute()
    path = str(p1)
    print(path)

    # Load .env variables
    env_file = os.path.join(path + "/script", ".env")
    load_dotenv(env_file)

    TOKEN = os.environ.get("TOKEN")
    CHANNEL_URL = os.environ.get("CHANNEL_URL")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    DM_URL = os.environ.get("DM_URL")
    SEND_OWO = os.environ.get("SEND_OWO")

    # static Variables
    VERIFICATION_KEYWORD = "captcha"

    for i in range(7):
        rangeNumber = random.randint(30,57)
        print_to_text_widget('     -------------------------------------------------')
        print_to_text_widget('')         
        print_to_text_widget('                    PROGRAM IS RUNNING!               ')
        print_to_text_widget('') 
        print_to_text_widget('     -------------------------------------------------')
        print_to_text_widget(f'     I am going to run this {rangeNumber} times')

        count = 0
        for i in range(rangeNumber): 
            # random interval times owoh & owob are sent
            intervalNum = (random.randint(1500,2500))/100.0
            print_to_text_widget(f'     Time between each run is: {intervalNum} seconds')

            # random time inverval times between hunt and battle
            owoIntervalNum = (random.randint(100,200))/100.0
            print_to_text_widget(f'     Time between hunt & battle is: {owoIntervalNum} seconds')

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

            if SEND_OWO == "yes":
                # random time inverval times between battle and owo
                owoIntervalNum2 = (random.randint(100,200))/100.0
                print_to_text_widget(f'     Time between battle & owo is: {owoIntervalNum2} seconds')
                time.sleep(owoIntervalNum2)
                payload = {
                    'content': "owo"
                }
                r = requests.post(CHANNEL_URL, data=payload, headers=header)
            
            # displays count number
            count += 1
            print_to_text_widget(f'     This was run {count}')
            print_to_text_widget('     -------------------------------------------------')

            # checks for keyword to stop script
            r = requests.get(CHANNEL_URL, headers=header)
            messages = r.json()
                
            for message in messages:
                if VERIFICATION_KEYWORD.lower() in message['content'].lower():
                    print_to_text_widget('     -------------------------------------------------')
                    print_to_text_widget('')        
                    print_to_text_widget(f"        OWO IS ASKING FOR CAPTCHA!: {message['content']}")
                    print_to_text_widget('')
                    print_to_text_widget('     -------------------------------------------------')
                    
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
                        for i in range(10):
                            play_sound(audio_file)
                            time.sleep(1)
     
                    print_to_text_widget('     -------------------------------------------------')
                    print_to_text_widget('')         
                    print_to_text_widget('                     PROGRAM EXIT SUCCESSFUL!         ')
                    print_to_text_widget('') 
                    print_to_text_widget('     -------------------------------------------------')
                    exit(0)
            time.sleep(intervalNum)


        # random breaks values
        breakPeriod = (random.randint(900000,1800000))/1000.0
        breakPeriodinMinutes = breakPeriod/60
        print_to_text_widget(f'     I am going to take a break for {breakPeriodinMinutes} secs')
        print_to_text_widget(f'     End break at: {time.ctime()}')
        print_to_text_widget('     -------------------------------------------------')
        time.sleep(breakPeriod)

def stop_script():
    root.destroy()
    sys.exit(0)

# GUI starts here
root = tk.Tk()
root.title("OWO AUTOMATIC BOT by Spaa")
root.geometry("600x550")

# Variables
TOKEN = tk.StringVar(value=os.environ.get("TOKEN", ""))
CHANNEL_URL = tk.StringVar(value=os.environ.get("CHANNEL_URL", ""))
BOT_TOKEN = tk.StringVar(value=os.environ.get("BOT_TOKEN", ""))
DM_URL = tk.StringVar(value=os.environ.get("DM_URL", ""))
SEND_OWO = tk.StringVar(value=os.environ.get("SEND_OWO", "no"))

# Labels
ttk.Label(root, text="Your token:").grid(column=0, row=0, padx=5, pady=10, sticky=tk.W)
ttk.Label(root, text="Channel URL:").grid(column=0, row=1, padx=5, pady=10, sticky=tk.W)
ttk.Label(root, text="Bot's token:").grid(column=0, row=2, padx=5, pady=10, sticky=tk.W)
ttk.Label(root, text="DM URL:").grid(column=0, row=3, padx=5, pady=10, sticky=tk.W)

# Entry widgets
ttk.Entry(root, textvariable=TOKEN, width=82).grid(column=0, row=0, padx=80, pady=10, sticky=tk.W)
ttk.Entry(root, textvariable=CHANNEL_URL, width=82).grid(column=0, row=1, padx=80, pady=10, sticky=tk.W)
ttk.Entry(root, textvariable=BOT_TOKEN, width=82).grid(column=0, row=2, padx=80, pady=10, sticky=tk.W)
ttk.Entry(root, textvariable=DM_URL, width=82).grid(column=0, row=3, padx=80, pady=10, sticky=tk.W)

# Checkboxes
chk_box_bot_off = ttk.Checkbutton(root, text="Send Owo", variable=SEND_OWO, onvalue="yes", offvalue="no")
chk_box_bot_off.grid(column=0, row=4, padx=5, pady=10, sticky=tk.W)

# Add a text widget to the output
output_text = tk.Text(root, wrap=tk.WORD, height=15, width=60)
output_text.grid(column=0, row=8, columnspan=1, padx=60, pady=20, sticky=tk.W)

# Add a scrollbar to the text widget
scrollbar = ttk.Scrollbar(root, command=output_text.yview)
scrollbar.grid(column=2, row=8, padx=(0, 10), pady=10, sticky=tk.N+tk.S)
output_text.config(yscrollcommand=scrollbar.set)

# Save button
ttk.Button(root, text="Save Data", command=save_data).grid(column=0, row=6, padx=65, pady=5, sticky=tk.W)
ttk.Button(root, text="Run Script", command=lambda: threading.Thread(target=run_script).start()).grid(column=0, row=6, padx=263, pady=5, sticky=tk.W)
ttk.Button(root, text="Exit", command=stop_script).grid(column=0, row=6, padx=465, pady=5, sticky=tk.W)


# Run the application
root.mainloop()
