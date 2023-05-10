import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from src.database import Base


class Defection(Base):
    __tablename__ = "defection"

    id = Column(Integer, primary_key=True)
    defection_time = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
    reason = Column(String(300), nullable=False)
    defection_type_id = Column(Integer, ForeignKey("defectiontype.id"), nullable=False)


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey("group.id"), nullable=False)


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    letter = Column(String(1), nullable=False)


class DefectionType(Base):
    __tablename__ = "defectiontype"

    id = Column(Integer, primary_key=True)
    defection_type = Column(String(150), nullable=False)
