# 캡스톤 프로젝트 소개 웹(EC2+ Docker, 또는 로컬)
본 저장소는 캡스톤 프로젝트 단일 소개 페이지와 API를 제공합니다.
## 1. 작품주제(Subject)
- 제목: KBO 정보 웹 사이트
- 요약: 야구 뉴스, 지표를 제공하고 예측 시스템 구현
## 2. 실용적 근거 (Rationale)
- 문제: 이해하기 힘든 야구 지표, 미래의 예측성",
- 기대 가치: 차트를 활용한 가시성 향상, 예측 시스템으로 경기 전략에 활용
## 3. 핵심기능 (Features)
기능 1: 야구 최신 뉴스 제공
기능 2: 자동화를 통한 경기 일정-선수 지표 최신화
기능 3: 예측 시스템을 통한 야구 관심도 향상
## 4. 구현환경(Environment)
- Front-End (프론트엔드): Next.js, JS, Chart.js
- Back-End (백엔드): FastAPI, PostgreSql
- Deploy(배포): Vercel, AWS RDS
## 5. 팀원 구성 및 역할 (Team)
- 김덕영: 프론트엔드, 웹 디자인 구성
- 최세현: DB 관리, 예측 시스템 구현
- 송기준: 백엔드, 서버 관리
## 6. 실행 방법 (Run)
docker compose up --build -d
# http://localhost:5000 < 프로젝트에 맞는 포트 또는 배포된 public IP >