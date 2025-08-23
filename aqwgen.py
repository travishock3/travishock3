#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AQW Nickname Helper (Menu Version)
- Menu interaktif untuk cek & generate nickname 4–6 huruf (bisa diatur)
- Cek langsung ke https://account.aq.com/CharPage?id=<name>
- AVAILABLE kalau halaman berisi "Not Found!"
"""

import requests, random, re, time, json

AQW_CHAR_URL = "https://account.aq.com/CharPage?id="

# ---------- Generator dasar ----------
STARTS = ["v","z","x","k","r","l","dr","kr","th","sh","zy","vy","fa","va","yr"]
VOWELS = ["a","e","i","o","u","ae","ai","ea","eo","ia","ya","yr"]
ENDS   = ["n","r","s","th","sh","x","z","l","g","k","rn","ry","is","on","ar","os","ir","yn"]
BANNED = {"angel","demon","saint","magic","korea","japan","china","india","media"}

def generate_name(min_len=4, max_len=6):
    for _ in range(50):
        name = random.choice(STARTS)
        for i in range(random.randint(1,2)):
            name += random.choice(VOWELS)
            if i==0: name += random.choice(STARTS)
        name += random.choice(ENDS)
        name = re.sub(r'[^A-Za-z]','',name)
        if min_len <= len(name) <= max_len and name.lower() not in BANNED:
            return name.capitalize()
    return random.choice(["Veyr","Kyrr","Zerth","Fael","Vaeth"])

def is_name_available(name:str)->bool:
    url = AQW_CHAR_URL + requests.utils.quote(name, safe="")
    r = requests.get(url, timeout=10)
    return "not found!" in r.text.lower()

# ---------- Menu ----------
def menu():
    while True:
        print("\n=== AQW Nickname Helper ===")
        print("1) Check specific name")
        print("2) Generate available names")
        print("3) Exit")
        ch = input("Choose: ").strip()
        if ch=="1":
            name = input("Enter name: ").strip()
            print("Checking...")
            print(f"{name}: {'AVAILABLE ✅' if is_name_available(name) else 'Taken ❌'}")
        elif ch=="2":
            try:
                count = int(input("How many names? (1-10): ").strip() or "1")
            except: count=1
            found=[]
            while len(found)<count:
                cand = generate_name()
                if is_name_available(cand):
                    found.append(cand)
                    print(" [+]",cand)
                time.sleep(0.3) # delay biar sopan
            print("Done.")
        elif ch=="3":
            break
        else:
            print("Invalid choice.")

if __name__=="__main__":
    menu()