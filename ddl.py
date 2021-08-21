from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric, DateTime, PrimaryKeyConstraint, \
    UniqueConstraint, CheckConstraint, Index, ForeignKey, Boolean


def create_db():
    metadata = MetaData()
    cookies = Table('cookies', metadata,
                    Column('cookie_id', Integer(), primary_key=True),
                    Column('cookie_name', String(50), index=True),
                    Column('cookie_recipe_url', String(255)),
                    Column('cookie_sku', String(55)),
                    Column('quantity', Integer()),
                    Column('unit_cost', Numeric(12, 2)),
                    CheckConstraint('unit_cost >= 0.00', name='unit_cost_positive')
                    )

    orders = Table('orders', metadata,
                   Column('order_id', Integer(), primary_key=True),
                   Column('user_id', ForeignKey('users.user_id')),
                   Column('shipped', Boolean(), default=False),
                   )
    users = Table('users', metadata,
                  Column('user_id', Integer()),
                  Column('username', String(15), nullable=False, unique=True),
                  Column('email_address', String(255), nullable=False),
                  Column('phone', String(20), nullable=False),
                  Column('password', String(25), nullable=False),
                  Column('created_on', DateTime(), default=datetime.now),
                  Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now),
                  PrimaryKeyConstraint('user_id', name='user_pk'),
                  UniqueConstraint('username', name='uix_username'),
                  )

    line_items = Table('line_items', metadata,
                       Column('line_items_id', Integer(), primary_key=True),
                       Column('order_id', ForeignKey('orders.order_id')),
                       Column('cookie_id', ForeignKey('cookies.cookie_id')),
                       Column('quantity', Integer()),
                       Column('extended_cost', Numeric(12, 2)),
                       )
    Index('ix_cookies_cookie_name', 'cookies.cookie_sku', 'cookies.cookie_name'),
    # Index('ix_cookies_cookie_name', 'cookie_name'),
    engine = create_engine('postgresql://anpvnpeu:D_jQ-v2B_FdrgP6fY1BjtjpjVg-2K9De@chunee.db.elephantsql.com/anpvnpeu',
                           echo=True)
    metadata.create_all(engine)
    connection = engine.connect()
    return cookies, orders, users, line_items, connection
