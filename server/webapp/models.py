#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, Integer, Float, BigInteger, String, Boolean, Binary, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from webapp import db


##Stores the
class forecastdata(db.Model):
    __tablename__ = 'forecastdata'
    id = Column(Integer(), primary_key=True, nullable=False)
    fetchdate = Column(DateTime, nullable=False)
    forecastdate = Column(DateTime, nullable=False)
    provider = Column( String(), nullable=False)
    key = Column( String(), nullable=False)
    value = Column( Float(), nullable=False)


##Stores the
class realdata(db.Model):
    __tablename__ = 'realdata'
    id = Column(Integer(), primary_key=True, nullable=False)
    time = Column(DateTime, nullable=False)
    indoor_humidity = Column( Float() )
    outdoor_humidity = Column( Float() )
    indoor_temperature = Column( Float() )
    outdoor_temperature = Column( Float() )
    outdoor_dew_point = Column( Float() )
    wind_chill_temp = Column( Float() )
    wind_speed = Column( Float() )
    gust_speed = Column( Float() )
    wind_dir = Column( String() )
    rain_diff = Column( Float() )
    total_rain = Column( Float() )
    rain_plain1 = Column( Float() )
    rain_plain1 = Column( Float() )
    abs_pressure = Column( Float() )
