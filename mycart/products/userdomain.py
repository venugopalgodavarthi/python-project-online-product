from dbconnect.dbconnection import db_conn,curser

def userdetails(db_conn,curser,email,id):
    curser.execute("select * from register where email=%s and id=%s",[email,id])
    res=curser.fetchone()
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("----profile details----")
    print('''username: {}\nEmail: {}\nphone: {}\naddress: {}'''.format(res[1],res[2],res[3],res[4]))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return True


def usercreate(db_conn,curser,res):
    curser.execute("insert into register (name,email,phone,address,password) values (%s,%s,%s,%s,%s)", res)
    db_conn.commit()
    return True


