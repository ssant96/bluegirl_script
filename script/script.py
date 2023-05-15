import requests, random, time, os, pygame, sys, json
from PIL import Image
from pathlib import Path

# Defines paths for resources
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Loads data from userData.json
def load_data_from_json():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    script_dir = os.path.join(parent_dir, "script")

    json_path = os.path.join(script_dir, "userData.json")

    default_data = {
        "User Token": "",
        "Botting URL": "",
        "Bot Token": "",
        "DM URL": "",
        "Send owo": "",
        "No break": "",
    }

    if os.path.exists(json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
            # Add any missing keys to the loaded data
            for key in default_data:
                if key not in data:
                    data[key] = default_data[key]
    else:
        data = default_data

    return data

# Main script
def run_script():
    # universalise path definition for the image
    p1 = Path(__file__)
    p1 = p1.parent.parent.absolute()
    path = str(p1)
    #print(path)

    data = load_data_from_json()
    TOKEN = data["User Token"]
    CHANNEL_URL = data["Botting URL"]
    BOT_TOKEN = data["Bot Token"]
    DM_URL = data["DM URL"]
    SEND_OWO = data["Send owo"]
    NO_BREAK = data["No break"]

    # static Variables
    VERIFICATION_KEYWORD = "captcha"
    
    print('     -------------------------------------------------')
    print('')         
    print('                    PROGRAM IS RUNNING!               ')
    print('') 
    print('     -------------------------------------------------')

    for i in range(7):
        rangeNumber = random.randint(32,64)
        print(f'     I am going to run this {rangeNumber} times')

        count = 0
        for i in range(rangeNumber): 
            # random interval times between each run
            runInterval = (random.randint(1500,2500))/100.0
            print(f'     Time between each run is: {runInterval} seconds')

            # random time inverval times between hunt and battle
            h_bInterval = (random.randint(100,200))/100.0
            print(f'     Time between hunt & battle is: {h_bInterval} seconds')

            header = {
                'authorization': TOKEN,
            }
            payload = {
                'content': "owoh"
            }

            r = requests.post(CHANNEL_URL, data=payload, headers=header)
            time.sleep(h_bInterval)
            
            payload = {
                'content': "owob"
            }

            r = requests.post(CHANNEL_URL, data=payload, headers=header)

            if SEND_OWO == "yes":
                # random time inverval times between battle and owo
                b_oInterval = (random.randint(100,200))/100.0
                print(f'     Time between battle & owo is: {b_oInterval} seconds')
                time.sleep(b_oInterval)
                payload = {
                    'content': "owo"
                }
                r = requests.post(CHANNEL_URL, data=payload, headers=header)
            
            # displays count number
            count += 1
            print(f'     This was run {count}')
            print('     -------------------------------------------------')

            # checks for keyword to stop script
            r = requests.get(CHANNEL_URL, headers=header)
            messages = r.json()
                
            for message in messages:
                if VERIFICATION_KEYWORD.lower() in message['content'].lower():
                    print('     -------------------------------------------------')
                    print('')        
                    print(f"        OWO IS ASKING FOR CAPTCHA!: {message['content']}")
                    print('')
                    print('     -------------------------------------------------')
                    
                    # send a DM using alt account
                    header = {
                        'authorization': BOT_TOKEN,
                    }
                    payload = {
                        'content': "OWO is asking for CAPTCHA!"
                    }
                    r = requests.post(DM_URL, data=payload, headers=header)

                    # shows image
                    image = Image.open(resource_path("warning.jpg"))
                    image.show()

                    # play beep sound 
                    def play_sound(file_path):
                        pygame.mixer.init()
                        pygame.mixer.music.load(file_path)
                        pygame.mixer.music.play()
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)

                    if __name__ == "__main__":
                        audio_file = resource_path("beep.mp3")
                        for i in range(10):
                            play_sound(audio_file)
                            time.sleep(1)
     
                    print('     -------------------------------------------------')
                    print('')         
                    print('                     PROGRAM EXIT SUCCESSFUL!         ')
                    print('') 
                    print('     -------------------------------------------------')
                    exit(0)
            time.sleep(runInterval)

        if NO_BREAK == "yes":
            # random breaks values
            breakPeriod = (random.randint(900000,1800000))/1000.0
            breakPeriodinMinutes = breakPeriod/60
            print(f'     I am going to take a break for {breakPeriodinMinutes} secs')
            print(f'     End break at: {time.ctime()}')
            print('     -------------------------------------------------')
            time.sleep(breakPeriod)