import random
import time
import names

#os.system('clear')
time.sleep(0.1)
print("\u001B[93m" + """\u001B[93m⣿⣿⠿⠿⠿⠿⣿⣷⣂⠄⠄⠄⠄⠄⠄⠈⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⡾⠯⠉⠉⠉⠉⠚⠑⠄⡀⠄⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠎⠄⠄⣀⡀⠄⠄⠄⠄⠄⠄⠄⠘⠋⠉⠉⠉⠉⠭
⡀⠄⠄⠄⠄⠄⠄⠄⠄⡇⠄⣠⣾⣳⠁⠄⠄⢺⡆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⣿⣷⡦⠄⠄⠄⠄⠄⢠⠃⢰⣿⣯⣿⡁⢔⡒⣶⣯⡄⢀⢄⡄⠄⠄⠄⠄⠄⣀
⠓⠄⠄⠄⠄⠄⠸⠄⢀⣤⢘⣿⣿⣷⣷⣿⠛⣾⣿⣿⣆⠾⣷⠄⠄⠄⠄⢀⣀
⠄⠄⠄⠄⠄⠄⠄⠑⢘⣿⢰⡟⣿⣿⣷⣫⣭⣿⣾⣿⣿⣴⠏⠄⠄⢀⣺⣿⣿
⣿⣿⣿⣿⣷⠶⠄⠄⠄⠹⣮⣹⡘⠛⠿⣫⣾⣿⣿⣿⡇⠑⢤⣶⣿⣿⣿⣿⣿
⣿⣿⣿⣯⣤⣤⣤⣤⣀⣀⡹⣿⣿⣷⣯⣽⣿⣿⡿⣋⣴⡀⠈⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣝⡻⢿⣿⡿⠋⡒⣾⣿⣧⢰⢿⣿⣿⣿⣿⣿
\u001B[0m""")
print("""\u001B[95m 𓃭ꉔꋪꏂꋬ꒯ꄲꋪ ꒯ꏂ ꉔꄲꂵꃳꄲꇙ & ꂵ3꒤ ꏂꇙꉔꋬꋊꏂꋪ𓃸 𓁹𓁹Yusei𓁹𓁹 \u001B[0m""")
time.sleep(0.1)
print(""" 🄲🄾🄼🄱🄾 🄾🄿🅃🄸🄾🄽🅂: \u001B[0m
\u001B[96m
1) NOMBRE: NOMBRE (Mix)
2) Nombres (Mayusculas, Minusculas)
3) GENERADOR DE CORREOS FALSOS
0) PARA SALIR A SCANEAR
\u001B[0m""")
menu = input("Enter Option :")

# LOGO DE VEGETA (ASCII) - solo si eliges 0
if menu == "0":
    print("
\u001B[91m      VEGETA ASCII MINI LOGO\u001B[0m
")
    print(
        r"""   /    /  
  /    /   
 |    ||    |
 |    ||    |
 |(o)(o)|   |
  _  _/   ,
   /    _/
        /
       /"""
    )
    exit()

if menu == "1":
    print("\t\t\u001B[1;33m (.txt) escriba \u001B[36m ")
    filename = input("
Nombre su Combo  :  ")
    hwm = int(input("cuantas lineas? : "))
    for i in range(0, hwm):
        rname = names.get_first_name()
        rlastname = names.get_last_name()
        num = random.randint(1, 100000)

        all1   = f"{rname}{num}"
        alln   = f"{all1}:{rname}{num}"
        all2   = f"{rlastname}{num}"
        allf   = f"{all2}:{rlastname}{num}"
        all3   = f"{rname}2022"
        alls   = f"{all3}:{rname}2022"
        all4   = f"{rlastname}2022"
        allg   = f"{all4}:{rlastname}2022"
        all5   = f"{rname}2023"
        alle   = f"{all5}:{rname}2023"
        all6   = f"{rlastname}2023"
        alld   = f"{all6}:{rlastname}2023"
        all7   = rname
        allt   = f"{all7}:{rname}"
        all8   = rlastname
        ally   = f"{all8}:{rlastname}"
        all9   = f"{rname}123"
        allp   = f"{all9}:{rname}123"
        all10  = f"{rlastname}123"
        allj   = f"{all10}:{rlastname}123"
        all11  = str(num)
        allv   = f"{all11}:{num}"

        F = f"/sdcard/combo/{filename}.txt"
        with open(F, "a+", encoding="utf-8") as f:
            f.write(f"{alln}
")
            f.write(f"{allf}
")
            f.write(f"{alln.lower()}
")
            f.write(f"{allf.lower()}
")
            f.write(f"{alls.upper()}
")
            f.write(f"{allg.upper()}
")
            f.write(f"{alle.lower()}
")
            f.write(f"{alld.lower()}
")
            f.write(f"{allt.lower()}
")
            f.write(f"{ally.lower()}
")
            f.write(f"{allt}
")
            f.write(f"{ally}
")
            f.write(f"{allp.lower()}
")
            f.write(f"{allj.lower()}
")
            f.write(f"{allp.upper()}
")
            f.write(f"{allj.upper()}
")
            f.write(f"{allv}
")

if menu == "2":
    print("\t\t\u001B[1;33m (.txt) escriba \u001B[36m ")
    filename = input("
Nombre su Combo  : ")
    hwm = int(input("numero de lineas (x2): "))
    for i in range(0, hwm):
        rname = names.get_first_name()
        rlastname = names.get_last_name()
        alln = rname
        alle = rname.upper()

        F = f"/sdcard/combo/{filename}.txt"
        with open(F, "a+", encoding="utf-8") as f:
            f.write(f"{alln}
")
            f.write(f"{alln.lower()}
")
            f.write(f"{alle}
")

if menu == "3":
    print("\t\t\u001B[1;33m GENERADOR DE CORREOS FALSOS \u001B[36m (.txt)\u001B[0m")
    filename = input("
Nombre su archivo de correos : ")
    hwm = int(input("Cuantos correos quieres generar? : "))
    dominios = [
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "outlook.com",
        "test.local",
        "example.com"
    ]
    print("Dominios disponibles: ", ", ".join(dominios))
    dominio = input("Escribe dominio (o presiona Enter para uno aleatorio): ").strip()
    if not dominio:
        dominio = random.choice(dominios)

    F = f"/sdcard/combo/{filename}.txt"
    with open(F, "a+", encoding="utf-8") as f:
        for _ in range(hwm):
            rname = names.get_first_name().lower()
            rlastname = names.get_last_name().lower()
            patrones = [
                f"{rname}{rlastname}{random.randint(1,999)}",
                f"{rname}.{rlastname}{random.randint(1,999)}",
                f"{rname}{random.randint(10,99)}",
                f"{rname[0]}{rlastname}{random.randint(1,9999)}",
                f"{rname}{rlastname}",
            ]
            user = random.choice(patrones)
            correo = f"{user}@{dominio}"
            print(correo)
            f.write(f"{correo}
")

print("\u001B[1;37;33m")