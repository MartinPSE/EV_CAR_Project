# https: // api2.sktelecom.com / tmap / routes / pedestrian?version =
# 9f52672d-844c-44fc-890a-b8522517f13c
#-*- coding:utf-8 -*-
#파이썬3으로 동작 시킬것
import os
import json
import requests

params = {'version':'1','startX':'126.894796',"startY":'37.647092',"endX":'126.835955',"endY":'37.655266','reqCoordType':'WGS84GEO','startName':'hwajung','endName':'starfield'} #딕셔너리 형식 - 사용하기 편리하다.
headers = {"appKey": "9f52672d-844c-44fc-890a-b8522517f13c"}
r = requests.get("https://api2.sktelecom.com/tmap/routes/pedestrian?", params=params, headers=headers)
#print (r.json()) #json형태로 출력

#json 라이브러리 사용 파싱
#json -> python 객체로 변환
data = r.json() # geojson 파일로 받아옴
# 위에 써있는거 다써면 돌아감.
# x가 경도!