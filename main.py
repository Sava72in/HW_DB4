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
find = input("Введите имя издателя или id: ")
q = """select b.title ,s2."name" ,s3.price ,s3.date_sale 
from publisher p 
left join book b on p.id = b.id_publisher 
left join stock s on b.id = s.id_book 
left join shop s2 on s.id_shop = s.id 
left join sale s3 on s3.id_stock = s2.id 
where p.name = '{}' and s3.date_sale notnull; """.format(find)
for i in con.execute(text(q)).fetchall():
    print(f'{i[0]} | {i[1]} | {i[2]} | {i[3]}')

# O’Reilly