from fastapi import APIRouter, Depends, HTTPException, status
from models.users import User, TokenResponse
from database.connection import Database
from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token
from fastapi.security import OAuth2PasswordRequestForm


user_router = APIRouter(
    tags=["User"],
)

users_database = Database(User)
hash_password = HashPassword()


@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )
    
    # Hashing user's password
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password

    # Signing up a new user
    await users_database.save(user)

    return {
        "message": "User created successfully!"
    }


@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm=Depends()) -> dict:
    user_exist = await User.find_one(User.email == user.username)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with supplied email does not exist"
        )

    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        return {
            'access_token': access_token,
            'token_type': 'Bearer',
        }
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed."
    )
    