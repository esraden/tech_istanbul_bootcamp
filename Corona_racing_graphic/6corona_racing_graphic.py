# -*- coding: utf-8 -*-
"""6Corona_racing_graphic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B_MVjTQNYnK2PwSnW_ZWgmb07LJcER9G

## Corona Veri Seti ile Veri Görselleştirme

![image.png](attachment:image.png)

## Kütüphaneleri içe aktarma-yükleme
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from google.colab import drive
drive.mount('/content/drive')

"""## Veri dosyasını yükleme"""

ls

df=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/corona_dat.csv')

"""## Keşifsel Veri Analizi (EDA)"""

pd.set_option('display.max_columns',None) # df de tüm kolonları göstermesini sağlar
df.head()

df.tail()

df.info()

#Türkiyedekiş günlük vaka sayıları
df[['date','Turkey']]

#seçilen ülkelerdeki günlük vaka sayıları
df[['date','Turkey','Italy','Germany','China','US']]

#Türkiyeyi ayrı bir seriye at
df_tr=df['Turkey']
type(df_tr)
#türkiyedeki günlük vaka değişimini çiz
df_tr.plot()

#türkiyedeki günlük vaka değişimini çiz
df_tr.plot()

#Seçilen ülkelerdeki günlük vaka sayısı değişimini çiz
df_countries=df[['Turkey','Italy','Germany','China','US']]
df_countries.plot()

#seçilen ülkelerdeki toplam vaka sayısı
df_countries.sum(axis=0)

#Toplam vaka sayısı
df_countries.sum(axis=0).plot(kind='bar')

sum_daily=df_countries.cumsum(axis=0) # aynı sütundaki rakamları alt alta toplasın
sum_daily

#sum_daily.drop('World_total',axis=1,inplace=True)

#sum_daily.drop('Countries_Total',axis=1,inplace=True)

sum_daily['Countries_Total']=sum_daily.sum(axis=1)
sum_daily

sum_daily.plot()

df_4=df[['date','Turkey','Italy','Germany','China','US']]
df_4.info()

df_4

#tarihsel olarak sıralı olduğu için date ı index oalrak ayarlayabiliriz
df_4['date']=pd.to_datetime(df_4['date'])
#df_4['month']=pd.DatetimeIndex(df_4['date']).month
#df['month'] = df['Date'].dt.month
df_4.set_index('date',inplace=True) #indexi i date olarak ayarla tarihe göre index le
df_4

#vaka sayıalrını kümülatif toplam yap
df_4.cumsum(axis=0).plot()

"""## Yarışan grafik"""

df_yarisan=df_4.cumsum(axis=0) # Günlğük vakaların kümülatif toplamlarında bir veri seti oluştur
df_yarisan

sns.lineplot(data=df_yarisan)

"""Bu uygulamayı da sisteme kurmalısınız
ffmpeg kurulumu

https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
"""

pip install bar_chart_race

pip install ffmpeg

import bar_chart_race as bcr

bcr.bar_chart_race(df_yarisan,filename='esra.denizli.mp4', figsize=(10, 8),
                  period_length=500,#toplam video uzunluğu
                   steps_per_period=10, #değişim hızı
                  title='COVID-19 @esraden')

!pip install bar_chart_race

import bar_chart_race as bcr
