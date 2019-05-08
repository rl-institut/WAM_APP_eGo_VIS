#use the engine form app_settings.py
#create all oep models with autoload = true
#figure out how to use sqla_orm with django-geojson

from sqlalchemy import create_engine, MetaData, Table, Column, MetaData, ARRAY, BigInteger, Boolean, \
                        Column, Float, ForeignKey, Integer, JSON, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from geoalchemy2.types import Geometry
########################################################################################################################

# set the schema name as string
ding0_schema = "grid"

DECLARATIVE_BASE = declarative_base()
METADATA = DECLARATIVE_BASE.metadata


# set your Table names
DING0_TABLES = {'versioning': 'ego_grid_ding0_versioning',
                'line': 'ego_grid_ding0_line',
                'lv_branchtee': 'ego_grid_ding0_lv_branchtee',
                'lv_generator': 'ego_grid_ding0_lv_generator',
                'lv_load': 'ego_grid_ding0_lv_load',
                'lv_grid': 'ego_grid_ding0_lv_grid',
                'lv_station': 'ego_grid_ding0_lv_station',
                'mvlv_transformer': 'ego_grid_ding0_mvlv_transformer',
                'mvlv_mapping': 'ego_grid_ding0_mvlv_mapping',
                'mv_branchtee': 'ego_grid_ding0_mv_branchtee',
                'mv_circuitbreaker': 'ego_grid_ding0_mv_circuitbreaker',
                'mv_generator': 'ego_grid_ding0_mv_generator',
                'mv_load': 'ego_grid_ding0_mv_load',
                'mv_grid': 'ego_grid_ding0_mv_grid',
                'mv_station': 'ego_grid_ding0_mv_station',
                'hvmv_transformer': 'ego_grid_ding0_hvmv_transformer'}


#####################################################TABLE DEFINITION###################################################
# 1 versioning table
versioning = Table(DING0_TABLES['versioning'], METADATA,
                   Column('run_id', BigInteger, primary_key=True, autoincrement=False, nullable=False),
                   Column('description', String(6000)),
                   schema=ding0_schema
                   )

# 2 ding0 lines table
ding0_line = Table(DING0_TABLES['line'], METADATA,
                   Column('id', Integer, primary_key=True),
                   Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                   Column('id_db', BigInteger),
                   Column('edge_name', String(100)),
                   Column('grid_name', String(100)),
                   Column('node1', String(100)),
                   Column('node2', String(100)),
                   Column('type_kind', String(100)),
                   Column('type_name', String(100)),
                   Column('length', Float(10)),
                   Column('u_n', Float(10)),
                   Column('c', Float(10)),
                   Column('l', Float(10)),
                   Column('r', Float(10)),
                   Column('i_max_th', Float(10)),
                   Column('geom', Geometry('LINESTRING', 4326)),
                   schema=ding0_schema
                   )

# 3 ding0 lv_branchtee table
ding0_lv_branchtee = Table(DING0_TABLES['lv_branchtee'], METADATA,
                           Column('id', Integer, primary_key=True),
                           Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                           Column('id_db', BigInteger),
                           Column('geom', Geometry('POINT', 4326)),
                           Column('name', String(100)),
                           schema=ding0_schema

                           )

# 4 ding0 lv_generator table
ding0_lv_generator = Table(DING0_TABLES['lv_generator'], METADATA,
                           Column('id', Integer, primary_key=True),
                           Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                           Column('id_db', BigInteger),
                           Column('la_id', BigInteger),
                           Column('name', String(100)),
                           Column('lv_grid_id', BigInteger),
                           Column('geom', Geometry('POINT', 4326)),
                           Column('type', String(22)),
                           Column('subtype', String(30)),
                           Column('v_level', Integer),
                           Column('nominal_capacity', Float(10)),
                           Column('weather_cell_id', BigInteger),
                           Column('is_aggregated', Boolean),
                           schema=ding0_schema
                           )
# 5 ding0 lv_load table
ding0_lv_load = Table(DING0_TABLES['lv_load'], METADATA,
                      Column('id', Integer, primary_key=True),
                      Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                      Column('id_db', BigInteger),
                      Column('name', String(100)),
                      Column('lv_grid_id', BigInteger),
                      Column('geom', Geometry('POINT', 4326)),
                      Column('consumption', String(100)),
                      schema=ding0_schema
                      )

# 6
ding0_lv_grid = Table(DING0_TABLES['lv_grid'], METADATA,
                      Column('id', Integer, primary_key=True),
                      Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                      Column('id_db', BigInteger),
                      Column('name', String(100)),
                      # Column('geom', Geometry('MULTIPOLYGON', 4326)),
                      Column('geom', Geometry('GEOMETRY', 4326)),
                      Column('population', BigInteger),
                      Column('voltage_nom', Float(10)),
                      schema=ding0_schema
                      )

# 7 ding0 lv_station table
ding0_lv_station = Table(DING0_TABLES['lv_station'], METADATA,
                         Column('id', Integer, primary_key=True),
                         Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                         Column('id_db', BigInteger),
                         Column('geom', Geometry('POINT', 4326)),
                         Column('name', String(100)),
                         schema=ding0_schema
                         )

# 8 ding0 mvlv_transformer table
ding0_mvlv_transformer = Table(DING0_TABLES['mvlv_transformer'], METADATA,
                               Column('id', Integer, primary_key=True),
                               Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                               Column('id_db', BigInteger),
                               Column('geom', Geometry('POINT', 4326)),
                               Column('name', String(100)),
                               Column('voltage_op', Float(10)),
                               Column('s_nom', Float(10)),
                               Column('x', Float(10)),
                               Column('r', Float(10)),
                               schema=ding0_schema
                               )

# 9 ding0 mvlv_mapping table
ding0_mvlv_mapping = Table(DING0_TABLES['mvlv_mapping'], METADATA,
                           Column('id', Integer, primary_key=True),
                           Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                           Column('lv_grid_id', BigInteger),
                           Column('lv_grid_name', String(100)),
                           Column('mv_grid_id', BigInteger),
                           Column('mv_grid_name', String(100)),
                           schema=ding0_schema
                           )

# 10 ding0 mv_branchtee table
ding0_mv_branchtee = Table(DING0_TABLES['mv_branchtee'], METADATA,
                           Column('id', Integer, primary_key=True),
                           Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                           Column('id_db', BigInteger),
                           Column('geom', Geometry('POINT', 4326)),
                           Column('name', String(100)),
                           schema=ding0_schema
                           )

# 11 ding0 mv_circuitbreaker table
ding0_mv_circuitbreaker = Table(DING0_TABLES['mv_circuitbreaker'], METADATA,
                                Column('id', Integer, primary_key=True),
                                Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                                Column('id_db', BigInteger),
                                Column('geom', Geometry('POINT', 4326)),
                                Column('name', String(100)),
                                Column('status', String(10)),
                                schema=ding0_schema
                                )

# 12 ding0 mv_generator table
ding0_mv_generator = Table(DING0_TABLES['mv_generator'], METADATA,
                           Column('id', Integer, primary_key=True),
                           Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                           Column('id_db', BigInteger),
                           Column('name', String(100)),
                           Column('geom', Geometry('POINT', 4326)),
                           Column('type', String(22)),
                           Column('subtype', String(30)),
                           Column('v_level', Integer),
                           Column('nominal_capacity', Float(10)),
                           Column('weather_cell_id', BigInteger),
                           Column('is_aggregated', Boolean),
                           schema=ding0_schema
                           )

# 13 ding0 mv_load table
ding0_mv_load = Table(DING0_TABLES['mv_load'], METADATA,
                      Column('id', Integer, primary_key=True),
                      Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                      Column('id_db', BigInteger),
                      Column('name', String(100)),
                      Column('geom', Geometry('GEOMETRY', 4326)),
                      Column('is_aggregated', Boolean),
                      Column('consumption', String(100)),
                      schema=ding0_schema
                      )

# 14 ding0 mv_grid table
ding0_mv_grid = Table(DING0_TABLES['mv_grid'], METADATA,
                      Column('id', Integer, primary_key=True),
                      Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                      Column('id_db', BigInteger),
                      Column('geom', Geometry('MULTIPOLYGON', 4326)),
                      Column('name', String(100)),
                      Column('population', BigInteger),
                      Column('voltage_nom', Float(10)),
                      schema=ding0_schema
                      )

# 15 ding0 mv_station table
ding0_mv_station = Table(DING0_TABLES['mv_station'], METADATA,
                         Column('id', Integer, primary_key=True),
                         Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                         Column('id_db', BigInteger),
                         Column('geom', Geometry('POINT', 4326)),
                         Column('name', String(100)),
                         schema=ding0_schema
                         )

# 16 ding0 hvmv_transformer table
ding0_hvmv_transformer = Table(DING0_TABLES['hvmv_transformer'], METADATA,
                               Column('id', Integer, primary_key=True),
                               Column('run_id', BigInteger, ForeignKey(versioning.columns.run_id), nullable=False),
                               Column('id_db', BigInteger),
                               Column('geom', Geometry('POINT', 4326)),
                               Column('name', String(100)),
                               Column('voltage_op', Float(10)),
                               Column('s_nom', Float(10)),
                               Column('x', Float(10)),
                               Column('r', Float(10)),
                               schema=ding0_schema
                               )
