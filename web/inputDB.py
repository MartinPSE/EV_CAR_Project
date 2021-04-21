# 기상청 관리번호 수정

import pandas as pd
import psycopg2
import numpy as np
import geopandas as gpd
import rasterio
import rasterio.features
import rasterio.warp

from sqlalchemy import create_engine
Gisang = pd.read_csv('gisang_station.csv',encoding='EUC-KR' )
Gisang=Gisang.drop('시작일', axis = 1)
Gisang=Gisang.drop('관리관서', axis = 1)
Gisang=Gisang.drop('노장해발고도(m)', axis = 1)
Gisang=Gisang.drop('기압계(관측장비지상높이(m))', axis = 1)
Gisang=Gisang.drop('기온계(관측장비지상높이(m))', axis = 1)
Gisang=Gisang.drop('풍속계(관측장비지상높이(m))', axis = 1)
Gisang=Gisang.drop('강우계(관측장비지상높이(m))', axis = 1)
Gisang = Gisang.fillna('0')
Gisang2 = Gisang['종료일'].str.contains('0',regex = False)
Gisang_Station = Gisang[Gisang2]
Gisang_Station = Gisang_Station.drop('종료일',axis = 1)
Gisang_Station = Gisang_Station.rename(index = str, columns={'지점':'station_num','지점명':'station_name','위도':'lat','경도':'lon'})
engine = create_engine('postgresql://postgres:postgres@localhost:5432/webgis')
Gisang_Station.to_sql('gisang_station', engine)
#%%

conn_string = "host='localhost' dbname ='webgis' user='postgres' password='postgres'"
conn = psycopg2.connect(conn_string)
curs= conn.cursor()



with rasterio.open('kangwondo//GTIF_GRS80//gangneung_grid.tif') as dataset:

    # Read the dataset's valid data mask as a ndarray.
    mask = dataset.dataset_mask()

    # Extract feature shapes and values from the array.
    for geom, val in rasterio.features.shapes(
            mask, transform=dataset.transform):

        # Transform shapes from the dataset's own coordinate
        # reference system to CRS84 (EPSG:4326).
        geom = rasterio.warp.transform_geom(
            dataset.crs, 'EPSG:5186', geom, precision=6)

        # Print GeoJSON shapes to stdout.
        print(geom)