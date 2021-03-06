from flask import Flask
from flask import jsonify,request, render_template, redirect,url_for, flash, session
from flask_caching import Cache
from bokeh.plotting import figure
from bokeh.embed import components
import sqlite3
import json
import datetime
from google.cloud import storage
import json
import os
import bcrypt
import sklearn


app = Flask(__name__)
cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

from my_app import views
from my_app import models
from my_app import fetch_data