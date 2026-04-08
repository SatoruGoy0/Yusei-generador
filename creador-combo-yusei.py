import random
import time
import names
import sys

time.sleep(0.1)
print("\u001B[93m⣿⣿⠿⠿⠿⠿⣿⣷⣂⠄⠄⠄⠄⠄⠄⠈⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\u001B[0m")
print("\u001B[93m⣷⡾⠯⠉⠉⠉⠉⠚⠑⠄⡀⠄⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\u001B[0m")
print("\u001B[93m⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣿⣿⣿⣿⣿\u001B[0m")
print("\u001B[93m⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠎⠄⠄⣀⡀⠄⠄⠄⠄⠄⠄⠄⠘⠋⠉⠉⠉⠉⠭\u001B[0m")
print("\u001B[93m⡀⠄⠄⠄⠄⠄⠄⠄⠄⡇⠄⣠⣾⣳⠁⠄⠄⢺⡆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\u001B[0m")
print("\u001B[93m⣿⣷⡦⠄⠄⠄⠄⠄⢠⠃⢰⣿⣯⣿⡁⢔⡒⣶⣯⡄⢀⢄⡄⠄⠄⠄⠄⠄⣀\u001B[0m")
print("\u001B[93m⠓⠄⠄⠄⠄⠄⠸⠄⢀⣤⢘⣿⣿⣷⣷⣿⠛⣾⣿⣿⣆⠾⣷⠄⠄⠄⠄⢀⣀\u001B[0m")
print("\u001B[93m⠄⠄⠄⠄⠄⠄⠄⠑⢘⣿⢰⡟⣿⣿⣷⣫⣭⣿⣾⣿⣿⣴⠏⠄⠄⢀⣺⣿⣿\u001B[0m")
print("\u001B[93m⣿⣿⣿⣿⣷⠶⠄⠄⠄⠹⣮⣹⡘⠛⠿⣫⣾⣿⣿⣿⡇⠑⢤⣶⣿⣿⣿⣿⣿\u001B[0m")
print("\u001B[93m⣿⣿⣿⣯⣤⣤⣤⣤⣀⣀⡹⣿⣿⣷⣯⣽⣿⣿⡿⣋⣴⡀⠈⣿⣿⣿⣿⣿⣿\u001B[0m")
print("\u001B[93m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣝⡻⢿⣿⡿⠋⡒⣾⣿⣧⢰⢿⣿⣿⣿⣿⣿\u001B[0m")

print("\u001B[95m 𓃭ꉔꋪꏂꋬ꒯ꄲꋪ ꒯ꏂ ꉔꄲꂵꃳꄲꇙ & ꂵ3꒤ ꏂꇙꉔꋬꋊꏂꋪ𓃸 𓁹𓁹Yusei𓁹𓁹 \u001B[0m")
time.sleep(0.1)
print(""" \u001B[96m🄲🄾🄼🄱🄾 🄾🄿🅃🄸🄾🄽🅂:\u001B[0m
\u001B[96m
1) NOMBRE: NOMBRE (Mix)
2) Nombres (Mayusculas, Minusculas)
3) GENERADOR DE CORREOS FALSOS
0) VEGETA ASCII + SALIR
\u001B[0m""")
menu = input("\u001B[93mEnter Option: \u001B[0m")

# LOGO VEGETA - Opción 0
if menu == "0":
    print("
\u001B[91m      VEGETA ASCII MINI LOGO\u001B[0m")
    print("""
   /\\    /\\  
  /  \\  /  \\ 
 |    ||    |
 |    ||    |
 |(o)(o)|   |
  \\_  _/   ,
   \\/    _/
        /
       /
    """)
    print("\u001B[92m¡Listo para escanear! 👊\u001B[0m")
    sys.exit()

# 1) COMBO NOMBRES:USUARIO
if menu == "1":
    print("\u001B[36m(.txt) \u001B[33mNombre su Combo:\u001B[0m ", end="")
    filename = input()
    hwm = int(input("\u001B[33mCuantas lineas?\u001B[0m "))
    F = f"/sdcard/combo/{filename}.txt"
    
    for i in range(hwm):
        rname = names.get_first_name()
        rlastname = names.get_last_name()
        num = random.randint(1, 99999)
        
        combos = [
            f"{rname}{num}:{rname}{num}",
            f"{rlastname}{num}:{rlastname}{num}",
            f"{rname}2022:{rname}2022",
            f"{rlastname}2022:{rlastname}2022",
            f"{rname}:{rname}",
            f"{rlastname}:{rlastname}",
            f"{num}:{num}"
        ]
        
        with open(F, "a", encoding="utf-8") as f:
            for combo in combos:
                f.write(f"{combo.lower()}
")
                f.write(f"{combo.upper()}
")
                f.write(combo + "
")
                f.write("
")

# 2) SOLO NOMBRES
if menu == "2":
    print("\u001B[36m(.txt) \u001B[33mNombre su Combo:\u001B[0m ", end="")
    filename = input()
    hwm = int(input("\u001B[33mNumero de lineas (x3):\u001B[0m "))
    F = f"/sdcard/combo/{filename}.txt"
    
    for i in range(hwm):
        rname = names.get_first_name()
        with open(F, "a", encoding="utf-8") as f:
            f.write(f"{rname}
")
            f.write(f"{rname.lower()}
")
            f.write(f"{rname.upper()}
")

# 3) CORREOS FALSOS
if menu == "3":
    print("\u001B[36mGENERADOR DE CORREOS FALSOS \u001B[33m(.txt)\u001B[0m")
    filename = input("\u001B[33mNombre del archivo:\u001B[0m ")
    hwm = int(input("\u001B[33mCuantos correos:\u001B[0m "))
    
    dominios = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "example.com"]
    print("Dominios: ", ", ".join(dominios))
    dominio = input("\u001B[33mDominio (Enter=aleatorio):\u001B[0m ").strip()
    if not dominio:
        dominio = random.choice(dominios)
    
    F = f"/sdcard/combo/{filename}.txt"
    with open(F, "w", encoding="utf-8") as f:
        for _ in range(hwm):
            rname = names.get_first_name().lower()
            rlastname = names.get_last_name().lower()
            num = random.randint(1, 9999)
            
            patrones = [
                f"{rname}{rlastname}{num}",
                f"{rname}.{rlastname}{num}",
                f"{rname}{num}",
                f"{rname[0]}{rlastname}{num}"
            ]
            email = f"{random.choice(patrones)}@{dominio}"
            print(f"\u001B[92m{email}\u001B[0m")
            f.write(email + "
")
    
    print(f"\u001B[92m¡{hwm} correos guardados en /sdcard/combo/{filename}.txt!\u001B[0m")

print("\u001B[93m¡Listo! 🎉\u001B[0m")