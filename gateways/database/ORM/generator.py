from datetime import date, datetime

from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String

from gateways.database.ORM import Base


class GeneratorORM(Base):
    __tablename__ = "generator"
    # __table_args__ = {"schema": "flety"}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    nit = Column(String(20), nullable=False)
    legal_papers_ok = Column(Boolean, default=False)
    papers_expiration_date = Column(Date, default=date.fromisoformat("2100-01-01"))
    additional_info = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime)
