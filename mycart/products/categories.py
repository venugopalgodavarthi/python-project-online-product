import datetime

def listcategroy(db_conn,curser):
    curser.execute('select * from category')
    res=curser.fetchall()
    print("\n---list out the categories---\n")
    print('item id','----','  item name')
    print('-'*30)
    for i in res:
        print(i[0],'   ----   ',i[1])
    print('-'*30)

def category(db_conn,curser):
    print("\n------------Categories Menu----------------")
    n = int(input("1.create a categories\n2.read categories\n3.delete a categories\n4.Exit\nchoose your option:"))
    if n == 1:
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("------------Item Creating------------")
        tid = input("enter the item id:")
        tname = input("enter the item name:")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        n = int(input('1.Confirm\n2.Cancel\nChoose one option:'))
        if n == 1:
            curser.execute("insert into category (item_id, item_name) values (%s,%s)", [tid, tname])
            db_conn.commit()
            print('\n--------------------------------------')
            print("your category is created successfully ")
            print('--------------------------------------\n')

        return category(db_conn,curser)
        
    elif n == 2:
        print('----------------------------------------\n')
        print("-----------your category list-----------")
        curser.execute("select * from category")
        res = curser.fetchall()
        for i in res:
            print(i[0], i[1],end="\n\n")
        print('----------------------------------------\n')
        return category(db_conn,curser)

    elif n == 3:
        print('\n------------------------------------')
        tid = input("enter the item id:")
        print('------------------------------------\n')
        n = int(input('1.Confirm Delete\n2.Cancel\nChoose one option:'))
        if n == 1:
            curser.execute("delete from category where item_id = %s", [tid])
            db_conn.commit()
            print('\n------------------------------------')
            print("your category is deleted successfully ")
            print('------------------------------------\n')
        return category(db_conn,curser)
    else:
        return False


def product(db_conn,curser):
    print('\n"""""""""""""""""""""""""""""""""""""""""""""')
    n = int(input("1.create a product\n2.read product\n3.Modify a product\n4.delete a product\n5.Exit\nchoose your option:"))
    print('""""""""""""""""""""""""""""""""""""""""""""""\n')
   
    if n == 1:
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("----------------Product Creation-------------------")
        pid = input("enter the product id:")
        pname = input("enter the product name:")
        price = int(input("enter the product price:"))
        desc = input("enter the product desc:")
        itemid = input("enter the product itemid:")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        n = int(input('1.Confirm\n2.Cancel\nChoose one option:'))
        if n == 1:
            curser.execute("insert into product(p_id, p_name, price, description, item_id) values (%s,%s,%s,%s,%s)", [pid,pname,price,desc,itemid])
            db_conn.commit()
            print("\n-------------------------------------")
            print("your product is created successfully ")
            print("-------------------------------------\n")
        return product(db_conn,curser)
        
    elif n == 2:
        print("\n---------------------------------------------")
        print("--------------your product list----------------")
        curser.execute("select * from product")
        res = curser.fetchall()
        print(30*'-')
        print('productid','productname','price','description',sep='||')
        for i in res:
            print(i[0], i[1], i[2],i[3],sep="||")
        print("\n---------------------------------------------")
        return product(db_conn,curser)

    elif n == 3:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        print("--------------your product modification----------------")
        pid = input("enter the product id:")
        pname = input("enter the product name:")
        price = int(input("enter the product price:"))
        desc = input("enter the product desc:")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        n = int(input('1.Confirm\n2.Cancel\nChoose one option:'))
        if n == 1:
            curser.execute("update product set p_name=%s, price=%s, description=%s where p_id=%s", [pname,price,desc,pid])
            db_conn.commit()
            print("\n|----------------------------------------|")
            print("|your product is modification success      |")
            print("------------------------------------------\n|")

        else:
            return product(db_conn,curser)
        return product(db_conn,curser)

    elif n == 4:
        print("\n----------------------------------------------")
        print("--------------your product delete---------------")
        tid = input("enter the product id:")
        print("----------------------------------------------\n")

        n = int(input('1.Confirm Delete\n2.Cancel\nChoose one option:'))
        if n == 1:
            curser.execute("delete from product where p_id = %s", [tid])
            db_conn.commit()
            print("|-------------------------------------|")
            print("|your product is deleted successfully |")
            print("|-------------------------------------|")

        return product(db_conn,curser)
    else:
        return False



    



