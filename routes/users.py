from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn
from database.connection import Database
from auth.hash_password import HashPassword


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


@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with supplied email does not exist"
        )

    if user_exist.password == user.password:
        return {
        "message": "User signed in successfully"
        }
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid detaild passed."
    )
    