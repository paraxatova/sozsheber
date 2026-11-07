from datetime import datetime, timedelta, timezone

uz_time = datetime.now(timezone.utc) + timedelta(hours=5)
print("O‘zbekiston vaqti:", uz_time.strftime("%Y-%m-%d %H:%M:%S"))

sale_product = [
    {
        "id": 1,
        "name": "rushka",
        "bahasi": 1500,
        "sani": 10
    },
    {
        "id": 2,
        "name": "qalem",
        "bahasi": 3000,
        "sani": 15
    },
    {
        "id": 3,
        "name": "albom",
        "bahasi": 12000,
        "sani": 5
    }
]

sales_history = []
brak_history = []


def show_all():
    print("Hazir bar bolgan onimler:")
    for b in sale_product:
        print(f"id: {b.get('id')} | name: {b.get('name')} | bahasi: {b.get('bahasi')} | sani: {b.get('sani')}")
    print()


def find_by_id(prod_id):
    for b in sale_product:
        if b["id"] == prod_id:
            return b
    return None


while True:
    print("1.onimdi satiw")
    print("2.onimdi redaktorlaw")
    print("3.onimdi oshiriw")
    print("4.onimdi izlew")
    print("5.onimdi qosiw")
    print("6.Barliq onimler")
    print("7. onim tariyxi")
    print("8.Esabat")
    print("9.Tamamlaw")
    a = input("buyriq berin: ")

    # if a == "1":
    #     show_all()
    #     prod_id = int(input("Ne satip almaqshisiz? "))
    #     b = find_by_id(prod_id)
    #     if not b:
    #         print("Bunday ID bar onim joq!")
    #         continue
    #     if b["sani"] == 0:
    #         print("Bulday onim bizde tawsildi!.")
    #         continue
    #
    #     sani1 = int(input("Neshe dana? "))
    #
    #     if b["sani"] >= sani1:
    #         summa = sani1 * b["bahasi"]
    #         print(f"{sani1} dana {b['name']} summa: {summa}")
    #         answer1 = input("Onimdi satip alasizba? (awa|yaq): ").lower()
    #
    #         if answer1 == "awa":
    #             b["sani"] -= sani1
    #             print(f"{sani1} dana {b['name']} satildi. Barliq summa: {summa}")
    #             sales_history.append({
    #                 "id": b["id"],
    #                 "name": b["name"],
    #                 "bahasi": b["bahasi"],
    #                 "sani": sani1,
    #                 "summa": summa,
    #                 "waqt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #             })
    #
    #         elif answer1 == "yaq":
    #             print("Satiw bekor qilindi.")
    #         else:
    #             print("Qate juwap kiritildi.")
    #
    #     else:
    #         print(f"Jeterli onim joq! Tek gana: {b['sani']} dana bar.")
    #         answer2 = input("Hammesin satip alasizba? (awa|yaq): ").lower()
    #
    #         if answer2 == "awa":
    #             sani2 = b["sani"]
    #             summa = sani2 * b["bahasi"]
    #             b["sani"] = 0
    #             print(f"{sani2} dana {b['name']} satildi. Barliq summa: {summa}")
    #             sales_history.append({
    #                 "id": b["id"],
    #                 "name": b["name"],
    #                 "bahasi": b["bahasi"],
    #                 "sani": sani2,
    #                 "summa": summa,
    #                 "waqt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #             })
    #
    #         elif answer2 == "yaq":
    #             print("Satiw bekor qilindi.")
    #         else:
    #             print("Qate juwap kiritildi.")
    #////
    if a == "1":
        while True:
            show_all()
            prod_id = int(input("Ne satip almaqshisiz? "))
            b = find_by_id(prod_id)
            if not b:
                print("Bunday ID bar onim joq!")
                continue
            if b["sani"] == 0:
                print("Bulday onim bizde tawsildi!.")
                continue

            sani1 = int(input("Neshe dana? "))

            if b["sani"] >= sani1:
                summa = sani1 * b["bahasi"]
                print(f"{sani1} dana {b['name']} summa: {summa}")
                print("Onimdi satip alasizba?")
                print("1 - awa")
                print("2 - yaq")
                answer1 = input("Tanlaw: ")

                if answer1 == "1":
                    b["sani"] -= sani1
                    print(f"{sani1} dana {b['name']} satildi. Barliq summa: {summa}")
                    sales_history.append({
                        "id": b["id"],
                        "name": b["name"],
                        "bahasi": b["bahasi"],
                        "sani": sani1,
                        "summa": summa,
                        "waqt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                else:
                    print("Satiw bekor qilindi.")

            else:
                print(f"Jeterli onim joq! Tek gana: {b['sani']} dana bar.")
                print("Hammesin satip alasizba?")
                print("1 - awa")
                print("2 - yaq")
                answer2 = input("Tanlaw: ")

                if answer2 == "1":
                    sani2 = b["sani"]
                    summa = sani2 * b["bahasi"]
                    b["sani"] = 0
                    print(f"{sani2} dana {b['name']} satildi. Barliq summa: {summa}")
                    sales_history.append({
                        "id": b["id"],
                        "name": b["name"],
                        "bahasi": b["bahasi"],
                        "sani": sani2,
                        "summa": summa,
                        "waqt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                else:
                    print("Satiw bekor qilindi.")

            # 🔴 Sotishni davom ettirish
            print("\nJane onim satip alasizba?")
            print("1 - awa")
            print("2 - yaq")
            cont = input("Tanlaw: ")
            if cont == "1":
                continue
            else:
                break
    # if a == "1":
    #     show_all()
    #
    #     cart = []  # satiladigan mahsulotlar
    #     total_summa = 0
    #
    #     while True:
    #         prod_id = int(input("Satiladigan onim ID (0 - toqtatuw): "))
    #         if prod_id == 0:
    #             break
    #
    #         b = find_by_id(prod_id)
    #         if not b:
    #             print("Bunday ID joq!")
    #             continue
    #
    #         if b["sani"] == 0:
    #             print("Bul onim tawsilgan!")
    #             continue
    #
    #         sani = int(input("Neshe dana? "))
    #         if sani > b["sani"]:
    #             print(f"Tek {b['sani']} dana bar!")
    #             continue
    #
    #         summa = sani * b["bahasi"]
    #
    #         cart.append({
    #             "product": b,
    #             "sani": sani,
    #             "summa": summa
    #         })
    #
    #         total_summa += summa
    #         print(f"{b['name']} ({sani} dana) qosildi.")
    #
    #         if len(cart) == 3:
    #             print("Tek 3 ta onimge shekem satila aladi.")
    #             break
    #
    #     if not cart:
    #         print("Hech narse satilmadi.")
    #         continue
    #
    #     print("\n--- SATIW TEKSE ---")
    #     for item in cart:
    #         print(f"{item['product']['name']} - {item['sani']} dana = {item['summa']}")
    #
    #     print("Barliq summa:", total_summa)
    #
    #     answer = input("Onimlerdi satip alasizba? (awa|yaq): ").lower()
    #     if answer == "awa":
    #         for item in cart:
    #             b = item["product"]
    #             b["sani"] -= item["sani"]
    #
    #             sales_history.append({
    #                 "id": b["id"],
    #                 "name": b["name"],
    #                 "bahasi": b["bahasi"],
    #                 "sani": item["sani"],
    #                 "summa": item["summa"],
    #                 "waqt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #             })
    #
    #         print("Satiw tabisli amalga asirildi ✅")
    #     else:
    #         print("Satiw bekor qilindi ❌")


    elif a == "2":
        show_all()
        prod_id = int(input("Qaysi onimni redaktorlaymiz? (id): "))
        b = find_by_id(prod_id)

        if b:
            print("\nNeni ozgertmekshisiz?")
            print("1. Ati")
            print("2. Bahasi")
            print("3. Sani")
            print("Masalan: 1,2 yoki 2,3 yoki 1,3 yoki 1,2,3")
            tanlov = input("Tanlaw cifrlar menen (utir menen ajratilgan): ")

            tanlov_list = [x.strip() for x in tanlov.split(",")]
            eski_sani = b["sani"]

            if "1" in tanlov_list:
                b["name"] = input(f"Jana ati ({b['name']}): ") or b["name"]
            if "2" in tanlov_list:
                b["bahasi"] = int(input(f"Jana bahasi ({b['bahasi']}): ") or b["bahasi"])
            if "3" in tanlov_list:
                yangi_sani_input = input(f"Jana sani ({b['sani']}): ")
                if yangi_sani_input.strip():
                    b["sani"] = int(yangi_sani_input)

            print("Onim redaktorlandi.")

            if b["sani"] != eski_sani:
                farq = eski_sani - b["sani"]

                if farq > 0:
                    print(f"Brak: {farq}  boldi.")
                    brak_history.append({
                        "id": b["id"],
                        "name": b["name"],
                        "sani": farq,
                        "vaqt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })

                elif farq < 0:
                    print(f"{abs(farq)}  qosildi.")

        else:
            print("Bunday ID bar onim joq!")

    elif a == "3":
        show_all()
        prod_id = int(input("Qaysi onimni oshiramiz? (id): "))
        b = find_by_id(prod_id)
        if b:
            sale_product.remove(b)
            print(f"{b['name']} dizimden oshirildi.")
        else:
            print("Bunday ID bar onim joq!")

    elif a == "4":
        prod_id = int(input("Qaysi ID bo‘yicha izlew kerek: "))
        b = find_by_id(prod_id)
        if b:
            print("\nOnim magliwmatlari:")
            print(f"id: {b['id']}")
            print(f"ati: {b['name']}")
            print(f"bahasi: {b['bahasi']}")
            print(f"sani: {b['sani']}\n")
        else:
            print("Bunday ID bar onim joq!")

    elif a == "5":
        print("\nJana product qosiw: ")
        tanlaw = input("1 - Ustine qosiw | 2 - Taza onim qosiw (1/2): ")

        if tanlaw == "1":
            idn = int(input("id: "))
            bar = find_by_id(idn)

            if bar:
                print(f"Bul id bizde bar: {bar['name']} (hazir {bar['sani']} dana)")
                sani = int(input("Neshe dana qosiw kerek: "))
                bar["sani"] += sani
                print(f"{bar['name']} endi hazirgi sani: {bar['sani']} dana.")
            else:
                print("Bul id onim joq!")

        elif tanlaw == "2":
            name = input("Onim ati: ")
            bahasi = int(input("Bahasi: "))
            sani = int(input("Sani: "))
            jana_bahasi = int(bahasi * 1.25)

            new_id = max(p["id"] for p in sale_product)
    elif a == "6":
        show_all()

        # 7. TARIYX
    elif a == "7":
        if not sales_history:
            print("Satiw joq")
        else:
            for s in sales_history:
                print(s)

        # 8. ESABAT
    elif a == "8":
        jami = sum(s["summa"] for s in sales_history)
        print("Jami summa:", jami)

        # 9. TAMAMLASH
    elif a == "9":
        answer = input("Kundi juwmaqlaysizba?(awa| yaq): ").lower()
        if answer == "awa":
            print("Kun juwmaqlandi!!")
            break
        elif answer == "yaq":
            print("Kun dawam etip atir..")


    else:

        print("Buyriq qate...!")

    # show_all()