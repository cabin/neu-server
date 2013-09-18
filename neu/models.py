from neu import db


class Prospect(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
    }

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(16), nullable=True)
    name = db.Column(db.Unicode(256), nullable=False)
    email = db.Column(db.Unicode(256), nullable=False)
    zipcode = db.Column(db.String(16))
    note = db.Column(db.Text())
    ip_address = db.Column(db.String(16))  # TODO: uint(4) or psql's INET
    created_at = db.Column(db.DateTime, default=db.func.now())


class Rfi(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
    }

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(16), nullable=False)
    fname = db.Column(db.Unicode(256), nullable=False)
    lname = db.Column(db.Unicode(256), nullable=False)
    email = db.Column(db.Unicode(256), nullable=False)
    phone = db.Column(db.Unicode(256))
    zipcode = db.Column(db.String(16))
    note = db.Column(db.Text())
    subscribed = db.Column(db.Boolean(), nullable=False, default=False)
    maker_faire = db.Column(db.Boolean(), nullable=False, default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
