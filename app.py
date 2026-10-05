import random
import socket
from datetime import datetime, timezone

from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

PASTEL_GRADIENTS = [
    ("#a1c4fd", "#c2e9fb"),
    ("#fbc2eb", "#a6c1ee"),
    ("#fddb92", "#d1fdff"),
    ("#d4fc79", "#96e6a1"),
    ("#ffecd2", "#fcb69f"),
    ("#e0c3fc", "#8ec5fc"),
    ("#fccb90", "#d57eeb"),
]

INDEX_TEMPLATE = """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ pod }}</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
      background: linear-gradient(135deg, {{ start }} 0%, {{ end }} 100%);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Pretendard",
        "Apple SD Gothic Neo", "Noto Sans KR", "Malgun Gothic", Roboto,
        "Helvetica Neue", Arial, sans-serif;
      color: #1f2937;
    }
    .card {
      width: 100%;
      max-width: 520px;
      padding: 48px 40px;
      background: #ffffff;
      border-radius: 24px;
      box-shadow: 0 20px 50px rgba(31, 41, 55, 0.12);
      text-align: center;
      animation: fadeIn 0.6s ease-out both;
    }
    .label {
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #6b7280;
    }
    .pod {
      margin: 16px 0 28px;
      font-size: clamp(26px, 6vw, 40px);
      font-weight: 700;
      letter-spacing: -0.02em;
      word-break: break-all;
    }
    .hint {
      padding: 14px 18px;
      border-radius: 12px;
      background: #f3f4f6;
      font-size: 15px;
      line-height: 1.6;
      color: #374151;
    }
    .timestamp {
      margin-top: 24px;
      font-size: 12px;
      color: #9ca3af;
      font-variant-numeric: tabular-nums;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(12px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>
  <main class="card">
    <p class="label">현재 응답 중인 Pod</p>
    <h1 class="pod">{{ pod }}</h1>
    <p class="hint">🔄 F5를 눌러서 새로고침하면 다른 Pod가 응답하는 걸 확인할 수 있어요</p>
    <p class="timestamp">{{ timestamp }}</p>
  </main>
</body>
</html>
"""


@app.route("/", methods=["GET"])
def index():
    start, end = random.choice(PASTEL_GRADIENTS)
    return render_template_string(
        INDEX_TEMPLATE,
        pod=socket.gethostname(),
        timestamp=datetime.now(timezone.utc).isoformat(),
        start=start,
        end=end,
    )


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "version": "v3",
        "pod": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
