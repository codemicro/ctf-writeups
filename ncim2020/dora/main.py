import socket
import time
import tkinter as tk
import base64
import json
import hashlib
import copy
import os
from autodetection import autodetect

region_map = {
    "1": "2",
    "2": "1",
    "3": "3",
    "4": "4"
}
cache_file = "cache.json"
cache = {}


def load_cache():
    global cache
    if not os.path.exists(cache_file):
        return
    with open(cache_file) as f:
        cache = json.load(f)


def save_cache():
    global cache
    with open(cache_file, "w") as f:
        json.dump(cache, f, indent=4, sort_keys=True)


def connect():
    global s
    s = socket.socket()
    s.connect(("139.59.94.242", 8000))
    s.recv(1024)  # disregard instruction message


class Window(tk.Tk):
    def __init__(self, imgdata):
        super().__init__()
        self.geometry("750x750")
        self.title("Dora")

        self.canvas = tk.Canvas(self, width=750, height=750)
        self.canvas.pack()
        self.image = tk.PhotoImage(data=imgdata)
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")


connect()
load_cache()

old_cache = copy.deepcopy(cache)
last_hash = ""

counter = 0

while True:
    print()
    print("Loading image")
    r = b""
    while b"\n" not in r:
        r += s.recv(102400)
        time.sleep(0.25)
    
    h = hashlib.md5(r).hexdigest()
    r = r.decode().strip()

    if r == "No flag for you":
        print("!!! Incorrect region !!!")
        # revert cache to previous state
        cache = copy.deepcopy(old_cache)
        save_cache()
        # because autodetection failed, add to the manual list
        if last_hash not in cache["manual"]:
            cache["manual"].append(last_hash)
        connect()  # reconnect and start again
        counter = 0
        continue

    elif h in cache["manual"]:
        imgdata = base64.b64decode(r)  # convert base64 data to binary blob

        Window(imgdata).mainloop()  # show manual entry window

        number = input("1, 2, 3, or 4 > ")
        old_cache = copy.deepcopy(cache)
        cache["manual"].remove(h)  # assume correct entry by hooman
        cache["hash"][h] = number
        save_cache()
        counter += 1

    elif h in cache["hash"]:  # image in cache
        number = cache["hash"][h]
        print("Cache fill:", number)
        counter += 1

    else:
        # autodetect!
        with open("temp.png", "wb") as f:
            f.write(base64.b64decode(r))
        number, chance = autodetect()

        old_cache = copy.deepcopy(cache)
        cache["hash"][h] = number
        save_cache()
        counter += 1

        print("Autodetect", number, "-", chance)
    
    last_hash = h
    s.send((region_map[number] + "\n").encode())
    print("Sent " + region_map[number], "- progress " + str(counter))
