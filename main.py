import sqlalchemy
from sqlalchemy.orm import sessionmaker
import psycopg2
from models import create_tables, Publisher, Book, Stock, Sale, Shop

DSN = "postgresql://postgres:postgres@localhost:5432/netology_db"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# publisher1 = Publisher(name='Пушкин')
# book1 = Book(title='Капитанская дочка', id_publisher=1)
# shop1 = Shop(name='Буквоед')
# stock1 = Stock(id_book=1, id_shop=1, count=2)
# session.add_all()
session.commit()

session.close()