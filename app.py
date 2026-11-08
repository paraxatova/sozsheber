import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client

app = Flask(__name__)
CORS(app)

# Supabase ulanıwı
SUPABASE_URL = "https://plvzhecbijalkhcfoeeb.supabase.co"
SUPABASE_KEY = "sb_publishable_k9tGyfnO_ruKyznIsSj0kQ_EVMpHzkb"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.route('/check', methods=['POST'])
def check_word():
    data = request.get_json()
    word = data.get('word', '').strip().lower()

    if not word:
        return jsonify({"correct": False, "message": "Sóz kiritilmedi"})

    # Supabase-ten sózdi izlew
    response = supabase.table('words').select('word').eq('word', word).execute()

    if response.data:
        return jsonify({"correct": True, "word": word})
    else:
        return jsonify({"correct": False, "word": word})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)