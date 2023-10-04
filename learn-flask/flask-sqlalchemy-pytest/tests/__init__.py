import random

from basic import create_app, db
from plugins.core.models import User, Role, UserRole

def init_db():
    users = [User(username=f"user0{i}", password=f'pwd0{i}', email=f"user0{i}@qq.com") for i in range(10)]
    roles = [Role(name=f"role0{i}") for i in range(10)]
    user_roles = []

    for i in range(20):
        user_id = random.randint(1, 10)
        role_id = random.randint(1, 10)
        user_roles.append(UserRole(user_id=user_id, role_id=role_id))

    db.session.add_all(users)
    db.session.add_all(roles)
    db.session.add_all(user_roles)
    db.session.commit()





class BaseTest:
    def setup_class(self):
        app = create_app('testing')
        app.app_context().push()
        self.client = app.test_client()

        db.drop_all()
        db.create_all()

        init_db()

    def teardown_class(self):
        print('---teardown class---')
