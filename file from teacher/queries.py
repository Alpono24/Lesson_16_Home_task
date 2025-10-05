from operator import and_

from sqlalchemy import select, func
from sqlalchemy.orm import joinedload

from db_session import Session
from models import Author, Book, Genre


def run_queries():
    with Session() as session:
        # 1. Все авторы
        print("=== Авторы ===")
        authors = session.scalars(select(Author)).all()
        for a in authors:
            print(a.id, a.name)

        # 2. Все жанры
        print("\n=== Жанры ===")
        genres = session.scalars(select(Genre)).all()
        for g in genres:
            print(g.id, g.name)

        # 3. Книги с авторами и жанрами (JOIN)
        print("\n=== Книги с авторами и жанрами ===")
        stmt = (
            select(Book.title, Author.name, Genre.name)
            .join(Author, Book.author_id == Author.id)
            .join(Genre, Book.genre_id == Genre.id)
        )
        for row in session.execute(stmt):
            print(row)

        # 4. Количество книг у каждого автора (GROUP BY)
        print("\n=== Количество книг по авторам ===")
        stmt = (
            select(Author.name, func.count(Book.id).label('book_count'))
            .join(Author.books)
            .group_by(Author.id, Author.name)
        )

        for author_name, book_count in session.execute(stmt):
            print(f"{author_name}: {book_count} книг(и)")
        # 5. Книги определенного жанра (WHERE)
        print("\n=== Книги в жанре 'Фантастика' ===")
        stmt = (
            select(Book.title, Author.name)
            .join(Author)
            .join(Genre)
            .where(Genre.name == "Фантастика")
        )
        for title, author in session.execute(stmt):
            print(f"'{title}' - {author}")
        # 6. Авторы с количеством книг больше 1 (HAVING)
        print("\n=== Авторы с более чем 1 книгой ===")
        stmt = (
            select(Author.name, func.count(Book.id).label('book_count'))
            .join(Author.books)
            .group_by(Author.id, Author.name)
            .having(func.count(Book.id) > 1)
        )
        for author_name, book_count in session.execute(stmt):
            print(f"{author_name}: {book_count} книг(и)")
        # 7. Книги, изданные после 2000 года (фильтрация по году)
        print("\n=== Книги после 2000 года ===")
        stmt = (
            select(Book.title, Author.name, Book.published_year)
            .join(Author)
            .where(Book.published_year > 2000)
            .order_by(Book.published_year)
        )
        for title, author, year in session.execute(stmt):
            print(f"{year}: '{title}' - {author}")
        # 8. Жанры с количеством книг (сортировка по популярности)
        print("\n=== Жанры по популярности ===")
        stmt = (
            select(Genre.name, func.count(Book.id).label('book_count'))
            .join(Genre.books)
            .group_by(Genre.id, Genre.name)
            .order_by(func.count(Book.id).desc())
        )
        for genre_name, book_count in session.execute(stmt):
            print(f"{genre_name}: {book_count} книг(и)")
        # 9. Загрузка связанных объектов через joinedload (eager loading)
        print("\n=== Все книги с авторами и жанрами (joinedload) ===")
        stmt = select(Book).options(
            joinedload(Book.author),
            joinedload(Book.genre)
        )
        books = session.scalars(stmt).unique().all()
        for book in books:
            print(f"'{book.title}' - {book.author.name} ({book.genre.name})")
        # 10. Поиск книг по названию (LIKE)
        print("\n=== Книги с 'война' в названии ===")
        stmt = (
            select(Book.title, Author.name)
            .join(Author)
            .where(Book.title.ilike("%война%"))
        )
        for title, author in session.execute(stmt):
            print(f"'{title}' - {author}")
        # 11. Комплексный запрос с несколькими условиями
        print("\n=== Фантастика после 2010 года ===")
        stmt = (
            select(Book.title, Author.name, Book.published_year)
            .join(Author)
            .join(Genre)
            .where(and_(
                Genre.name == "Фантастика",
                Book.published_year > 2010
            ))
            .order_by(Book.published_year.desc())
        )
        for title, author, year in session.execute(stmt):
            print(f"{year}: '{title}' - {author}")



if __name__ == "__main__":
    run_queries()