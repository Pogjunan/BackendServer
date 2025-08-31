# 베이스 이미지로 공식 Python 이미지를 사용 (슬림 버전)
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 명세 파일 복사 및 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# FastAPI(Uvicorn) 서버 실행 명령
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]



#docker run -d --cpus=1.0 --memory=1g fastapi-app:latest 이렇게 실행자원 제한가능
# docker run --gpus all 이렇게 GPU 사용가능
 