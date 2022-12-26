from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship

from crm_app.database import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    date_create = Column(DATETIME)
    company_id = Column(Integer)