from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, desc, func, Column, Integer, String, CheckConstraint, DateTime
from datetime import datetime

Base = declarative_base()
engine = create_engine("sqlite:///migrations_test.db")

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    email = Column(String(), unique = True)
    grade = Column(Integer(), CheckConstraint("grade BETWEEN 1 AND 2"))
    birthday = Column(DateTime())
    date_joined = Column(DateTime(), default = datetime.now())
    guardian_name = Column(String())
    guardian_phone = Column(Integer())
    def __repr__(self):
        return f"Student {self.id} : {self.name} : Grade {self.grade}"
