alter table books
drop constraint books_author_id_fkey;

alter table books
add constraint books_author_id_fkey
foreign key (author_id)references authors(id) on delete cascade;

select title, published_year from books
where author_id = 2

- все где есть иииии))))
select title, published_year from books
where title ilike '%и%';



select b.title, a.name as author, g.name as genre
from books b
join authors a on b.author_id = a.id
join genres g on b.genre_id  = g.id;



select a.name, count(b.id)as books_count
from authors a
left join books b on a.id = b.author_id 
group by a.id;

insert into authors (name) values ('Пушкин А.С.')


insert into genres (name) values ('Поэзия');

insert into books (title, author_id, genre_id, published_year)
values ('Евгений Онегин', 6 , 6, 1833);


delete FROM authors 
WHERE id = 6;








pip install "SQLAlchemy>=2.0" alembic psycopg2-binary








#Запустить код
import os
from sqlalchemy import create_engine, text


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/library_db")
engine = create_engine(DATABASE_URL, echo=True)

with engine.connect() as conn:
    print("connected:", conn.execute(text("SELECT 1")).scalar())




#Запустить код
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase

class Base(DeclarativeBase):
    pass



alembic init migrations