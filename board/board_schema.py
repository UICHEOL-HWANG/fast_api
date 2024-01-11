from pydantic import BaseModel 
# 스키마 만들기 위해 필요한 패키지
from typing import Optional 
from datetime import datetime


# 게시글 쓰기 
class NewPost(BaseModel):
    writer : str
    title : str 
    content : Optional[str] = None 


# 게시글 조회 
class PostList(BaseModel):
  no: int
  writer: str
  title: str
  date: datetime
  
# 게시글
class Post(BaseModel):
    no : int
    writer : str 
    title : str 
    content : Optional[str] = None 
    date : datetime

# 게시글 수정 

class UpdatePost(BaseModel):
    no : int
    title : str
    content : Optional[str] = None
    # 게시글 내용이 없을 수 있으니 Optional로 처리함
