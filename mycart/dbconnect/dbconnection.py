import pymysql
db_conn = pymysql.connect(user='root', password='root', host='localhost', port=3306, database='mycart')
print(db_conn)
curser = db_conn.cursor()
print(curser)


def create_table(cur, db):
    cur.execute("""create table register(
                id int primary key auto_increment,
                name varchar(30),
                email varchar(30) unique,
                phone bigint unique,
                address varchar(100),
                password varchar(20) 
                )""")
    db.commit()


def create_category(cur, db):
    cur.execute("""create table category(
                item_id varchar(10) primary key,
                item_name varchar(30) unique
                )""")
    db.commit()

def create_product(cur, db):
    cur.execute("""create table product(p_id varchar(20) primary key, 
                p_name varchar(30), 
                price int, 
                description varchar(100), 
                item_id varchar(10), 
                FOREIGN KEY (item_id) references category(item_id));""")
    db.commit()

def create_cart(cur, db):
    cur.execute("""create table cart(cart_id int  primary key auto_increment, 
                user_id int,
                user_email varchar(30), 
                item_id varchar(10), 
                prod_id varchar(10), 
                price int,
                FOREIGN KEY (user_id) references register(id),
                FOREIGN KEY (item_id) references category(item_id),
                FOREIGN KEY (prod_id) references product(p_id)
                );""")
    db.commit()

def create_order(cur, db):
    cur.execute("""create table orderbill(order_id int primary key auto_increment, 
                order_date date,
                user_id int,
                user_email varchar(30),
                shipping_address varchar(100),  
                prod_details text, 
                actual_price int,
                discount_price int,
                billing_price int,
                FOREIGN KEY (user_id) references register(id)
                );""")
    db.commit()

def insert_admin(cur, db):
    cur.execute("""insert into register (name,email,phone,address,password) 
    values('venugopal','venugopal@admin.com',9966332211,'nellore','admin'));""")
    db.commit()

#create_table(curser, db_conn)
#create_category(curser, db_conn)
#create_product(curser, db_conn)
#create_cart(curser, db_conn)
#create_order(curser, db_conn)
#insert_admin(curser, db_conn)


