import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import os

import pandas as pd
import os

# Определяем пути к файлам и создаем DataFrame с начальными значениями
os.makedirs('bin', exist_ok=True)

files = {
    'bin/projects.csv': pd.DataFrame({
        'id': [],
        'Project': []
    }),
    'bin/comments.csv': pd.DataFrame({
        'id': [],
        'comment': []
    }),
    'bin/comment_log.csv': pd.DataFrame({
        'id': [],
        'task_id': [],
        'comment_id': [],
        'date': []
    }),
    'bin/status_log.csv': pd.DataFrame({
        'id': [],
        'taskid': [],
        'status_id': [],
        'changedate': []
    }),
    'bin/status.csv': pd.DataFrame({
        'id': [],
        'status': []
    }),
    'bin/tasks.csv': pd.DataFrame({
        'id': [],
        'Task': [],
        'start_date_id': [],
        'status_id': [],
        'tag_id': [],
        'comment_id': [],
        'project_id': [],
        'value_id': [],
        'goal_id': []
    })
}

# Функция для загрузки или создания DataFrame
def load_or_create_dataframe(file_path, default_df):
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        if df.empty:
            df = default_df
    else:
        df = default_df
    return df

# Загрузка или создание каждого DataFrame
dataframes = {file: load_or_create_dataframe(file, df) for file, df in files.items()}



# Сохранение каждого DataFrame в CSV
for file, df in dataframes.items():
    df.to_csv(file, index=False)


dataframes['bin/projects.csv']