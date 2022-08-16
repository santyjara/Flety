from sqlalchemy import Column, Float, Integer, String

from gateways.database.ORM import Base


class VehicleTypeORM(Base):
    __tablename__ = "vehicle_type"
    # __table_args__ = {"schema": "flety"}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    n_shafts = Column(Integer, nullable=False)
    max_weight_kg = Column(Float, nullable=False)
    description = Column(String)
    image_path = Column(String(200))
