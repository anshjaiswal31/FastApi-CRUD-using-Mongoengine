from fastapi import FastAPI, HTTPException
from models import UserME,UserCreate
from db import connect
import uvicorn
app = FastAPI()
import json

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=9001, reload=True)

connect("mongoengine", host="mongodb://localhost:27017/mongoengine")

@app.post("/users/", response_model=UserCreate)
async def create_user(user: UserCreate):
    user_db = UserME(**user.model_dump())
    user_db.save()
    return user

@app.get("/users/{email_id}", response_model=UserCreate)
async def get_one_user(email_id: str):
    user = UserME.objects(email=email_id).first() # type: ignore
    print(user)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{email_id}", response_model=UserCreate)
async def update_user(email_id: str, user: UserCreate):
    existing_user = UserME.objects(email=email_id).first() # type: ignore
    if existing_user:
        existing_user.update(**user.model_dump())
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{email_id}", response_model=UserCreate)
async def delete_user(email_id: str):
    user = UserME.objects(email=email_id).first() # type: ignore
    if user:
        user.delete()
        return user
    raise HTTPException(status_code=404, detail="User not found")















# @app.get("/users/")
# async def get_all_users():
#     users = UserME.objects() # type: ignore
#      for user in users:
#         print(user.email)
#         print(user.first_name)
#     if users:
#         return users
#     raise HTTPException(status_code=404, detail="User not found")