from . import db
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    account_type = db.Column(db.String(80))
    pic = db.Column(db.String(200))
    date = db.Column(db.String(30))
    rsvplst = db.Column(db.String(80))


    def __init__(self, first_name, last_name, username, password,account_type,pic,date,rsvplst):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.account_type = account_type
        self.pic = pic
        self.date = date
        self.rsvplst = rsvplst

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)


class Event(db.Model):
    __tablename__ = 'event_list'

    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(80))
    date = db.Column(db.Date)
    price = db.Column(db.String(80))
    sponsors = db.Column(db.String(80))
    event_type = db.Column(db.String(255))
    venue = db.Column(db.String(80))
    pic = db.Column(db.String(200))
    rsvps = db.Column(db.Integer)
    support = db.Column(db.Float)


    def __init__(self, name,date,price,sponsors,event_type,location,pic,rsvps,support):
        self.event_name = name
        self.date = date
        self.price = price
        self.sponsors = sponsors
        self.event_type = event_type
        self.venue = location
        self.pic = pic
        self.rsvps = rsvps
        self.support = support
        

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Event %r>' % (self.event_name)
