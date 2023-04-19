from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

class HashPassword:

    def create_hash(self, password: str):
        """
            The method takes a string and returns the hashed value.
        """
        return pwd_context.hash(password)
    
    def verify_hash(self, plain_password: str, hashed_password: str):
        """
            Takes the plain password 
            and the hashed password 
            and compares them. 
            The function returns a Boolean value 
            indicating whether the values passed 
            are the same or not.
        """
        return pwd_context.verify(plain_password, hashed_password)
