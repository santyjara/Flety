from sqlalchemy import Column, ForeignKey, Integer, String

from gateways.database.ORM import Base


class ContactORM(Base):
    __tablename__ = "contact"
    # __table_args__ = {"schema": "flety"}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    full_name = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False)
