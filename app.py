from flask import Flask, jsonify

app = Flask(__name__)

# FAKE credentials for secret-scanning tests only (not a real key)
AWS_ACCESS_KEY_ID = "AKIAQ7RZ3MXK4WJTB2VN"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
