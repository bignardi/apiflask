from app import db


class User(db.Model):
    __tablename__ = 'users'

    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(20))
    name = db.Column(db.String(20))
    email = db.Column(db.String(40), unique=True)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    __tablename__ = 'posts'

    id_post = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'))

    user = db.relationship('User', foreign_keys=id_user)

    def __init__(self, content, id_user):
        self.content = content
        self.id_user = id_user

    def __repr__(self):
        return '<Post %r>' % self.id_post

class Follow(db.Model):
    __tablename__ = 'follow'

    id_follow = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'))
    id_follower = db.Column(db.Integer, db.ForeignKey('users.id_user'))

    user = db.relationship('User', foreign_keys=id_user)
    follower = db.relationship('User', foreign_keys=id_follower)