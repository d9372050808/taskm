import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# чистые таблицы
df_value=pd.DataFrame(['[[ценность1]]','[[ценность2]]','[[ценность3]]'], columns=['ценность'])
df_goal=pd.DataFrame(['[[цц1]]','[[цц2]]','[[цц3]]'], columns=['цель']) 
df_project=pd.DataFrame(['[[проект1]]','[[проект2]]','[[проект3]]'], columns=['проект']) 
df_tags=pd.DataFrame(['[[тег1]]','[[тег2]]','[[тег3]]'], columns=['тег'])
df_rank=pd.DataFrame([3,2,1,0.5, 0.25], columns=['ранг'])
df_time=pd.DataFrame([5, 30, 120, 240, 900], columns=['время'])
df_prob=pd.DataFrame([0.1,0.2,0.3,0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1], columns=['вероятность'])
df_stasus=pd.DataFrame(['[[статус1]]','[[статус2]]','[[статус3]]'], columns=['статус'])

df_date_start=pd.DataFrame(['[[дата1]]','[[дата2]]','[[дата3]]'], columns=['дата старта'])
df_date_finish=pd.DataFrame(['[[дата1]]','[[дата2]]','[[дата3]]'], columns=['дата завершения'])
df_comment=pd.DataFrame(['[[коммент1]]','[[коммент2]]','[[коммент3]]'], columns=['коммент'])
df_time_plan=pd.DataFrame([5, 30, 120, 240, 900], columns=['длительность план'])
df_time_fact=pd.DataFrame([5, 30, 120, 240, 900], columns=['длительность факт'])
df_log=pd.DataFrame(['[[лог1]]','[[лог2]]','[[лог3]]'], columns=['лог'])

# df_alarm=pd.DataFrame([1,10], columns=['беспокоит'])
# df_mpv=pd.DataFrame(['[[мвп1]]','[[мвп2]]','[[мвп3]]'], columns=['мвп'])
# df_finish1=pd.DataFrame(['[[рез1]]','[[рез2]]','[[рез3]]'], columns=['рез1'])
# df_finish2=pd.DataFrame(['[[рез1]]','[[рез2]]','[[рез3]]'], columns=['рез2'])

# комплексные таблицы
df_task=pd.DataFrame(['[[задача1]]','[[задача2]]','[[задача3]]'], columns=['задача']) 


 'тег', 'статус', 'дата', 'время', 'ком', 'польза', 'интерес', 'влияние', 'вероятность', 'время', 'силы', 'ресурс', 'беспокоит', 'автомат', 'рез1', 'рез2', 'мвп', 'множ_ценн']