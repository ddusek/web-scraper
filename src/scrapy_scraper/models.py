from typing_extensions import Required
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Flat(Base):
    __tablename__ = "flat"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120), nullable=False)
    image: Mapped[str] = mapped_column(String(250), nullable=False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
