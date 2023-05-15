import requests, random, time, os, pygame, threading, sys, json
import tkinter as tk
from PIL import Image

# Save user given data to JSON file
def save_data_to_json():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    script_dir = os.path.join(parent_dir, "script")

    if not os.path.exists(script_dir):
        os.makedirs(script_dir)

    json_path = os.path.join(script_dir, "userData.json")

    data = {
        "TOKEN": TOKEN.get(),
        "CHANNEL_URL": CHANNEL_URL.get(),
        "BOT_TOKEN": BOT_TOKEN.get(),
        "DM_URL": DM_URL.get(),
        "SEND_OWO": SEND_OWO.get(),
        "BREAK": BREAK.get(),
    }

    with open(json_path, 'w') as file:
        json.dump(data, file)


def load_data_from_json():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    script_dir = os.path.join(parent_dir, "script")

    json_path = os.path.join(script_dir, "userData.json")

    default_data = {
        "TOKEN": "",
        "CHANNEL_URL": "",
        "BOT_TOKEN": "",
        "DM_URL": "",
        "SEND_OWO": "no",
        "BREAK": "no",
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


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)