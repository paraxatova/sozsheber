import os
import re
import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "app", "words.db")
if not os.path.exists(DB_PATH):
    DB_PATH = os.path.join(BASE_DIR, "words.db")


def clean_word_token(word):
    # Barliq tinish belgilerin (útiw, nokat, eki nokat, útirli nokat, tirnoqlar h.t.b) toliq tazalaw
    cleaned = re.sub(r"^[^\wʻ’ʼ`]+|[^\wʻ’ʼ`]+$", "", word)
    return cleaned.lower()


def get_suggestions(word, limit=5):
    if not word:
        return []
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    first_char = word[0]
    cursor.execute("SELECT word FROM words WHERE word LIKE ? OR length(word) BETWEEN ? AND ?",
                   (first_char + '%', max(1, len(word) - 2), len(word) + 2))
    candidates = [r[0] for r in cursor.fetchall()]
    conn.close()

    def edit_distance(s1, s2):
        if len(s1) < len(s2):
            return edit_distance(s2, s1)
        if len(s2) == 0:
            return len(s1)
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]

    suggestions = []
    for cand in set(candidates):
        dist = edit_distance(word, cand)
        if dist <= 2:
            suggestions.append((cand, dist))

    suggestions.sort(key=lambda x: x[1])
    return [s[0] for s in suggestions[:limit]]


def check_word_in_db(word):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT word FROM words WHERE word = ?", (word,))
    result = cursor.fetchone()
    conn.close()
    return result is not None


@app.route("/api/check", methods=["POST"])
def check_text():
    data = request.json or {}
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"errors": [], "total_words": 0})

    # Teksttegi barlik sozlerdi ayriqsha ajratip aliw (tinish belgilerisiz)
    raw_tokens = re.findall(r"[\wʻ’ʼ`-]+", text)

    errors = []
    processed_words = set()

    for token in raw_tokens:
        clean_word = clean_word_token(token)
        if not clean_word or clean_word.isdigit() or clean_word in processed_words:
            continue

        processed_words.add(clean_word)
        if not check_word_in_db(clean_word):
            suggestions = get_suggestions(clean_word)
            errors.append({
                "original": clean_word,
                "suggestions": suggestions
            })

    return jsonify({"errors": errors, "total_words": len(raw_tokens)})


if __name__ == "__main__":
    app.run(debug=True, port=5000)