from extensions import db


class Gym(db.Model):
    __bind_key__ = 'gyms'
    __tablename__= 'gyms'
    id = db.Column(db.Integer, primary_key=True)
    gymName = db.Column(db.String(50), unique=True)
    pricePerMonth = db.Column(db.Integer)
    is_open = db.Column(db.Boolean, default=True)

    @classmethod
    def get_by_name(cls, gymName):
        return cls.query.filter_by(gymName=gymName).first()

    @classmethod
    def get_by_email(cls, pricePerMonth):
        return cls.query.filter_by(pricePerMonth=pricePerMonth).first()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all_open(cls):
        return cls.query.filter_by(is_open=True).all()

    def save(self):
        db.session.add(self)
        db.session.commit()
