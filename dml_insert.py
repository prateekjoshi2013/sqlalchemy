from sqlalchemy import insert


def inserts(cookies, orders, users, line_items, conn):
    ins = cookies.insert().values(
        cookie_name='chocolate chip',
        cookie_recipe_url='http://some.awe.me/cookie/recipe.html',
        cookie_sku='CC01',
        quantity='12',
        unit_cost='0.50'
    )
    compiled_params = ins.compile().params
    result = conn.execute(ins)
    ins_prim_key = result.inserted_primary_key

    print(str(ins))

    ins = insert(cookies).values(
        cookie_name='chocolate chip',
        cookie_recipe_url='http://some.awe.me/cookie/recipe.html',
        cookie_sku='CC01',
        quantity='12',
        unit_cost='0.50'
    )

    ins = cookies.insert()
    result = conn.execute(ins, cookie_name='chocolate chip',
                          cookie_recipe_url='http://some.awe.me/cookie/recipe.html',
                          cookie_sku='CC01',
                          quantity='12',
                          unit_cost='0.50')
    ## bulk inserts
    inventory_list = [
        {
            'cookie_name': 'peanut butter',
            'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
            'cookie_sku': 'PB01',
            'quantity': '24',
            'unit_cost': '0.25'
        },
        {
            'cookie_name': 'oatmeal raisin',
            'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
            'cookie_sku': 'EWW01',
            'quantity': '100',
            'unit_cost': '1.00'
        }
    ]
    result = conn.execute(ins, inventory_list)
