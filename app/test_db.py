import sqlite3

# 1. Bazaga ulanamiz
conn = sqlite3.connect("words.db")
cursor = conn.cursor()

# 2. Bazadagi so'zlar sonini tekshiramiz
cursor.execute("SELECT COUNT(*) FROM words")
count = cursor.fetchone()[0]
print(f"Bazadagi jami so'zlar soni: {count}")

# 3. Bir nechta so'zni bazadan qidirib ko'ramiz
test_words = ["kitap", "mektep", "sózsheber", "qwertyuiop"]

print("\nSo'zlarni tekshirish testi:")
for word in test_words:
    cursor.execute("SELECT word FROM words WHERE word = ?", (word.lower(),))
    result = cursor.fetchone()
    if result:
        print(f"  ✓ '{word}' — bazada bor")
    else:
        print(f"  ✗ '{word}' — bazada YO'Q (xato deb topiladi)")

conn.close()