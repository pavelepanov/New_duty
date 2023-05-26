from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from database import Base


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey("grade.id"), nullable=False)


class Grade(Base):
    __tablename__ = "grade"

    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    letter = Column(String(1), nullable=False)
