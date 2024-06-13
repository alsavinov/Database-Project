import psycopg2
import psycopg2.extras
from psycopg2 import Error
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class myDB():
    def __init__(self,db, us, pa):
        try:
            self.connection = psycopg2.connect(user=us,
                                          password=pa,
                                          host = 'localhost',
                                          port="5432",
                                          database=db)
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            self.cursor = self.connection.cursor()
            self.cursor = self.connection.cursor(cursor_factory = psycopg2.extras.DictCursor)
        except (Exception, Error) as error:
            h = 2
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            h = 1
            print("Соединение с PostgreSQL закрыто")

    def query(self, q):
        self.cursor.execute(q)
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def callproc(self, func, params):
        return self.cursor.callproc(func, params)




def create_db(name_db):
    global ndb 
    ndb = name_db
    db = myDB('tmp', 'postgres', '111')
    db.callproc('f_create_db', [name_db])
    res = db.fetchall()
    db.connection.close()
    return res

def connect_db(name_db):
    global ndb 
    ndb = name_db
    db = myDB('tmp', 'postgres', '111')
    db.callproc('f_connect_db', [name_db])
    res = db.fetchall()
    db.connection.close()
    return res


def show_table_players():
    db = myDB(ndb, us, pa)
    db.callproc('show_table_players', [])
    res = db.fetchall()
    db.connection.close()
    return res

def show_table_teams():
    db = myDB(ndb, us, pa)
    db.callproc('show_table_teams', [])
    res = db.fetchall()
    db.connection.close()
    return res

def show_table_bets():
    db = myDB(ndb, us, pa)
    db.callproc('show_table_bets', [])
    res = db.fetchall()
    db.connection.close()
    return res

def get_matching_bets():
    db = myDB(ndb, us, pa)
    db.callproc('get_matching_bets', [])
    res = db.fetchall()
    db.connection.close()
    return res


def show_table_users():
    db = myDB(ndb, us, pa)
    db.callproc('show_table_users', [])
    res = db.fetchall()
    db.connection.close()
    return res

def show_table_matches():
    db = myDB(ndb, us, pa)
    db.callproc('show_table_matches', [])
    res = db.fetchall()
    db.connection.close()
    return res

def delete_all_bets():
    db = myDB(ndb, us, pa)
    db.callproc('delete_all_bets', [])
    db.connection.close()

def delete_all_tables():
    db = myDB(ndb, us, pa)
    db.callproc('delete_all_tables', [])
    db.connection.close()

def f_delete_bet(aid):
    db = myDB(ndb, us, pa)
    db.callproc('delete_bet', [aid])
    db.connection.close()

def f_delete_match(aid):
    db = myDB(ndb, us, pa)
    db.callproc('delete_match', [aid])
    db.connection.close()





def f_update_user(aid, aphone, afirst_name, alast_name, agender, aage):
    db = myDB(ndb, us, pa)
    db.callproc('update_user', [aid, aphone, afirst_name, alast_name, agender, aage])
    db.connection.close()

def f_update_match(aid, amatch_result, ascore_home, ascore_away):
    db = myDB(ndb, us, pa)
    db.callproc('update_match', [aid, amatch_result, ascore_home, ascore_away])
    db.connection.close()

def add_user(aphone, afirst_name, alast_name, agender, aage):
    db = myDB(ndb, us, pa)
    db.callproc('add_user', [aphone, afirst_name, alast_name, agender, aage])
    db.connection.close()

def add_bet(auser_id, amatch_id, aoutcome, asum_of_bet, acoef):
    db = myDB(ndb, us, pa)
    db.callproc('add_bet', [auser_id, amatch_id, aoutcome, asum_of_bet, acoef])
    db.connection.close()

def add_match(amatch_date, ateam_id_home, ateam_id_away, amatch_result, ascore_home, ascore_away):
    db = myDB(ndb, us, pa)
    db.callproc('add_match', [amatch_date, ateam_id_home, ateam_id_away, amatch_result, ascore_home, ascore_away])
    db.connection.close()



def delete_db(name_db):
    db = myDB('tmp', 'postgres', '111')
    db.callproc('f_delete_db', [name_db])
    res = db.fetchall()
    db.connection.close()
    return res



def get_us_pa(user, password):
    global us
    us = user
    global pa
    pa = password


