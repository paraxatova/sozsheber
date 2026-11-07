import json
import os

# convert.py turgan papkani aniqlaymiz
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Fayllarning to'g'ri va aniq yo'lini ko'rsatamiz
txt_fayl = os.path.join(BASE_DIR, 'sozler.txt')
json_fayl = os.path.join(BASE_DIR, 'words.json')

lugat = {}

if os.path.exists(txt_fayl):
    with open(txt_fayl, 'r', encoding='utf-8') as f:
        for line in f:
            soz = line.strip()
            if soz:
                lugat[soz] = [soz]

    with open(json_fayl, 'w', encoding='utf-8') as jf:
        json.dump(lugat, jf, ensure_ascii=False, indent=4)

    print(f"Bajarildi! Jami {len(lugat)} ta so'z muvaffaqiyatli 'words.json' ga o'tkazildi.")
else:
    print(f"Xatolik: '{txt_fayl}' fayli topilmadi!")