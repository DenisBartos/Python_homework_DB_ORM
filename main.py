import sqlalchemy
from sqlalchemy.orm import sessionmaker
import json

from models import create_tables, Publisher, Sale, Book, Stock, Shop

SQLsystem = 'postgresql'
login = 'Denis2000gos'
password = 'Denis2000gos'
host = 'localhost'
port = 5432
db_name = '2'
DSN = f'{SQLsystem}://{login}:{password}@{host}:{port}/{db_name}'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)


def publ_name_():
    with open('tests_data.json', 'r') as db:
        data = json.load(db)

    for line in data:
        method = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[line['model']]
        session.add(method(id=line['pk'], **line.get('fields')))

    session.commit()

    publ_name = input('Ведите имя писателя или id для вывода: ')
    if publ_name.isnumeric():
        for c in session.query(Publisher).filter(
                Publisher.id == int(publ_name)).all():
            print(c)
    else:
        for c in session.query(Publisher).filter(
                Publisher.name.like(f'%{publ_name}%')).all():
            print(c)


if __name__ == '__main__':
    publ_name_()
    session.close()
