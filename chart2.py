import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('Qt5Agg')

def plot_chart():
    
    # Данные для графика
    mu = 0
    sigma = 1
    x = np.arange(-5,5,.01)
    f = np.exp(-np.square((x-mu)/sigma)/2)/(np.sqrt(2*np.pi)*sigma)
    
    fig, ax = plt.subplots()
    ax.plot(x, f)
    
    ax.set(xlabel='X', ylabel='Y', title='Нормальное распределение')
    ax.grid()
    
    plt.show()

def plot_chart2():
    
    # Данные для графика
    mu = 0
    sigma = 1
    mu2 = 1
    sigma2 = 2
    mu3 = -2
    sigma3 = 3
    x = np.arange(-11,7,.01)
    f = np.exp(-np.square((x-mu)/sigma)/2)/(np.sqrt(2*np.pi)*sigma)
    f2 = np.exp(-np.square((x-mu2)/sigma2)/2)/(np.sqrt(2*np.pi)*sigma2)
    f3 = np.exp(-np.square((x-mu3)/sigma3)/2)/(np.sqrt(2*np.pi)*sigma3)
    
    fig, ax = plt.subplots()
    ax.plot(x, f)
    ax.plot(x, f2)
    ax.plot(x, f3)
    
    ax.set(xlabel='X', ylabel='Y', title='Нормальное распределение - 3 графика')
    ax.grid()
    
    plt.show()
