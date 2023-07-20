import requests
import sqlite3

db = sqlite3.connect('movies.db')
movie= db.execute('SELECT * FROM move')
for m in movie:
    mv = requests.get('http://192.168.1.67:8000/upload',params={'moviename':m[1],'genre':m[2],'tags':m[3],'eurl':m[4],'img':m[5],'cat':'movie','quality':'HD','eno':'1'})
    print(mv.text)