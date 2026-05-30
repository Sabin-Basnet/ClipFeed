from pydantic import BaseModel
from fastapi_users import schemas
import uuid
# schemas.py defines how your data looks when it is traveling over the internet (as JSON data) between your frontend and your backend. 

class PostCreate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    title: str
    content: str

# using fastapi_users library:
# for viewing userdata (defined in library)
class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

# for creating a new user
class UserCreate(schemas.BaseUserCreate):
    pass

# for updating user data like email, password etc.
class UserUpdate(schemas.BaseUserUpdate):
    pass