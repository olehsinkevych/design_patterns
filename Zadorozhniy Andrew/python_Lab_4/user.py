from abc import ABCMeta
import hashlib
import os


class User(metaclass=ABCMeta):
    """Class User represents user.
    Attributes:
        id (int): user id.
        password (str): user password.
        login_status (bool): is user logged in.
        salt (bytes): special salt to add to user password.
    Methods:
        verify_password():
            verifies user's password using hashlib and sha256 encoding.
        verify_login():
            verifies user's login.. (TO DO)
    """

    _id = 0

    def __init__(self, password: str, login_status=False) -> None:
        """Constructs all the necessary attributes for the user object.
        Args:
            password (str): user password.
            login_status (bool): is user logged in.
            salt (bytes): special salt to add to user password
        """
        super().__init__()
        User._id += 1
        self._id = User._id
        self.password = password
        self.login_status = login_status
        self_salt = None

    @property
    def password(self):
        "str: Returns user's encoded password."

        return self._password

    @password.setter
    def password(self, password):
        "Sets user's password afted encoding it using sha256."
        salt = os.urandom(32)
        self._salt = salt
        self._password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    @property
    def login_status(self):
        "bool: Returns user's login status"

        return self.login_status

    @login_status.setter
    def login_status(self, login_status):
        "Sets user's login status after verification of type of password (should be bool)."

        if isinstance(login_status, bool):
            self._login_status = login_status

    def verify_password(self, password) -> bool:
        """Verifies user password using the hashlib.pbkdf2_hmac.
        Args:
            password (str): password to verify.
        """

        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), self._salt, 100000)

        if key == self.password:
            print('Password is correct')
            return True
        else:
            print('Password is incorrect')
            return False

    def verify_login(self):
        """Verifies user's login
        TO DO: implement this method
        """

        pass


john = User(password='1', login_status=True)
print(john.password)
john.verify_password('1')
john.verify_password('pass')

michael = User(password='2', login_status=True)
print(michael._id)