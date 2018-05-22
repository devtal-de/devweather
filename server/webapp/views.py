#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template, request, Response, redirect
import json
from webapp import app,db
from webapp.models import *

from datetime import datetime, timedelta

@app.route("/")
def index():
    data = db.session.query(realdata).order_by(realdata.time.desc()).first()
    return render_template('index.html', data=data)


@app.route("/data/<int:id>")
def data(id):
    data = db.session.query(realdata).filter(realdata.id==id).first()
    if not data:
        return "no data"
    return render_template('index.html', data=data)

@app.route("/post", methods=['POST'])
def post():
    if not request.is_json:
        return "no valid json"
    content = request.json
    #return str(content)
    record = realdata()
    record.time = datetime.now()
    for key,value in content.items():
        setattr(record,key,value)

        # time = datetime.now(),
        # indoor_humidity = float(content['indoor_humidity']),
        # outdoor_humidity = content['outdoor_humidity'],
        # indoor_temperature = content['indoor_temperature'],
        # outdoor_temperature = content['outdoor_temperature'],
        # outdoor_dew_point = content['outdoor_dew_point'],
        # wind_chill_temp = content['wind_chill_temp'],
        # wind_speed = content['wind_speed'],
        # gust_speed = content['gust_speed'],
        # wind_dir = content['wind_dir'],
        # rain_diff = content['rain_diff'],
        # total_rain = content['total_rain'],
        # abs_pressure = content['abs_pressure']

    try:
        db.session.add(record)
        db.session.commit()
        return "OK"
    except Exception as e:
        db.session.rollback()
        return "FAIL: " + e
