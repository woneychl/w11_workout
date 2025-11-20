from flask import Flask, render_template, jsonify
import json, os

app = Flask(__name__)

DATA_DIR = "data"

def load_json(page):
    with open(os.path.join(DATA_DIR, f"{page}.json"), "r", encoding="utf-8") as f:
        return json.load(f)

# --------------------------
# HTML 페이지 라우트
# --------------------------
@app.get("/api/health")
def health():
    return jsonify({"status": "ok"}),200

@app.get("/")
def main():
    return render_template("index.html")

@app.get("/subject")
def subject_page():
    return render_template("subject.html")

@app.get("/rationale")
def rationale_page():
    return render_template("rationale.html")

@app.get("/features")
def features_page():
    return render_template("features.html")

@app.get("/environment")
def environment_page():
    return render_template("environment.html")

@app.get("/team")
def team_page():
    return render_template("team.html")

# --------------------------
# API (JSON 제공)
# --------------------------
@app.get("/api/<page>")
def api_page(page):
    return jsonify(load_json(page))

# --------------------------
# 실행
# --------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
