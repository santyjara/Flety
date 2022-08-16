from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from gateways.database.ORM import Base


class LoadORM(Base):
    __tablename__ = "load"
    # __table_args__ = {"schema": "flety"}

    id = Column(Integer, primary_key=True, index=True)
    assigned_generator_id = Column(Integer, ForeignKey("generator.id"))
    assigned_generator = relationship("GeneratorORM", backref="loads")
    pick_up_date = Column(DateTime(timezone=True), nullable=False)
    origin_city = Column(String(50), index=True, nullable=False)
    origin_address_id = Column(Integer, ForeignKey("address.id"))
    origin_address = relationship("AddressORM", foreign_keys=[origin_address_id])
    destiny_city = Column(String(50), index=True, nullable=False)
    destiny_address_id = Column(Integer, ForeignKey("address.id"))
    destiny_address = relationship("AddressORM", foreign_keys=[destiny_address_id])
    contact_id = Column(Integer, ForeignKey("contact.id"))
    contact = relationship("ContactORM")
    product_type = Column(String(50), nullable=False)
    requirements = Column(String)
    vehicle_type_id = Column(Integer, ForeignKey("vehicle_type.id"))
    vehicle_type = relationship("VehicleTypeORM")
    load_type = Column(
        Enum(
            "combustible",
            "big bags",
            name="load_type",
        ),
        nullable=False,
    )
    trailer_type = Column(
        Enum(
            "furgón",
            "estacas",
            name="trailer_type",
        ),
        nullable=False,
    )
    weight_kg = Column(Float)
    includes_loading = Column(Boolean, default=False, nullable=False)
    loading_cost = Column(Float)
    includes_unloading = Column(Boolean, default=False, nullable=False)
    unloading_cost = Column(Float)
    status = Column(String(20), default="pending", nullable=False)
    assigned_vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
    assigned_vehicle = relationship("VehicleORM", backref="loads")
    assigned_company_id = Column(Integer, ForeignKey("transport_company.id"))
    assigned_company = relationship("TransportCompanyORM", backref="loads")
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime)
