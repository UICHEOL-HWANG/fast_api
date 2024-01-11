from fastapi import FastAPI

# 데이터베이스 
import models
from database import engine 

# 라우터 
from board import board_router

models.Base.metadata.create_all(bind=engine)
# 자동으로 테이블을 생성하게 설정하는 패키지

app = FastAPI() 

app.include_router(board_router.app,tags=["board"])

# board 라우터 갖고 오기 


@app.get("/")
def read_root():
    return {"Hello":"World!"}

