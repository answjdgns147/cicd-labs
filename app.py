import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)

DB_PATH = ":memory:"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    conn.executemany(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        [("alice", "alice@example.com"), ("bob", "bob@example.com")],
    )
    return conn


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


# TEST ONLY: intentional SQL injection for CodeQL detection testing
@app.route("/search", methods=["GET"])
def search():
    name = request.args.get("name", "")
    conn = get_db()
    query = "SELECT id, name, email FROM users WHERE name = '" + name + "'"
    rows = conn.execute(query).fetchall()
    conn.close()
    return jsonify([{"id": r[0], "name": r[1], "email": r[2]} for r in rows]), 200


if __name__ == "__main__":
    # TEST ONLY: debug mode enabled for CodeQL detection testing
    app.run(host="0.0.0.0", port=5000, debug=True)
