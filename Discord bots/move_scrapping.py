import urllib.request
from move import move

name = input('Target move: ')
move = move(name,'','','','','')
move.scrap()
print(move.toString())