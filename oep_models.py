#use the engine form app_settings.py
#create all oep models with autoload = true
#figure out how to use sqla_orm with django-geojson

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



