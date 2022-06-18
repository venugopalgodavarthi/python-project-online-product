from dbconnect.dbconnection import db_conn, curser
from products.categories import category,product,listcategroy
from products.cartdetails import cartbuying,cartdelete,cartlist,deletecart
from products.userdomain import userdetails,usercreate
from products.orderdetails import orderlist,adminorderlist

def print_hi():
    print("*"*30)
    print("welcome to my cart")
    print("*"*30)

def register():
    name = input("enter the name:")
    email = input("enter the email:")
    phone = int(input("enter the phone:"))
    address = input("enter the address:")
    password = input("enter the password:")
    re_password = input("enter the re_password:")
    if password == re_password:
        return [name, email, phone, address, password]


def adminwelcome():
    n = int(input("1.categories\n2.product\n3.order\n4.exit\nchoose your option:"))
    if n == 1:
        if category(db_conn,curser):
            pass
        else:
            adminwelcome()
    elif n == 2:
        if product(db_conn,curser):
            pass
        else:
            adminwelcome()
    elif n == 3:
        res=adminorderlist(db_conn,curser)
        if res:
            m=int(input("1.go to main menu\n2.Exit\nchoose your option:"))
            if m==1:
                return adminwelcome()
            else:
                print("Thank you admin")
    else:
        print("exit")
        print("Thank you admin")

class user:
    def __init__(self,id,email):
        self.id = id
        self.email= email

    def productdetails(self,curser,n):
        res = curser.execute("select * from product where item_id=%s",[n])
        res=curser.fetchall()
        print("\n---list out the products---\n")
        print('product id','product name','price','description')
        print('-'*30)
        for i in res:
            print(i[0],i[1],i[2],i[3])
        print('-'*30)

    def userwelcome(self,db_conn,curser):
        print("\n ----- Main Menu -----\n")
        n = int(input("1.categories\n2.cart\n3.order\n4.profile\n5.logout\nchoose your option:"))
        if n == 1:
            listcategroy(db_conn,curser)
            itemid = input("Enter the Item ID:").upper()
            self.productdetails(curser,itemid)
            m=int(input("1.go back\n2.add a product to cart\n3.Exit\nchoose your option:"))
            if m==1:
                self.userwelcome(db_conn,curser)
            elif m==2:
                print("\n--------------------------")
                print("add the product into cart:")
                print("--------------------------\n")
                prodid = input("Enter the product ID:").upper()
                curser.execute('select * from product where p_id = %s',[prodid])
                temp=curser.fetchone()
                print(temp)
                t = int(input('\n1.Confirm \n2.Cancel\nChoose one option:'))
                if t == 1:
                    res=[self.id,self.email,itemid,temp[0],temp[2]]
                    print(res)
                    curser.execute("insert into cart (user_id,user_email,item_id,prod_id,price) values (%s,%s,%s,%s,%s)", res)
                    db_conn.commit()
                    print("-----------------------------")
                    print("your product is added to cart")
                    print("-----------------------------")
                    return self.userwelcome(db_conn,curser)
                else:
                    return self.userwelcome(db_conn,curser)
            else:
                print('thank you visiting')
        elif n == 2:
                check=cartlist(db_conn,curser,self.email)
                if check:
                    m=int(input("1.delete cart item\n2.buying\n3.go to order\n4.Exit\nchoose your option:"))
                    if m==1:
                        temp=int(input("enter the cart number:"))
                        res=cartdelete(db_conn,curser,self.email,temp)
                        if res is not None:
                            print("\n-----------------------")
                            print("your cart item is deleted")
                            print("--------------------------\n")
                        cartlist(db_conn,curser,self.email)
                        return self.userwelcome(db_conn,curser)
                    elif m==2:
                        cartcheck=cartbuying(db_conn,curser,self.email,self.id)
                        if cartcheck:
                            deletecart(db_conn,curser,self.email,self.id)
                            return self.userwelcome(db_conn,curser)
                        else:
                            return self.userwelcome(db_conn,curser)
                    elif m==3:
                        res=orderlist(db_conn,curser,self.email,self.id)
                        if res:
                            m=int(input("\n1.go to main menu\n2.Exit\nchoose your option:"))
                            if m==1:
                                self.userwelcome(db_conn,curser)
                            else:
                                self.userwelcome(db_conn,curser)
                        else:
                            self.userwelcome(db_conn,curser)
                    else:
                        self.userwelcome(db_conn,curser)
                else:
                    return self.userwelcome(db_conn,curser)
                    
        elif n == 3:
            res=orderlist(db_conn,curser,self.email,self.id)
            if res:
                m=int(input("\n1.go to main menu\n2.Exit\nchoose your option:"))
                if m==1:
                    self.userwelcome(db_conn,curser)
                else:
                    self.userwelcome(db_conn,curser)
            else:
                self.userwelcome(db_conn,curser)
        elif n == 4:
            res=userdetails(db_conn,curser,self.email,self.id)
            if res:
                m=int(input("1.go to main menu\n2.logout\n3.exit\nchoose your option:"))
                if m==1:
                    self.userwelcome(db_conn,curser)
                elif m==2:
                    print("Thank you for visiting")
                else:
                    self.userwelcome(db_conn,curser)
            else:
                self.userwelcome(db_conn,curser)
        else:
            return main()


def login(curser):
    print("\n --------login--------\n ")
    user = input("enter the email id:")
    password = input("enter the password:")
    curser.execute("select * from register where email=%s and password=%s", [user, password])
    res = curser.fetchone()
    if res:
        return res



def main():
    n = int(input('1.Register\n2.login\n3.exit\n Choose one option:'))
    print("+"*30)
    if n == 1:
        res=register()
        print(30*'-')
        n = int(input('\n1.Confirm\n2.Cancel\nChoose one option:'))
        if n == 1:
            if usercreate(db_conn,curser,res):
                print("\n**your registration is success**\n")
                return main()
        else:
            return main()
    elif n == 2:
        try:
            res = login(curser)
            if res[-1] == 'admin':
                print("your admin login is success")
                print("Welcome to my cart Mr.{}".format(res[1].title()))
                print("\n ------Main Menu------\n ")
                adminwelcome()
                return main()
            elif res is not None:
                print("your login is success")
                print("Welcome to my cart Mr.{}\n".format(res[1].title()))
                print("+"*30,)
                u=user(res[0],res[2])
                u.userwelcome(db_conn,curser)
                return main()
        except:
            return main()
    else:
        print("Thank you for visiting")
        print("+"*30)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
