import json
import os
import sqlite3

DATABASE = 'words.db'
JSON_FILE = 'app/words.json'


def migrate_json_to_db():
  # 1. Baza hám kesteni jaratıw
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT UNIQUE NOT NULL
        )
    ''')
  conn.commit()

  # 2. words.json faylın oqıw
  if not os.path.exists(JSON_FILE):
    print(f"Qátelik: '{JSON_FILE}' faylı tabılmadı!")
    return

  try:
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
      data = json.load(f)
  except Exception as e:
    print('JSON faylın oqıwda qátelik:', e)
    return

  # 3. Bazaga sózlerdi qosıw
  count = 0
  # JSON faylıńızdıń qanday qurılısta (structure) ekenine qaray:
  # Eger ol dizim (list) bolsa, mısalı ["sóz1", "sóz2"]
  if isinstance(data, list):
    words_list = data
  # Eger ol sózlik (dict) bolsa, mısalı {"sóz1": [...], "sóz2": [...]}
  elif isinstance(data, dict):
    words_list = data.keys()
  else:
    print('JSON fayl formatı túsiniksiz.')
    return

  for word in words_list:
    clean_word = str(word).strip().lower()
    if clean_word:
      try:
        cursor.execute(
            'INSERT OR IGNORE INTO words (word) VALUES (?)', (clean_word,)
        )
        count += 1
      except sqlite3.Error as e:
        print(f"'{clean_word}' sózin qosıwda qátelik: {e}")

  conn.commit()
  conn.close()
  print(
      f'Sáwmetli tamamlandı! Jami {count} sóz bazaǵa (words.db) kóshirildi.'
  )


if __name__ == '__main__':
  migrate_json_to_db()