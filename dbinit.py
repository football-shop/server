import sqlite3

connect = sqlite3.connect('data.db')
cursor = connect.cursor()

## 테이블 SHOP
try:
  table = 'shop' # 테이블 이름
  cursor.execute('''DROP TABLE %s ''' % table)
except:
  pass

try:
  cursor.execute('''CREATE TABLE shop (name text, lat real, lng real)''')
  print('Created %s' % table)
  cursor.execute("INSERT INTO shop VALUES ('Mediapia', 37.584708, 126.984830)")
  cursor.execute("INSERT INTO shop VALUES ('Ssaka', 37.566166, 127.006100)")
  cursor.execute("INSERT INTO shop VALUES ('Kisan sports', 37.577352, 127.015016)")
  cursor.execute("INSERT INTO shop VALUES ('Nike Capo', 37.565372, 127.009225)")
  connect.commit()
  print('Data Inserted into %s' % table)
except:
  raise
  pass


