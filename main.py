from flask import Flask, render_template, request, redirect, url_for
import random
import copy
import re
from flask import Flask, request, Response, abort, render_template,session,make_response
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from collections import defaultdict
from sqlalchemy import create_engine
import pandas as pd
import pymysql
import datetime
import paramiko
from urllib.parse import urlparse,parse_qsl
import requests
from io import StringIO
import csv
app = Flask(__name__)
db_path = "mysql://shuichi47:V3BtyW&U@172.104.91.29:3306/twitter_text"
url_sql = urlparse(db_path)
conn = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(host = url_sql.hostname, port=url_sql.port, user = url_sql.username, password= url_sql.password, database = url_sql.path[1:]))

df = pd.read_sql('select * from neoneet_ai where like_number > 49 ORDER BY like_number desc',conn)
users_twitter = []
for i in range(len(df)):
    users_twitter.append('https://twitter.com/neoneet_ai/status/'+str(df['tweet_id'][i]))

@app.route("/")
def zero():

    return render_template('zero.html')

@app.route("/self")
def self():

    return render_template('self.html')

@app.route("/note")
def note():

    return render_template('note.html')


@app.route("/bot")
def bot():

    return render_template('bot.html')


@app.route("/saron")
def saron():

    return render_template('saron.html')

@app.route("/tweet")
def tweet():


    return render_template('tweet.html',users_twitter=users_twitter)


if __name__ == '__main__':
    app.run(debug=True)
