import os
import random
import pandas as pd
from basic import db, create_app
from plugins.basic.models import Branch, Position, BranchPosition, PositionUser, User, UserRole, Role, Menu


def read_sheet(sheet_name):
    return pd.read_excel(os.path.join(os.path.dirname(__file__), 'data.xls'), header=0,
                         sheet_name=sheet_name).itertuples()


def init_db():
    for row in read_sheet('branch'):
        db.session.add(Branch(row.id, row.name, row.pid))
    for row in read_sheet('position'):
        db.session.add(Position(row.id, row.name))
    for row in read_sheet('branch_position'):
        db.session.add(BranchPosition(row.id, row.branch_id, row.position_id))
    for row in read_sheet('position_user'):
        db.session.add(PositionUser(row.id, row.position_id, row.user_id))
    for row in read_sheet('user'):
        db.session.add(User(row.id, row.username, row.password, row.email))
    for row in read_sheet('role'):
        db.session.add(Role(row.id, row.name))
    for row in read_sheet('user_role'):
        db.session.add(UserRole(row.id, row.user_id, row.role_id))
    for row in read_sheet('menu'):
        db.session.add(Menu(row.id, row.pid, row.title))
    db.session.commit()


class BaseTest:

    def setup_class(self):
        app = create_app('Testing')
        app.app_context().push()
        self.client = app.test_client()
        db.drop_all()
        db.create_all()
        init_db()

    # def teardown_class(self):
    #     db.drop_all()
