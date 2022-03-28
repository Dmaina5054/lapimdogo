import imp
from typing import Optional
from pydantic import BaseModel, EmailStr

#properties required during user creation
class UserCreat(BaseModels):
    username: str
    email: EmailStr
    password: str 
    