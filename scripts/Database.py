import sqlite3, pyotp, uuid, bcrypt


class Database:
    def __init__(self) -> None:
        self.db = sqlite3.connect("users.db", check_same_thread=False)
        self.db.execute("CREATE TABLE IF NOT EXISTS users(username varchar(255),password varchar,secretKey varchar(32),userId varchar(100))")
        self.db.commit()

    def create_entry(self, username: str, password: str) -> bool:
        uname: list = self.db.execute("SELECT username FROM users WHERE username=(?)", (username,)).fetchall()
        
        if uname:
            return dict(
                message="Email ID already exists! Try login.",
                code=1
            )
        
        userId: str = str(uuid.uuid4())
        secretKey: str = pyotp.random_base32()
        password: str = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        self.db.execute("INSERT INTO users VALUES(?,?,?,?)", (username, password, secretKey, userId))
        self.db.commit()

        return dict(message="Account created successfully!",
            userId=userId,
            auth_uri=pyotp.totp.TOTP(secretKey).provisioning_uri(name=username, issuer_name="AppName"),
            code=0
        )


    def delete_entry(self, username: str, password: str) -> dict:
        passwd: list = self.db.execute("SELECT password FROM users WHERE username=(?)", (username,)).fetchall()

        if not passwd:
            return dict(
                message="username ID doesn't exists!",
                code=1
            )

        if bcrypt.checkpw(password.encode(), passwd[0][0].encode()):
            self.db.execute("DELETE FROM users WHERE username=(?)", (username,))
        
        return dict(
            message="Account deleted successfully!",
            code=0
        )


    def __del__(self) -> None:
        self.db.close()
