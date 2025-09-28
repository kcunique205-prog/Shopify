import os
from flask import Flask, jsonify

# Flask app banayein
app = Flask(__name__)

# '/' route banayein (yeh aapke main URL par chalega)
@app.route('/')
def home():
    # Ek simple JSON response bhejें
    response = {
        "status": "success",
        "message": "API is alive and running! Made By @diwazz"
    }
    return jsonify(response)

# Ek aur example route
@app.route('/ping')
def ping():
    return "Pong!"

# --- Server Start ---
if __name__ == "__main__":
    # Render is port ka istemaal karega
    port = int(os.environ.get("PORT", 5000))
    # Server ko sabhi network interfaces par chalayein
    app.run(host='0.0.0.0', port=port)
