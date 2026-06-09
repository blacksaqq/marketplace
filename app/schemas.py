from pydantic import BaseModel, Field, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class UserCreate(BaseModel):
    nickname: str = Field(min_length=4, max_length=32)
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)
    
class UserRead(BaseModel):
    id: int
    nickname: str
    email: EmailStr
    role: str

    model_config = {
        'from_attributes' : True
    }
