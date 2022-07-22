import matplotlib
import matplotlib.pyplot as plt
import seaborn

matplotlib.use('Qt5Agg')

def plot_chart():
    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 
              'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    games_released = [1416, 1738, 1996, 1957, 2059, 1767,
                      2186, 2333, 2370, 2491, 2328, 2221]

    # вызовите функцию barplot()
    seaborn.barplot(x=months, y=games_released)
    plt.show()
