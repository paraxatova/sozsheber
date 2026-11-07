from datetime import datetime, timedelta, timezone

uz_time = datetime.now(timezone.utc) + timedelta(hours=5)
print("O‘zbekiston vaqti:", uz_time.strftime("%Y-%m-%d %H:%M:%S"))

sale_product = [
    {"id": 1, "name": "rushka", "bahasi": 1500, "sani": 10},
    {"id": 2, "name": "qalem", "bahasi": 3000, "sani": 15},
    {"id": 3, "name": "albom", "bahasi": 12000, "sani": 5}
]

sales_history = []
brak_history = []

# 🔹 HISOBOT UCHUN QO‘SHIMCHA TARIXLAR
edit_history = []
add_history = []
remove_history = []


def show_all():
    print("Hazir bar bolgan onimler:")
    for b in sale_product:
        print(f"id:{b['id']} | {b['name']} | bahasi:{b['bahasi']} | sani:{b['sani']}")
    print()


def find_by_id(prod_id):
    for b in sale_product:
        if b["id"] == prod_id:
            return b
    return None


while True:
    print("\n1.onimdi satiw")
    print("2.onimdi redaktorlaw")
    print("3.onimdi oshiriw")
    print("4.onimdi izlew")
    print("5.onimdi qosiw")
    print("6.Barliq onimler")
    print("7.onim tariyxi")
    print("8.Esabat")
    print("9.Tamamlaw")

    a = input("buyriq berin: ")

    # 1. SATIW
    if a == "1":
        show_all()

        cart = []  # satiladigan mahsulotlar
        total_summa = 0

        while True:
            prod_id = int(input("Satiladigan onim ID (0 - toqtatuw): "))
            if prod_id == 0:
                break

            b = find_by_id(prod_id)
            if not b:
                print("Bunday ID joq!")
                continue

            if b["sani"] == 0:
                print("Bul onim tawsilgan!")
                continue

            sani = int(input("Neshe dana? "))
            if sani > b["sani"]:
                print(f"Tek {b['sani']} dana bar!")
                continue

            summa = sani * b["bahasi"]

            cart.append({
                "product": b,
                "sani": sani,
                "summa": summa
            })

            total_summa += summa
            print(f"{b['name']} ({sani} dana) qosildi.")

            if len(cart) == 3:
                print("Tek 3 ta onimge shekem satila aladi.")
                break

        if not cart:
            print("Hech narse satilmadi.")
            continue

        print("\n--- SATIW TEKSHIRIW ---")
        for item in cart:
            print(f"{item['product']['name']} - {item['sani']} dana = {item['summa']}")

        print("Barliq summa:", total_summa)

        answer = input("Onimlerdi satip alasizba? (awa|yaq): ").lower()
        if answer == "awa":
            for item in cart:
                b = item["product"]
                b["sani"] -= item["sani"]

                sales_history.append({
                    "id": b["id"],
                    "name": b["name"],
                    "bahasi": b["bahasi"],
                    "sani": item["sani"],
                    "summa": item["summa"],
                    "waqt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })

            print("Satiw tabisli amalga asirildi ✅")
        else:
            print("Satiw bekor qilindi ❌")

    # 2. REDAKTOR
    elif a == "2":
        show_all()
        pid = int(input("ID: "))
        b = find_by_id(pid)

        if b:
            eski_sani = b["sani"]
            b["name"] = input("Ati: ") or b["name"]
            b["bahasi"] = int(input("Bahasi: ") or b["bahasi"])
            b["sani"] = int(input("Sani: ") or b["sani"])

            edit_history.append({
                "id": b["id"],
                "name": b["name"],
                "eski_sani": eski_sani,
                "jana_sani": b["sani"],
                "waqt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            print("Redaktorlandi!")
        else:
            print("ID joq!")

    # 3. OSHIRIW (O‘CHIRISH)
    elif a == "3":
        show_all()
        pid = int(input("ID: "))
        b = find_by_id(pid)

        if b:
            remove_history.append({
                "id": b["id"],
                "name": b["name"],
                "sani": b["sani"],
                "waqt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            sale_product.remove(b)
            print("Onim oshirildi!")
        else:
            print("ID joq!")

    # 4. IZLEW
    elif a == "4":
        pid = int(input("ID: "))
        b = find_by_id(pid)
        print(b if b else "Topilmadi!")

    # 5. QOSIW
    elif a == "5":
        tanlaw = input("1-Ustine | 2-Taza (1/2): ")

        if tanlaw == "1":
            pid = int(input("ID: "))
            bar = find_by_id(pid)
            if bar:
                sani = int(input("Neshe dana: "))
                bar["sani"] += sani
                add_history.append({
                    "id": bar["id"],
                    "name": bar["name"],
                    "sani": sani,
                    "waqt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })

        elif tanlaw == "2":
            name = input("Ati: ")
            bahasi = int(input("Bahasi: "))
            sani = int(input("Sani: "))
            new_id = max(p["id"] for p in sale_product) + 1

            sale_product.append({
                "id": new_id,
                "name": name,
                "bahasi": bahasi,
                "sani": sani
            })

            add_history.append({
                "id": new_id,
                "name": name,
                "sani": sani,
                "waqt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    # 6. KO‘RISH
    elif a == "6":
        show_all()

    # 7. SATIW TARIYXI
    elif a == "7":
        for s in sales_history:
            print(s)

    # 8. ESABAT
    elif a == "8":
        print("\n--- ESABAT ---")
        print("Jami satiw summasi:", sum(s["summa"] for s in sales_history))

        print("\nRedaktorlangan onimler:")
        for e in edit_history:
            print(e)

        print("\nQosilgan onimler:")
        for q in add_history:
            print(q)

        print("\nOshirilgan onimler:")
        for r in remove_history:
            print(r)

    # 9. CHIQISH
    elif a == "9":
        print("Dastur toqtadi.")
        break

    else:
        print("Qate buyriq!")
