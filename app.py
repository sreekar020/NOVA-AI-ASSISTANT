# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from new import reply  # Import your Nova logic

app = Flask(__name__)
CORS(app)  # Allow requests from your HTML/JS

# --- Chatbot Route ---
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    if not message:
        return jsonify({"reply": "Please type something to ask Nova."})
    
    response = reply(message)
    return jsonify({"reply": response})


# --- Feedback Submission Route ---
@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json()
    message = data.get("message", "").strip()
    stars = data.get("stars")

    if not message or not stars:
        return jsonify({"status": "error", "message": "Feedback and rating are required."}), 400

    try:
        conn = sqlite3.connect("feedback.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO feedback (message, stars) VALUES (?, ?)",
            (message, stars)
        )
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "Feedback submitted successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": "Database error: " + str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)