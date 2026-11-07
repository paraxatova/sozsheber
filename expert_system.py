def expert_system():
    print("=== Ekspert tizimi: Talabaga yo'nalish tanlashda maslahat ===")
    print("Savollarga 'ha' yoki 'yo'q' deb javob bering:\n")

    # Foydalanuvchidan javoblarni yig'ish
    math = input("Matematikani yaxshi ko'rasizmi? (ha/yo'q): ").strip().lower() == 'ha'
    programming = input("Dasturlashga qiziqasizmi? (ha/yo'q): ").strip().lower() == 'ha'
    design = input("Dizaynga qiziqasizmi? (ha/yo'q): ").strip().lower() == 'ha'
    creative = input("Ijodiy fikrlaysizmi? (ha/yo'q): ").strip().lower() == 'ha'
    data = input("Ma'lumotlar tahliliga qiziqasizmi? (ha/yo'q): ").strip().lower() == 'ha'
    networks = input("Kompyuter tarmoqlariga qiziqasizmi? (ha/yo'q): ").strip().lower() == 'ha'
    security = input("Axborot xavfsizligiga qiziqasizmi? (ha/yo'q): ").strip().lower() == 'ha'
    people = input("Odamlar bilan muloqot qilishni yoqtirasizmi? (ha/yo'q): ").strip().lower() == 'ha'
    hardware = input("Kompyuter qurilmalari va mikrosxemalarga qiziqasizmi? (ha/yo'q): ").strip().lower() == 'ha'

    print("\n--- Ekspert tizimining xulosasi ---")
    recommendations = []

    # Qoidalarni tekshirish (Bilimlar bazasi)
    if math and programming:
        recommendations.append(("Dasturiy injiniring (Software Engineering)", "1-qoida (Matematika AND Dasturlash)"))

    if design and creative:
        recommendations.append(("UI/UX Dizayn (UI/UX Design)", "2-qoida (Dizayn AND Ijodiy fikrlash)"))

    if math and data:
        recommendations.append(("Ma'lumotlar ilmi (Data Science)", "3-qoida (Matematika AND Ma'lumotlar tahlili)"))

    if networks or security:
        recommendations.append(("Kiberxavfsizlik (Cybersecurity)", "4-qoida (Tarmoqlar OR Xavfsizlik)"))

    if people:
        recommendations.append(("Menejment (Management)", "5-qoida (Odamlar bilan muloqot)"))

    if hardware:
        recommendations.append(
            ("Kompyuter injiniringi (Computer Engineering)", "6-qoida (Qurilmalar va mikrosxemalar)"))

    # Natijalarni chiqarish
    if recommendations:
        for rec, rule in recommendations:
            print(f"-> Tavsiya etilgan yo'nalish: {rec}")
            print(f"   (Asos: {rule})\n")
    else:
        print("Afsuski, berilgan javoblar bo'yicha mos yo'nalish topilmadi.")


if __name__ == "__main__":
    expert_system()