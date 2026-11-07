# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#         def tanisiw(self):
#             print(f"Salem menin atim {self.name} jasim {self.age} ")
#
#         def magliwmatlar(self):
#             print(f"Salem menin maglimatlar {self.name} jasim {self.age}")
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this editor
from datetime import datetime
from zoneinfo import ZoneInfo

products = [
    {"code": 1, "name": "prujin", "bahasi": 50000, "sani": 25},
    {"code": 2, "name": "diska", "bahasi": 550000, "sani": 30},
]
sold_products = []
price_changes = []

while True:
    print("\nMENYU")
    print("1. Satiw")
    print("2. Baha ozgertiw")
    print("3. Esabat (Tariyx)")
    print("4. Onim izlew")
    print("5. Onim qosiw")
    print("6. Hamme onim")
    print("0. Shigiw")
    menyu = input("Tanlan (san): ").strip()

    # --- 1. Satiw ---
    if menyu == "1":
        if len(products) == 0:
            print("Sklad bos")
            continue

        Sebet = []
        jami_summa = 0
        while True:
            print("\nZatlar:")
            for p in products:
                print(f"{p['code']}. {p['name']} ({p['sani']} dana) - {p['bahasi']} som")
            kod = input("Korzinkige onimdi qosiw ushin kodti kiritin, yaki 'exit' basin: ").strip()

            if kod.lower() == "exit":
                break

            if not kod.isdigit():
                print("Kod nomer boliwi kerak.")
                continue

            kod = int(kod)
            topildi = False
            for i, p in enumerate(products):
                if p["code"] == kod:
                    topildi = True
                    satiw_bahasi = p["bahasi"] * 1.1  # +10%
                    print(f"Tanlangan: {p['name']} ({p['sani']} dana, {p['bahasi']} som)")
                    print(f"Sawda bahasi (10% qosimshasi menen): {satiw_bahasi:.2f} som/dana")

                    Korzinkidegi_san = sum(item["san"] for item in Sebet if item["p_index"] == i)
                    while True:
                        son_str = input("Neshewin satasiz: ").strip()
                        if not son_str.isdigit():
                            print("1 den baslap kiritin.")
                            continue
                        son = int(son_str)
                        if son <= 0:
                            print("1 den baslap kiritin.")
                        elif (Korzinkidegi_san + son) > p["sani"]:
                            print(f"Korzinada tek {p['sani']} dana bar. Hazirgi korzinada {Korzinkidegi_san} dana.")
                        else:
                            break

                    bu_jami = son * satiw_bahasi
                    jami_summa += bu_jami
                    Sebet.append({
                        "p_index": i,
                        "san": son,
                        "baha": satiw_bahasi,
                        "jami": bu_jami,
                        "name": p["name"]
                    })
                    print(f"  Korzinaga qosildi: {son} dana {p['name']}.")
                    print(f" Bul sawda: {bu_jami:.2f} som | Jami: {jami_summa:.2f} som")
                    break

            if not topildi:
                print("Kod tabilmadi")

        if jami_summa > 0 and len(Sebet) > 0:
            print(f"\nSebet: {len(Sebet)} ta zat. Jami: {jami_summa:.2f} som.")
            tasdiq = input("Satip alasizba? (1=awa, 0=yaq): ").strip()
            if tasdiq == "1":
                oshirishlar = []
                for item in Sebet:
                    i = item["p_index"]
                    p = products[i]
                    p["sani"] -= item["san"]
                    sold_products.append({
                        "name": item["name"],
                        "san": item["san"],
                        "baha": item["baha"],
                        "jami": item["jami"],
                        "waqt": datetime.now(ZoneInfo("Asia/Tashkent")).strftime("%Y-%m-%d %H:%M")
                    })
                    if p["sani"] == 0:
                        oshirishlar.append(i)

                for i in sorted(oshirishlar, reverse=True):
                    print(f"  {products[i]['name']} oshirildi (sani 0).")
                    products.pop(i)
                for j, p in enumerate(products):
                    p["code"] = j + 1
                print(f"\n  Satildi. Jami tolem: {jami_summa:.2f} som.")
            else:
                print("Satiw biykarlandi. Korzina tazalandi.")
        else:
            print("Korzina bos.")

    # --- 2. Baha ozgertiw ---
    elif menyu == "2":
        if len(products) == 0:
            print("Sklad bos")
            continue

        print("Onimler:")
        for p in products:
            print(f"{p['code']}. {p['name']} - {p['bahasi']} som ({p['sani']} dona)")
        kod = input("Kod kiritin: ").strip()
        topildi = False
        for p in products:
            if str(p["code"]) == kod:
                topildi = True
                print(f"\nTanlangan onim: {p['name']}")
                yangi_baha_str = input("Jana baha kiritin: ").strip()
                yangi_baha = float(yangi_baha_str) if yangi_baha_str.replace('.', '', 1).isdigit() else 0
                if yangi_baha > 0:
                    eski_baha = p["bahasi"]
                    p["bahasi"] = yangi_baha
                    vaqt = datetime.now(ZoneInfo("Asia/Tashkent")).strftime("%Y-%m-%d %H:%M")
                    price_changes.append({
                        "name": p["name"],
                        "eski": eski_baha,
                        "yangi": yangi_baha,
                        "waqt": vaqt
                    })
                    print(f"Baha ozgertildi: {eski_baha} som → {yangi_baha} som")
                else:
                    print("Baha duris kiritilmedi.")
                break
        if not topildi:
            print("Kod tabilmadi")

    # --- 3. Esabat ---
    elif menyu == "3":
        if len(sold_products) == 0 and len(price_changes) == 0:
            print("Tariyx joq.")
        else:
            if len(sold_products) > 0:
                print("\n  Satiwlar:")
                for s in sold_products:
                    print(f"{s['waqt']} | {s['name']} - {s['san']} dana = {s['jami']:.2f} som")
            if len(price_changes) > 0:
                print("\n  Baha ozgeriwi:")
                for c in sorted(price_changes, key=lambda x: x["waqt"], reverse=True):
                    print(f"{c['waqt']} | {c['name']} - {c['eski']} → {c['yangi']} som")

    # --- 4. Onim izlew ---
    elif menyu == "4":
        kod = input("Onim kodin kiritin: ").strip()
        if not kod.isdigit():
            print("Tek kod kiritin (nomer).")
            continue

        kod = int(kod)
        topildi = False
        for i, p in enumerate(products):
            if p["code"] == kod:
                topildi = True
                print(f"\nTabilgan onim: {p['name']} (kod {p['code']})")
                print(f"Sani: {p['sani']} dana | Bahasi: {p['bahasi']} som")
                print("\n1. Bahasini ozgertiw")
                print("2. Onimdi oshiriw")
                print("0. menyuge qaytiw")
                tanlov = input("Tanlan: ").strip()

                if tanlov == "1":
                    yangi_baha_str = input("Jana baha kiritin: ").strip()
                    yangi_baha = float(yangi_baha_str) if yangi_baha_str.replace('.', '', 1).isdigit() else 0
                    if yangi_baha > 0:
                        eski_baha = p["bahasi"]
                        p["bahasi"] = yangi_baha
                        vaqt = datetime.now(ZoneInfo("Asia/Tashkent")).strftime("%Y-%m-%d %H:%M")
                        price_changes.append({
                            "name": p["name"],
                            "eski": eski_baha,
                            "yangi": yangi_baha,
                            "waqt": vaqt
                        })
                        print(f"Baha ozgertildi: {eski_baha} som → {yangi_baha} som")
                    else:
                        print("Baha duris kiritilmedi.")

                elif tanlov == "2":
                    tasdiq = input("Rastan oshirejaqsizba? (1=awa, 0=yaq): ").strip()
                    if tasdiq == "1":
                        products.pop(i)
                        for j, pr in enumerate(products):
                            pr["code"] = j + 1
                        print(" Onim oshirildi.")
                break
        if not topildi:
            print("Kod tabilmadi")

    # --- 5. Onim qosiw ---
    elif menyu == "5":
        name = input("Onim atin kiritin: ").strip()
        bahasi_str = input("Bahasin kiritin: ").strip()
        sani_str = input("Sanin kiritin: ").strip()
        if not (bahasi_str.replace('.', '', 1).isdigit() and sani_str.isdigit()):
            print("Baha ham sani duris kiritilmedi.")
            continue
        bahasi = float(bahasi_str)
        sani = int(sani_str)
        code = len(products) + 1
        products.append({"code": code, "name": name, "bahasi": bahasi, "sani": sani})
        print(f" {name} qosildi. Kod: {code}")

    # --- 6. Hamma onim ---
    elif menyu == "6":
        if len(products) == 0:
            print("Sklad bos")
        else:
            print("\n Hamme onimler:")
            for p in products:
                print(f"{p['code']}. {p['name']} - {p['bahasi']} som ({p['sani']} dona)")

    # --- 0. Shigiw ---
    elif menyu == "0":
        print("Sawdaniz juwmaqlandi.")
        break

    else:
        print("Kod qate. Qayta urinip korin.")
