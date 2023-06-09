from pydantic import BaseModel, EmailStr
from beanie import Document


class User(Document):
    """ 
        The model will be used 
        as response model 
        where we do not want to interact 
        with the password, 
        reducing the amount of work to be done.
    """
    email: EmailStr
    password: str

    
    class Settings:
        name = "users"


    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
            }
        }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
