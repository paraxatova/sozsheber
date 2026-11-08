import sqlite3
from supabase import create_client, Client

# Haqıyqıy Project URL hám Secret Key joybarıńızdan alındı:
SUPABASE_URL = "https://plvzhecbijalkhcfoeeb.supabase.co"
SUPABASE_KEY = "sb_publishable_k9tGyfnO_ruKyznIsSj0kQ_EVMpHzkb"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_to_supabase():
    try:
        conn = sqlite3.connect('app/words.db')
        cursor = conn.cursor()
        cursor.execute("SELECT word FROM words")
        rows = cursor.fetchall()
    except Exception as e:
        print("SQLite bazasın oqıwda qátelik shıqtı (fayl jolın tekseriń):", e)
        return

    total_words = len(rows)
    print(f"Jámı {total_words} sóz tabıldı. Supabase-ge júklew baslandı...")

    batch_size = 1000
    batch = []
    uploaded = 0

    for row in rows:
        batch.append({"word": row[0]})
        if len(batch) == batch_size:
            supabase.table('words').upsert(batch, on_conflict='word').execute()
            uploaded += len(batch)
            print(f"{uploaded} / {total_words} sóz júklendi...")
            batch = []

    if batch:
        supabase.table('words').upsert(batch, on_conflict='word').execute()
        uploaded += len(batch)
        print(f"{uploaded} / {total_words} sóz júklendi...")

    print(" Tabıslı tamamlandı! Barlıq sózler Supabase bulutlı bazasına kóshirildi.")

if __name__ == "__main__":
    upload_to_supabase()