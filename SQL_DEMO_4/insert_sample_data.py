from sqlalchemy import text, insert
from db_session import engine, Session


# from models import Base, Author, Genre, Book
#
#
def insert_sample_data():
    # создаём таблицы, если их нет (безопасно)
    models.Base.metadata.create_all(engine)
    with Session() as session:
        # создадим авторов и жанры
        authors = [
            Author(name='Достоевский Ф. М.'),
            Author(name='Толстой Л. Н.'),
            Author(name='Булгаков М. А.'),
            Author(name='Оруэлл Дж.'),
            Author(name='Хемингуэй Э.')
        ]
        genres = [
            Genre(name='Роман'),
            Genre(name='Фантастика'),
            Genre(name='Драма'),
            Genre(name='Исторический'),
            Genre(name='Сатира')
        ]
        session.add_all(authors + genres)
        session.commit()  # фиксация чтобы появились id

        # теперь можем добавить книги, используя присвоенные id
        # (или связать через объекты authors[0], genres[0])
        books = [
            Book(title='Преступление и наказание', author_id=authors[0].id, genre_id=genres[0].id, published_year=1866),
            Book(title='Братья Карамазовы', author_id=authors[0].id, genre_id=genres[0].id, published_year=1880),
            Book(title='Война и мир', author_id=authors[1].id, genre_id=genres[3].id, published_year=1869),
            Book(title='Анна Каренина', author_id=authors[1].id, genre_id=genres[0].id, published_year=1877),
            Book(title='Мастер и Маргарита', author_id=authors[2].id, genre_id=genres[4].id, published_year=1967),
            Book(title='Собачье сердце', author_id=authors[2].id, genre_id=genres[4].id, published_year=1925),
            Book(title='1984', author_id=authors[3].id, genre_id=genres[1].id, published_year=1949),
            Book(title='По ком звонит колокол', author_id=authors[4].id, genre_id=genres[2].id, published_year=1940)
        ]
        session.add_all(books)
        session.commit()

# if __name__ == '__main__':
#     insert_sample_data()



import models
from models import metadata_obj, workers_table


def create_tables():
    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine)

create_tables()



def insert_data():
    with engine.connect() as conn:

        #"Это первый не самый удобный способ
        # stmt = """INSERT INTO workers (username) VALUES
        #         ('AO Bobr'),
        #         ('OOO Volk');"""
        #"Это через куэри билдер
        stmt  = insert(workers_table).values(
            [
                {'id': 1, 'username': 'alpon1'},
                {'id': 2, 'username': 'alpon2'},
            ]
        )



        conn.execute(stmt)
        conn.commit()

insert_data()
