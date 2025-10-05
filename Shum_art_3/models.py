#
# from sqlalchemy import Integer, String, Column, ForeignKey
# from sqlalchemy.orm import relationship, DeclarativeBase
#
#
# class Base(DeclarativeBase):
#     pass
#
# class Base(DeclarativeBase):
#     pass
#
class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    books = relationship("Book", back_populates="author")

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    books = relationship("Book", back_populates="genre")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"))
    genre_id = Column(Integer, ForeignKey("genres.id", ondelete="CASCADE"))
    published_year = Column(Integer, nullable=True)

    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")
#
#
#
# #_________________________________________________________________________
#
from sqlalchemy import Table, Column, Integer, String, MetaData
metadata_obj = MetaData()

workers_table = Table(
    'workers',
       metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String)
)
from datetime import datetime

#_____________________________________________________________________________1111111111
#Занятие 3 Шумейко
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from xmlrpc.client import DateTime

metadata_obj = MetaData()
#
# workers_table = Table(
#     'workers',
#        metadata_obj,
#     Column('id', Integer, primary_key=True),
#     Column('username', String)
# )

from sqlalchemy.orm import DeclarativeBase
import enum

class Base(DeclarativeBase):
    pass

class Worker(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)

#_____________________________________________________________________________1111111111
# class Workload(enum.Enum):
#     parttime = "parttime"
#     fulltime = "fulltime"

class ResumeORM(Base):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True)
    resume_id = Column(String(100), nullable=False)
    compensation = Column(Integer, nullable=True )
    # workload = Column(enum.Enum(Workload), nullable=False)
    worker_id = Column(Integer, ForeignKey("workers.id", ondelete="CASCADE"))

