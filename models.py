import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import psycopg2

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    def __str__(self):
        return f'name: {self.name}'

class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40))
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    publisher = relationship(Publisher, backref='book')
    def __str__(self):
        return f'title: {self.title}, id_p: {self.id_publisher}'


class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)


class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    book = relationship(Book, backref='book')
    shop = relationship(Shop, backref='shop')
    count = sq.Column(sq.Integer)


class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.FLOAT, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    stock = relationship(Stock, backref='stock')
    count = sq.Column(sq.Integer)


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
