
import sqlite3
import json
from flask import Flask, flash, redirect, render_template, \
     request, url_for, jsonify
from app import app

### URL Handling
HTML = '''
  <!doctype html>
  <title>API Server</title>
  <h1>API Server</h1>
  <p> This is API server for 'Mobile Programming' </p>
'''

@app.route('/')
@app.route('/index')
def index():
    return HTML

@app.route('/api/shop/')
def brand():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute("SELECT * FROM shop")

    data = []
    for r in rows:
        d = {}
        d['name'] = r[0]
        d['lat'] = r[1]
        d['lng'] = r[2]
        data.append(d)
    print(json.dumps(data))
    return jsonify(data)

@app.route('/api/shop/<name>')
def brand_name(name):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute("SELECT * FROM shop WHERE name = '%s' " % name)
    data = [r for r in rows]
    print(data)

    return jsonify(data)

@app.route('/api/shop/<name>', methods=['DELETE'])
def brand_delete(name):
    sql = "DELETE FROM shop WHERE name = '%s' " % (name)
    try:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        res = c.execute(sql)
        conn.commit()
        print(res)
        res = True
    except:
        res = False
        pass
    return jsonify(res)



