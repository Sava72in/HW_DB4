import json
from pprint import pprint

import sqlalchemy
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
import psycopg2
from models import *

DSN = "postgresql://postgres:postgres@localhost:5432/netology_db"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
con = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
with open('./tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()
session.close()
find = input("Введите имя издателя : ")
q = """select b.title , s3."name" ,s.price ,s.date_sale 
from sale s 
join stock s2 on s.id_stock = s2.id 
join shop s3 on s2.id_shop = s3.id 
join book b on s2.id_book = b.id 
join publisher p on b.id_publisher =p.id 
where p.name = '{}' ; """.format(find)
for i in con.execute(text(q)).fetchall():
    print(f'{i[0]} | {i[1]} | {i[2]} | {i[3]}')

# O’Reilly