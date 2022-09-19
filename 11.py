import argparse
from data.users import User
from data import db_session

db_session.global_init("db/user.db")
user = User()
db_sess = db_session.create_session()
a = [['Ridley', 'Scott', 21, 'captain', 'research engineer', 'module_1', 'scot3t_chief@mars.org', "Санкт-Петербург"],
     ['Joy', 'Kresp', 18, 'worker', 'biologist', 'module_1', 'division@ma3rs.org', ''],
     ['Mark', 'Wrens', 19, 'worker', 'astronomer', 'module_1', 'mwrens@m3ars.org', ''],
     ['Annie', 'Tilens', 23, 'worker', 'radiation specialist', 'module_1', 'aie@ma6rs.org', '']]
for i in a:
     user = User()
     user.surname = i[1]
     user.name = i[0]
     user.age = i[2]
     user.position = i[3]
     user.speciality = i[4]
     user.address = i[5]
     user.email = i[6]
     user.city_from = i[7]
     db_sess.add(user)
     db_sess.commit()