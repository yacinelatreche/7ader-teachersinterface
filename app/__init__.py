from flask import Flask
from flask import render_template
import flask
from flask import request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

from app import login_view