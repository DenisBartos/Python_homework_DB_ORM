from db_connect import DB
from tables import Publisher, Book, Sale, Stock, Shop, create_tables
from inserts import insert_data_into_tables

session = DB.session


def check_user_input(user_input):
    publisher_ids = list(map(lambda x: str(x[0]), session.query(Publisher.id).all()))
    publisher_names = list(map(lambda x: x[0], session.query(Publisher.name).all()))
    if user_input in publisher_ids:
        return Publisher.id
    elif user_input.title() in publisher_names:
        return Publisher.name
    else:
        return False


def get_books_by_publisher(publisher):
    query_param = check_user_input(publisher)
    if not query_param:
        print('unable to find publisher by your request')
        return
    else:
        query = session.query(Book.title, Shop.name, Sale.price, Sale.count).join(Publisher, Stock, Shop, Sale).filter(
            query_param == publisher.title()).order_by(Book.title).all()
        print(session.query(Publisher.name).filter(query_param == publisher.title()).first()[0])
        for book, shop, price, count in query:
            print(f'the book {book} is available in {shop} in quantity {count} for the price of {price}')
        return query


if __name__ == '__main__':
    create_tables()
    insert_data_into_tables()

    while True:
        command = input('input publisher id or name: ').strip()
        if command == 'break':
            break
        else:
            get_books_by_publisher(command)
