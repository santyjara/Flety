from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String

from gateways.database.ORM import Base


class SubscriptionPlanORM(Base):
    __tablename__ = "subscription_plan"
    # __table_args__ = {"schema": "flety"}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    monthly_cost_COP = Column(Float, nullable=False)
    # if -1 loads per month = inf
    loads_per_month = Column(Integer)
    includes_analytics_module = Column(Boolean, default=False)
    includes_tracking_module = Column(Boolean, default=False)
    description = Column(String)
    benefits = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime)
