import datetime
def cartlist(db_conn,curser,email):
    curser.execute("""select cart.cart_id, category.item_name, product.p_id, product.p_name,
                        product.price, product.description
                        from ((cart  inner join product  on cart.prod_id = product.p_id)
                        inner join category on cart.item_id = category.item_id)
                        where cart.user_email = %s""",[email])
    prod = curser.fetchall()
    if prod:
        print("item name","product id",'product name','price','descriptiom')
        for i in prod:
            print(i,end="\n\n")
        return True
    else:
        print('\n|---------------|')
        print("|not cart items|")
        print('|---------------|\n')
        return False

def cartdelete(db_conn,curser,email,choose):
    curser.execute("""delete from cart where user_email = %s and cart_id = %s""",[email,choose])
    db_conn.commit()
    return curser.rowcount


def addressbill():
    print("\n``````````````````````````````")
    print("**plz fill the shipping address**\n")
    D_no=input("door no*:")
    street=input("street name*:")
    city=input("city name*:")
    state=input("state name*:")
    country=input("country name*:")
    pincode=input("pincode name*:")
    phone=input("phone name*:")
    print("``````````````````````````````\n")
    return '-'.join([D_no,street,city,street,city,state,country,pincode,phone])

def cartbuying(db_conn,curser,email,id):
    curser.execute("""select category.item_name, product.p_id, product.p_name,
                        product.price
                        from ((cart  inner join product  on cart.prod_id = product.p_id)
                        inner join category on cart.item_id = category.item_id)
                        where cart.user_email = %s""",[email])
    prod = curser.fetchall()
    curser.execute("""select sum(price) from cart where user_email = %s""",[email])
    cost = list(curser.fetchone())
    cost=int(cost[0])
    print("item name","product id",'product name','price','description')
    pid=['***'.join([i[1],i[2],str(i[3])]) for i in prod]
    if prod:
        for i in prod:
            print(i,end="\n\n")
        print("total actual amount is",cost)
        discount=0
        final=cost
        if cost>10000:
            discount=500
            print("discount amount is:   -",discount)
            final-=discount
            print("total billing ammount is:",final)
        else:
            print(" no discount amount is -",discount)
            print("total billing amount is:",final)
        var=[str(datetime.date.today()),id,email,addressbill(), '\n'.join(pid),cost,discount,final]
        z = int(input('1.Confirm buying \n2.Cancel\nChoose one option:'))
        if z == 1:
            print("\n----------------------------")
            print("preview about buying details\n",var,sep='\n')
            print("\n----------------------------")
            t = int(input('1.Confirm \n2.Cancel\nChoose one option:'))
            if t == 1:
                curser.execute("""insert into orderbill (
                order_date, user_id, user_email, shipping_address, prod_details,
                actual_price,discount_price,billing_price)
                values(%s,%s,%s,%s,%s,%s,%s,%s)""",var)
                db_conn.commit()
                print("your buying items orderd")
                return True
            else:
                return False
        else:
            return False
    else:
        print('\n|---------------|')
        print("|not cart items|")
        print('|---------------|\n')
        return False

def deletecart(db_conn,curser,email,id):
    curser.execute("delete from cart where user_email=%s and user_id=%s",[email,id])
    db_conn.commit()
