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
    
    sns.histplot(data=df_normal_a, x='score', bins=50)
    
    plt.show()
