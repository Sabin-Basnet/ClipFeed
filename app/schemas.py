from pydantic import BaseModel
from fastapi_users import schemas
import uuid
from datetime import datetime

# schemas.py defines how your data looks when it is traveling over the internet (as JSON data) between your frontend and your backend.


class PostCreate(BaseModel):
    caption: str
    file_type: str
    file_name: str


class PostResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    caption: str
    url: str
    file_type: str
    file_name: str
    created_at: datetime

    class Config:
        from_attributes = True


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