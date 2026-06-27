from datetime import datetime
from datetime import timedelta

from jose import jwt


SECRET_KEY = "x402-secret-key"

ALGORITHM = "HS256"


class TokenService:

    def create(self, username):

        payload = {
            "sub": username,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }

        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm=ALGORITHM
        )
