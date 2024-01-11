from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

DB_URL = "sqlite:///./fast_api.db"

engine = create_engine(DB_URL,pool_size=50,connect_args={"check_same_thread": False})
# sqlite는 기본적으로 한 개의 스레드만 DB에 접근할 수 있도록 제한 
# 그렇기에 check_same_thread = False로 줘서 여러 스레드에서 접근할 수 있도록 접근 
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()


# 게시글이 만약 없다면 예외처리를 추가해줘야 한다. 

def get_db():
    db = SessionLocal() 
    try :
        yield db 
    finally:
        db.close()
    