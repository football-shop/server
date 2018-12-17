import sqlite3
import pickle

connect = sqlite3.connect('data.db')
cursor = connect.cursor()

## 테이블 HOTITEMS
try:
  table = 'hotItems' # 테이블 이름
  cursor.execute('''DROP TABLE %s ''' % table)
except:
  pass

try:
  cursor.execute('''CREATE TABLE hotItems (name text, image bin)''')
  print('Created %s' % table)
  file = open('./assets/images/hotItems_adidasSpectralMode.png', 'rb')
  with file:
      data = file.read()
  cursor.execute("INSERT INTO hotItems VALUES ('Adidas Spectral Mode', ?)", [sqlite3.Binary(data)])
  connect.commit()
  file.close()
  print('Data Inserted into %s' % table)
except:
  raise
  pass


