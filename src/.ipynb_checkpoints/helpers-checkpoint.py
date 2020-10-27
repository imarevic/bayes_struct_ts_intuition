import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_ts_and_save(df, idx, y, title, out_path):
    """
    plots a ts given a df explicitly.
    args:
    df: data frame
    idx: time-series index
    y: y variable
    title: title of plot
    out_path: path to write to
    """
    # plot
    sns.set_style('ticks')
    fig, ax = plt.subplots()
    fig.set_size_inches(18.5, 10.5)
    fig.suptitle(title, fontsize=20)
    sns.lineplot(idx, y, data=df)
    
    # save figure
    fig.savefig(os.path.join(out_path, df.name + '.png'), dpi=100)