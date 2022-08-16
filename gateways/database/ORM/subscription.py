from datetime import date

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from gateways.database.ORM import Base


class SubscriptionORM(Base):
    __tablename__ = "subscription"
    # __table_args__ = {"schema": "flety"}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    subscription_plan_id = Column(Integer, ForeignKey("subscription_plan.id"))
    subscription_plan = relationship("SubscriptionPlanORM")
    subscription_start_date = Column(Date, default=str(date.today()), nullable=False)
    subscription_end_date = Column(Date, nullable=False)
    updated_at = Column(DateTime)
