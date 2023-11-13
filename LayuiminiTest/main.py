from random import random

from flask import render_template, request, g

from basic import create_app
from basic.database import db
from plugins.basic.models import User, Role, UserRole

app = create_app('Development')

@app.before_request
def global_before():
    if not request.path.startswith('/static/'):
        print(request.path)
    pass

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

db.drop_all()
db.create_all()
init_db()

if __name__ == '__main__':
    app.run()
