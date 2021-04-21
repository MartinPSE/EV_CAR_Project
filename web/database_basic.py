## CONNECT POSTGRES
import psycopg2
import geopandas as gpd


conn_string = "host='localhost' dbname ='webgis' user='postgres' password='postgres'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()
#%%
