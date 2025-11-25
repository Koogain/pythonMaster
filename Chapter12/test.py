import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from geopy.geocoders import Nominatim

df = pd.read_csv(
    "C:\\Users\\User\\PycharmProjects\\pythonMaster\\Chapter12\\지원자 정보(응답).csv",
    encoding="utf-8-sig"
)

# 컬럼 이름에서 BOM · 공백 · 따옴표 전부 제거
df.columns = df.columns.str.replace('\ufeff', '').str.strip().str.replace('"','')

print(df.columns.tolist())