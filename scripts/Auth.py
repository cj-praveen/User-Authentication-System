from scripts.Database import Database
import pyotp, bcrypt

class Auth(Database):
    def __init__(self) -> None:
        super().__init__()


    def authentication(self, username: str, password: str) -> dict:
        uname: list = self.db.execute("SELECT username FROM users WHERE username=(?)", (username,)).fetchall()

        if not uname:
            return dict(
                message="Account doesn't exists!",
                code=1
            )
        
        passwd: str = self.db.execute("SELECT password FROM users WHERE username=(?)", (username,)).fetchall()[0][0]
        
        if not bcrypt.checkpw(password.encode(), passwd.encode()):
            return dict(
                message="Incorrect password!",
                code=1
            )
        
        userId: str = self.db.execute("SELECT userId FROM users WHERE username=(?)", (username,)).fetchall()[0][0]
        
        return dict(
            message="Authentication success!",
            code=0,
            userId=userId
        )


    def authorization(self, userId: str, totp: str) -> dict:
        secretKey: str = self.db.execute("SELECT secretKey FROM users WHERE userId=(?)", (userId, )).fetchall()[0][0]

        if totp == pyotp.TOTP(secretKey).now():
            return dict(
                message="Authorization success!",
                code=0
            )
        
        return dict(
            message="Authorization failed!",
            code=1
        )
