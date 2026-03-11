from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


table_base = declarative_base()


class Modules(table_base):
    __tablename__ = 'modules'


    id = Column(Integer, primary_key=True, nullable=False)
    type = Column(Integer, nullable=False)
    # amount = Column(Integer, nullable=False)
    point = Column(Integer, ForeignKey('point.id'), nullable=False)

    module_point = relationship("Points", back_populates="point_module")


class Points(table_base):
    __tablename__= 'points'

    id = Column(Integer, primary_key=True, nullable=False)
    coord_x = Column(Integer, nullable=True)
    coord_y = Column(Integer, nullable=True)
    coord_z = Column(Integer, nullable=True)
    status = Column(Boolean, nullable=False, default=True)

    point_module = relationship("Modules", back_populates="module_point")