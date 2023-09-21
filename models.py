from mongoengine import Document, StringField,ObjectIdField
from pydantic import BaseModel

class UserME(Document):
    id = ObjectIdField(required=True, primary_key=True)
    username = StringField(required=True)
    email = StringField(required=True, unique=True)

class UserCreate(BaseModel):
    _id: str
    username: str
    email: str

# class UserID(BaseModel):
#     _id: str
#     username: str
#     email: str