import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


matplotlib.use('Qt5Agg')

def plot_chart():
    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 
              'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    games_released = [1416, 1738, 1996, 1957, 2059, 1767,
                      2186, 2333, 2370, 2491, 2328, 2221]

    # вызовите функцию barplot()
    sns.barplot(x=months, y=games_released)
    plt.show()

def plot_chart2():
    sns.set()
    
    np.random.seed(33)
    normal_data_a = np.random.normal(size=500, loc=100, scale=10)
    
    df_normal_a = pd.DataFrame(data=normal_data_a, columns=['score']).assign(group='Group A')
    
    sns.histplot(data=df_normal_a, x='score', bins=50, kde=True)
    # ~ kde - огибающая кривая (ядерная оценка плотности)
    
    plt.show()

def plot_chart3():
    sns.set()
    
    np.random.seed(33)
    normal_data_a = np.random.normal(size=500, loc=100, scale=6)
    normal_data_b = np.random.normal(size=500, loc=107, scale=5)
    
    df_normal_a = pd.DataFrame(data=normal_data_a, columns=['score']).assign(group='A')
    df_normal_b = pd.DataFrame(data=normal_data_b, columns=['score']).assign(group='B')
    
    score_data = pd.concat([df_normal_a, df_normal_b], ignore_index=True)
    
    # print(score_data)
    
    sns.histplot(data=score_data, 
                x='score', 
                alpha=.7,
                hue='group',
                bins=50, 
                kde=True)
    
    plt.show()
