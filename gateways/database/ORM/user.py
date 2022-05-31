from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
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
    user_rol_id = Column(Integer, ForeignKey("user_rol.id"))
    rol = relationship("UserRolORM")
    transport_company_id = Column(Integer, ForeignKey("transport_company.id"))
    transport_company = relationship("TransportCompanyORM")
    generator_id = Column(Integer, ForeignKey("generator.id"))
    generator = relationship("GeneratorORM")
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True))
