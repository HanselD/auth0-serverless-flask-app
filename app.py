from functools import wraps
import json
from os import environ as env
from werkzeug.exceptions import HTTPException

from dotenv import load_dotenv, find_dotenv
from flask import Flask, jsonify, redirect, render_template, url_for
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode

app = Flask(__name__)

OAuth = OAuth(app)
