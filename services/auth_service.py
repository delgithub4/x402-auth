from services.password_service import PasswordService
from services.token_service import TokenService


class AuthService:

    def __init__(self):

        self.password = PasswordService()

        self.token = TokenService()

        self.users = []

    def register(self, user):

        hashed = self.password.hash(
            user.password
        )

        new_user = {

            "username": user.username,

            "email": user.email,

            "password": hashed

        }

        self.users.append(new_user)

        return {

            "message": "Registration successful."

        }

    def login(
        self,
        username,
        password
    ):

        for user in self.users:

            if user["username"] == username:

                if self.password.verify(
                    password,
                    user["password"]
                ):

                    token = self.token.create(
                        username
                    )

                    return {

                        "access_token": token,

                        "token_type": "bearer"

                    }

        return {

            "message": "Invalid credentials."

        }
