from neu import db


class Prospect(db.Model):
    __table__args = {
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
