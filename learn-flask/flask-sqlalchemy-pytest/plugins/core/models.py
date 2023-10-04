from werkzeug.security import generate_password_hash

from basic import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    _password = db.Column('password', db.String(128))
    email = db.Column(db.String(128), unique=True)

    roles = db.relationship('Role', backref='users', secondary='users_roles')

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)

class UserRole(db.Model):
    __tablename__ = 'users_roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)