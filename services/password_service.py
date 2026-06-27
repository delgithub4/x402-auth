from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


class PasswordService:

    def hash(self, password):

        return pwd_context.hash(password)

    def verify(self, password, hashed):

        return pwd_context.verify(
            password,
            hashed
        )
