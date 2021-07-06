

import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
import platform
if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
elif platform.system() == 'Darwin':
    rc('font', family = 'AppleGothic')
else:
    print('Check your OS system')


def god():

    df = pd.read_excel('./files/youtube_rank.xlsx')
    df.head()
    df['replaced_subscriber'] = df['replaced_subscriber'].astype('int')
    df.info()
    
    pivot_df = df.pivot_table(index = 'category', values = 'replaced_subscriber', aggfunc = ['sum','count'])
    pivot_df.head()


    pivot_df.columns = ['subscriber_sum', 'category_count']
    pivot_df.head()


    pivot_df = pivot_df.reset_index()
    pivot_df.head()

    plt.figure(figsize = (30,10))
    plt.pie(pivot_df['subscriber_sum'], labels=pivot_df['category'], autopct='%1.1f%%')
    plt.show()


    pivot_df = pivot_df.sort_values(by='category_count', ascending=False)
    pivot_df.head()
    plt.figure(figsize = (30,10))
    plt.pie(pivot_df['category_count'], labels=pivot_df['category'], autopct='%1.1f%%')
    plt.show()
