from sqlalchemy.orm import Session 
from sqlalchemy import and_
from models import Board 
from .board_schema import NewPost,PostList,Post,UpdatePost

def insert_post(new_post:NewPost,db:Session):
    post = Board(
        writer = new_post.writer,
        title = new_post.title,
        content = new_post.content
    )
    db.add(post)
    db.commit() 
    
    return post.no

def list_all_post(db: Session):
    lists = db.query(Board).filter(Board.del_yn == 'Y').all() 
    return [PostList(no=row.no,writer=row.writer,title = row.title,date=row.date) for row in lists]
# Board 의 데이터를 모두 가져오는 대신에, del_yn은 삭제된 데이터를 제외 하고 가져오는것임


def get_post(post_no:int,db:Session):
    post = db.query(Board).filter(and_(Board.no == post_no,Board.del_yn=='Y')).first()
    return Post(no=post.no,writer=post.writer,title=post.title,content=post.content,date=post.date)
# fitler 조건을 no가 넘어온 post_no와 같은가?를 추가해줬다 

def update_post(update_post: UpdatePost, db: Session):
    post = db.query(Board).filter(and_(Board.no == update_post.no, Board.del_yn == 'Y')).first()  # update_post.no로 수정
    try:
        if not post:
            raise Exception("존재하지 않는 게시글")
        post.title = update_post.title
        post.content = update_post.content
        db.commit()
        db.refresh(post)
        return get_post(post.no, db)

    except Exception as e:
        return str(e)  # 예외 메시지를 문자열로 반환
    
def alter_del_yn(post_no: int, db: Session):
    try:
        post = db.query(Board).filter(and_(Board.no == post_no, Board.del_yn == 'Y')).first()
        if not post:
            raise Exception("존재하지 않는 게시글")
        
        # 게시글의 del_yn 값을 변경하는 로직 추가
        
        db.commit()
        db.refresh(post)
        return post
    except Exception as e:
        return str(e)

def delete_post(post_no : int, db:Session):
    try : 
        post = db.query(Board).filter(and_(Board.no == post_no, Board.del_yn == 'Y')).first()

        if not post:
            raise Exception("존재하지 않는 게시글")
        db.delete(post)
        db.commit()
        return {'msg':'삭제완료'}
    except Exception as e :
        return str(e)
        