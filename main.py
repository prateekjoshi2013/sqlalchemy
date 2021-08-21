from sqlalchemy import select, desc, func

from ddl import create_db


def main():
    (cookies, orders, users, line_items, conn) = create_db()
    # inserts(cookies, orders, users, line_items, conn)
    s = select([cookies])
    rp = conn.execute(s)
    results = rp.fetchall()
    print(results)

    s = cookies.select()
    rp = conn.execute(s)
    # print(results.first())
    # print(results.fetchone())
    results = rp.fetchall()
    print(results)
    first_row = results[0]
    first_row[1]
    print(first_row)
    print(first_row[1])
    print(first_row.cookie_name)
    print(first_row[cookies.c.cookie_name])
    for rec in results:
        print('-->', rec)
    # print(results.scalar())
    s = select([cookies.c.cookie_name, cookies.c.quantity])
    rp = conn.execute(s)
    print(rp.keys())
    result = rp.first()
    print(result)

    ####-ORDERING

    s = select([cookies.c.cookie_name, cookies.c.quantity])
    s = s.order_by(desc(cookies.c.quantity))
    rp = conn.execute(s)
    for cookie in rp:
        print(f'{cookie.quantity} - {cookie.cookie_name}')

    ## limit the query

    s = select([cookies.c.cookie_name, cookies.c.quantity])
    s = s.order_by(cookies.c.quantity)
    s = s.limit(2)
    rp = conn.execute(s)
    print([result.cookie_name for result in rp])

    ### AGGREGATE FUNCTIONS
    ### SUM
    s=select([func.sum(cookies.c.quantity)])
    rp=conn.execute(s)
    print(rp.scalar())

    ### COUNT
    s=select([func.count(cookies.c.cookie_name)])
    rp=conn.execute(s)
    record=rp.first()
    print(record.keys())
    print(record.count_1)

    ### RENAMING COLUMN COUNT

    s=select([func.count(cookies.c.cookie_name).label('inventory_count')])
    rp=conn.execute(s)
    record=rp.first()
    print(record.keys())
    print(record.inventory_count)




if __name__ == '__main__':
    main()
