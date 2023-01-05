from fastapi import FastAPI

app = FastAPI()

# request Get method url: "/"

# Method and Path
@app.get("/") 
async def root(): # funtion root
    return {"message": "Hello World!"}

@app.get("/api") 
async def root():
    return {"message": "welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}