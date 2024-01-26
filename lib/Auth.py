import sqlite3, pyotp, uuid

class Auth:
    def __init__(self) -> None:
        self.db = sqlite3.connect('user.db', check_same_thread=False)
        self.db.execute("CREATE TABLE IF NOT EXISTS user(username varchar,password varchar,secret varchar,client_id varchar)")
        self.db.commit() 

    def create_entry(self, username: str, password: str) -> dict:
        try:
            if self.db.execute("SELECT username from user where username=?", (username,)).fetchall():
                return dict(message="User already exist!", code=1)
            secret_key = pyotp.random_base32()
            self.db.execute("INSERT INTO user values(?,?,?,?)", (username, password, secret_key, str(uuid.uuid1())))
            self.db.commit()
            return dict(message="Success!", code=0, 
                        content=(pyotp.totp.TOTP(secret_key).provisioning_uri(name=username, issuer_name='User Authentication System')
                         ,secret_key))
        except sqlite3.Error as e:
            print(f"An error occurred: {e.args[0]}")

    def authentication(self, username: str, password: str) -> dict:
        try:
            if i := self.db.execute("SELECT password,client_id from user where username=?", (username,)).fetchall():
                x, y = i[0]
                if password != x:
                    return dict(message="Incorrect Password!", code=1)
                return dict(message="Authentication Success!", content=y, code=0)
            return dict(message="Email don't exists", code=1)
        except sqlite3.Error as e:
            print(f"An error occurred: {e.args[0]}")

    def authorization(self, client_id: str, otp: int) -> dict:
        try:
            i = self.db.execute("SELECT secret from user where client_id=?", (client_id,)).fetchall()[0][0]
            if int(pyotp.TOTP(i).now()) != otp:
                return dict(message="Incorrect OTP!", code=1)
            return dict(message="Authorization Success!", code=0)
        except sqlite3.Error as e:
            print(f"An error occurred: {e.args[0]}")

    def __del__(self):
        self.db.close()
