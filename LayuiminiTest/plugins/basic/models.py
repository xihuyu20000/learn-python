from werkzeug.security import generate_password_hash, check_password_hash

from basic import db

class Branch(db.Model):
    __tablename__ = 'branch'
    __table_args__ = {'comment': '部门表'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, doc='部门id')
    name = db.Column(db.String(128), nullable=False, unique=True, doc='部门名称')
    pid = db.Column(db.Integer, nullable=False, default=0, doc='上级部门id')
    positions = db.relationship('Position', backref='branch', secondary='branch_position', doc='职务')

    def __init__(self, id, name, pid):
        self.id = id
        self.name = name
        self.pid = pid

class Position(db.Model):
    __tablename__ = 'position'
    __table_args__ = {'comment': '职务表'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, doc='职务id')
    name = db.Column(db.String(128), nullable=False, unique=True, doc='职务名称')
    users = db.relationship('User', backref='user', secondary='position_user', doc='用户')

    def __init__(self, id, name):
        self.id = id
        self.name = name

class BranchPosition(db.Model):
    __tablename__ = 'branch_position'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)

    def __init__(self, id, branch_id, position_id):
        self.id = id
        self.branch_id = branch_id
        self.position_id = position_id

class PositionUser(db.Model):
    __tablename__ = 'position_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, id, position_id, user_id):
        self.id = id
        self.position_id = position_id
        self.user_id = user_id

class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'comment': '用户表'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, doc='用户id')
    username = db.Column(db.String(128), nullable=False, unique=True, doc='用户名')
    _password = db.Column('password', db.String(128), doc='密码')
    email = db.Column(db.String(128), unique=True, doc='邮箱')
    roles = db.relationship('Role', backref='user', secondary='user_role', doc='角色')
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
class Role(db.Model):
    __tablename__ = 'role'
    __table_args__ = {'comment': '角色表'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, doc='角色id')
    name = db.Column(db.String(128), nullable=False, unique=True, doc='角色名')

    def __init__(self, id, name):
        self.id = id
        self.name = name

class UserRole(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

    def __init__(self, id, user_id, role_id):
        self.id = id
        self.user_id = user_id
        self.role_id = role_id

class Menu(db.Model):
    __tablename__ = 'menu'
    __table_args__ = {'comment': '菜单表'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, doc='菜单id')
    pid = db.Column(db.Integer, default=0, doc='父id')
    title = db.Column(db.String(128), nullable=False, default='', doc='名称')
    icon = db.Column(db.String(128), nullable=False, default='', doc='菜单图标')
    href = db.Column(db.String(128), nullable=False, default='', doc='链接')
    target = db.Column(db.String(24), nullable=False, default='_self', doc='链接打开方式')
    sort = db.Column(db.Integer, nullable=False, default=0, doc='排序')
    status = db.Column(db.Integer, nullable=False, default=1, doc='状态(0:禁用，1：启用)')
    remark = db.Column(db.String(256), nullable=True, doc='备注信息')

    def __init__(self, id, pid, title):
        self.id = id
        self.pid = pid
        self.title = title
















