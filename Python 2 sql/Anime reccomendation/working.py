from bridge_sql import bridge
from anm_anime import anm_anime
from usu_user import usu_user
import time


while(True):
	cmd = input("cmd: ")
	if(cmd == 'geturl'):
		print(bridge.getAnimeUrl(input("name: ")))
	elif(cmd == 'save_anime'):
		bridge_sql.insert(input("name: "),input("score: "))
	elif(cmd == 'save_user'):
		newuser = usu_user(input('Name: '),input('Password: '),time.strftime("%d/%m/%Y"))
		newuser.usu_insert()
	else:
		print('Error')

