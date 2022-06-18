def orderlist(db_conn,curser,email,id):
    curser.execute("""select * from orderbill
                        where user_email = %s and user_id=%s""",[email,id])
    prod = curser.fetchall()
    if prod:
        print("\n*********preview about order details*********\n")
        print('order_id','order_date','user_id','user_email','shipping_address','prod_details','actual_price',
                            'discount_price','billing_price',sep='||')
        print()
        for i in prod:
            print(i,sep="||",end="\n\n")
        return True
    else:
        print('\n|---------------|')
        print("|not order items|")
        print('|---------------|\n')
        return False

def adminorderlist(db_conn,curser):
    curser.execute("""select * from orderbill""")
    prod = curser.fetchall()
    if prod:
        print("\n*********preview about order details*********\n")
        print('order_id','order_date','user_id','user_email','shipping_address','prod_details','actual_price',
                            'discount_price','billing_price',sep="||")
        for i in prod:
            print(i, sep="||",end="\n\n")
        return True
    else:
        print('\n|---------------|')
        print("|not order items|")
        print('|---------------|\n')

        return False