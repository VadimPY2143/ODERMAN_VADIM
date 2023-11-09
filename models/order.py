from __future__ import annotations
from typing import List, Optional

from sqlalchemy import ForeignKey,String

from  sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .associates import student_group_assoc_table
from .group import Group

class Order(Base):
    __tablename__ = "order"

    pizza_count: Mapped[int] = mapped_column()
    phone_number: Mapped[int] = mapped_column()
    delivery_adress: Mapped[Optional[str]]
    pizza_name: Mapped[str] = mapped_column(String(50))
    delivery_adress: Mapped[str] = mapped_column(String(250))
    groups: Mapped[List[Group]] = relationship(secondary=student_group_assoc_table)

    def __str__(self) -> str:
        return f''
