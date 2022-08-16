from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String

from gateways.database.ORM import Base


class AddressORM(Base):
    __tablename__ = "address"
    # __table_args__ = {"schema": "flety"}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    address_line_1 = Column(String(100))
    city = Column(String(30))
    zipcode = Column(String(6))
    country = Column(String(30))
    lat = Column(Float)
    long = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow())

    def __repr__(self):
        return "<Address(address_line='%s')>" % self.address_line_1
