from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase

class Base(DeclarativeBase):
    pass

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

from sqlalchemy import Table, Column, Integer, String, MetaData
metadata_obj = MetaData()
workers_table = Table(
    'workers',
       metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String)
)