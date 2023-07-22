import json

from db_connect import DB
from tables import Publisher, Book, Sale, Stock, Shop

session = DB.session


def insert_data_into_tables():
    with open("test_data.json", 'r') as f:
        data = json.load(f)

    publishers = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'publisher')
    books = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'book')
    shops = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'shop')
    stocks = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'stock')
    sales = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'sale')

    for publisher in publishers:
        add_record = Publisher(id=publisher['id'],
                               name=publisher['fields']['name']
                               )
        session.add(add_record)
        session.commit()

    for book in books:
        add_record = Book(id=book['id'],
                          title=book['fields']['title'],
                          id_publisher=book['fields']['publisher']
                          )
        session.add(add_record)
        session.commit()

    for shop in shops:
        add_record = Shop(id=shop['id'],
                          name=shop['fields']['name']
                          )
        session.add(add_record)
        session.commit()

    for stock in stocks:
        add_record = Stock(id=stock['id'],
                           id_book=stock['fields']['book'],
                           id_shop=stock['fields']['shop'],
                           count=stock['fields']['count']
                           )
        session.add(add_record)
        session.commit()

    for sale in sales:
        add_record = Sale(id=sale['id'],
                          price=sale['fields']['price'],
                          date_sale=sale['fields']['date_sale'],
                          id_stock=sale['fields']['stock'],
                          count=sale['fields']['count']
                          )
        session.add(add_record)
        session.commit()
