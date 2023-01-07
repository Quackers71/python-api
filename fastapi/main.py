from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "I like pizza", "id": 2}]

@app.get("/") 
async def root():
    return {"message": "Hello World!"}

@app.get("/api") 
async def root():
    return {"message": "welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    print(post)
    print(post.dict())

    post_dict = post.dict()
    post_dict['id'] =  randrange(3, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}
# title str, content str
