from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from gateways.database.ORM import Base


class UserORM(Base):
    __tablename__ = "user"
    # __table_args__ = {"schema": "flety"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surnames = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    addresses = relationship("AddressORM", backref="user")
    contacts = relationship("ContactORM", backref="user")
    subscription = relationship("SubscriptionORM", uselist=False, backref="user")
    user_rol = Column(
        Enum(
            "admin",
            "conductor",
            "generador",
            "propietario",
            "empresa de transporte",
            name="user_rol",
        ),
        nullable=False,
    )
    transport_company_id = Column(Integer, ForeignKey("transport_company.id"))
    transport_company = relationship("TransportCompanyORM")
    generator_id = Column(Integer, ForeignKey("generator.id"))
    generator = relationship("GeneratorORM")
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime)
