import sqlite3

CREATE_USERS_TABLE = 'CREATE TABLE IF NOT EXISTS users (user_id TEXT PRIMARY KEY, password TEXT, name TEXT, email TEXT, address TEXT,' \
                     ' phoneno INTEGER, credit_card_info TEXT, shipping_info TEXT);'
CREATE_PRODUCTS_TABLE = 'CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, name TEXT, description TEXT,' \
                        ' price INTEGER, image_file_name TEXT, category TEXT);'
CREATE_CATEGORY_TABLE = 'CREATE TABLE IF NOT EXISTS category (category_id INTEGER PRIMARY KEY, department_id TEXT, category_name TEXT, description TEXT);'
# CREATE_ORDER_DETAIL_TABLE = 'CREATE TABLE IF NOT EXISTS order_detail (order_id INTEGER PRIMARY KEY, FOREIGN KEY(product_id) REFERENCES products (product_id),' \
#                             ' FOREIGN KEY (name) REFERENCES products (name), quantity INTEGER, unit_cost FLOAT, sub_total FLOAT);'
# CREATE_SHIPPING_INFO_TABLE = 'CREATE TABLE IF NOT EXISTS shipping_info (shipping_id INTEGER PRIMARY KEY, shipping_type TEXT, shipping_cost INTEGER, shipping_region_id INTEGER);'
# CREATE_ORDERS_TABLE = 'CREATE TABLE IF NOT EXISTS orders (FOREIGN KEY (order_id) REFERENCES order_details (order_id), data_created TEXT, data_shipped TEXT, customer_name TEXT,' \
#                       ' customer_id TEXT, status TEXT, FOREIGN KEY shipping_id REFERENCES shipping_info (shipping_id));'

INSERT_USER = 'INSERT INTO users (user_id, password) VALUES (?, ?);'
GET_ALL_USERS = 'SELECT * FROM users;'
GET_ALL_PRODUCTS = 'SELECT * FROM products;'

GET_USER = 'SELECT * FROM users WHERE user_id = (?);'


def connect():
    return sqlite3.connect('data.db')


def create_tables(connection):
    with connection:
        connection.execute('PRAGMA foreign_keys = ON;')
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_PRODUCTS_TABLE)
        # connection.execute(CREATE_CATEGORY_TABLE)
        # connection.execute(CREATE_ORDER_DETAIL_TABLE)
        # connection.execute(CREATE_SHIPPING_INFO_TABLE)
        # connection.execute(CREATE_ORDERS_TABLE)
        connection.commit()


def add_user(connection, user_id, password):
    with connection:
        connection.execute(INSERT_USER, (user_id, password))
        connection.commit()


def get_all_users(connection):
    with connection:
        return connection.execute(GET_ALL_USERS).fetchall()


def get_user(connection, user_id):
    with connection:
        return connection.execute(GET_USER, user_id).fetchall()
