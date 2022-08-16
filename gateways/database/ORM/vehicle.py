from datetime import date

from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from gateways.database.ORM import Base


class VehicleORM(Base):
    __tablename__ = "vehicle"
    # __table_args__ = {"schema": "flety"}

    id = Column(Integer, primary_key=True)
    model_name = Column(String(100), nullable=False)
    brand = Column(
        Enum(
            "Kenworth",
            "International Eagle",
            name="brand",
        ),
        nullable=False,
    )
    vehicle_type_id = Column(Integer, ForeignKey("vehicle_type.id"), nullable=False)
    vehicle_type = relationship(
        "VehicleTypeORM", cascade="save-update, merge, delete", passive_deletes=False
    )
    driver_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    driver = relationship(
        "UserORM", backref="driver_vehicles", foreign_keys=[driver_id]
    )
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("UserORM", backref="owner_vehicles", foreign_keys=[owner_id])
    model_year = Column(Integer, nullable=False)
    license_plate = Column(String(10), nullable=False)
    soat_expiration_date = Column(Date, default=date.fromisoformat("2100-01-01"))
    color = Column(String(20))
    image_path = Column(String(200))
