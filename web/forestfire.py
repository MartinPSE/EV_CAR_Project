##
import psycopg2
import geopandas as gpd
import pandas as pd
import rasterio as rt

conn_string = "host='localhost' dbname ='webgis' user='postgres' password='postgres'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()
#%%
cur.execute("select * from coffee")
# cur.execute("CREATE TABLE news_list (nid SERIAL PRIMARY KEY, press_date DATE, ranking INTEGER, score INTEGER, press TEXT, title TEXT, link TEXT, creation_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
#
# conn.commit()​
## 만약 DB에서 데이터를 가져오는 SELECT문이라면 아래 코드를 붙여준다.
## result = cur.fetchall()
# data_coffee = cur.fetchall()

conn_string = "host='localhost' dbname ='webgis' user='postgres' password='postgres'"
conn = psycopg2.connect(conn_string)
curs= conn.cursor()

cur.execute("INSERT INTO gisang_station (station_num, station_name) VALUES (station_num, station_num, station_name)",[station_num,station_name])
conn.commit()
#%% Create Table
cur.execute("CREATE TABLE gisang_station (station_num SERIAL PRIMARY KEY, station_name TEXT);");
conn.commit()
##cur.execute("INSERT INTO gisang_station (station_num, station_name) VALUES (%s %s)", (Gisang_Station['station_num'], Gisang_Station['station_name']))
##conn.commit()
# print(data_coffee)
df_coffee = gpd.GeoDataFrame.from_postgis('select * from coffee', conn, geom_col='geom' )

Gangneung = pd.read_csv('kangwondo\kangwondo_askii_2014\Gangneung.txt',names=['x','y','height'],delimiter=' ')

dataset = rt.open('kangwondo\Hoengseong.tif')


# INSERT 보다 이거 쓰는게 데이터프레임 넣기 더 좋음
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@localhost:5432/webgis')
Gisang_Station.to_sql('gisang_station', engine)