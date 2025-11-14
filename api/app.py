from flask import Flask, request, jsonify, send_file
from pathlib import Path
import json, os

app = Flask(__name__)

DATA_PATH = Path("/app/data/expenses.json")
DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
if not DATA_PATH.exists():
    DATA_PATH.write_text("[]", encoding="utf-8")

@app.get("/api/subject")
def subject():
    return jsonify({
        "title": "작품주제",
        "description": "KBO 데이터 웹 사이트",
        "description2":"한줄 요약: 전문 야구 지표를 제공하고 경기 결과를 예측하는 웹 사이트"
    })
@app.get("/api/rationale")
def rationale():
    return jsonify({
        "title": "실용적 근거",
        "description": "문제점: 이해하기 힘든 야구 지표, 미래의 예측성",
        "description2":"기대 가치: 차트를 활용한 가시성 향상, 예측 시스템으로 경기 전략에 활용"
    })
@app.get("/api/features")
def features():
    return jsonify({
        "title": "핵심 기능",
        "description": "기능 1:야구 실시간 소식 제공", 
        "description2": "기능 2: 자동화를 통한 경기 일정-선수 지표 최신화",
        "description3": "기능 3: 예측 시스템을 이용한 관심도 창출"
    })
@app.get("/api/environment")
def environment():
    return jsonify({
        "title": "구현환경",
        "description": "개발 언어: python3, JS, html",
        "description2":"프레임워크: next.js, numpy, pandas, sklearn, fastApi",
        "description3": "배포 환경: vercel, AWS RDS"
    })
@app.get("/api/team")
def team():
    return jsonify({
        "title": "팀 구성 및 역할",
        "description": "김덕영: 팀장, 프론트 엔드, CSS",
        "description2":"최세현: DB 데이터 관리, 예측 모델링",
        "description3": "송기준: 백엔드, 통신 연결 관리"
    })

if __name__ == "__main__":
    # 적절한 포트(예: 5000)로 0.0.0.0 에서 실행
    app.run(host="0.0.0.0", port=5000)