import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Patch
import pandas as pd

def make_bar(data, por, title, name, file_name, drop_df=False, range=False):
    df = pd.DataFrame({
        'Label': data,
        'Value': por
        })

    if drop_df:
        df = df.drop(labels=0, axis=0)

    fig, ax = plt.subplots()
    ax.bar('Label', 'Value', data=df, color=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray', 'tab:green', 'tab:purple', 'tab:pink', 'm', 'tab:olive','tab:brown', 'mediumseagreen','k'])

    plt.tick_params(
        axis='x',        
        which='both',   
        bottom=False,  
        top=False,    
        labelbottom=False)

    plt.title(title)

    fontP = FontProperties()
    fontP.set_size('small')

    cmap = dict(zip(df['Label'].tolist(), ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray', 'tab:green', 'tab:purple', 'tab:pink', 'm', 'tab:olive','tab:brown', 'mediumseagreen','k']))

    patches = [Patch(color=v, label=k) for k, v in cmap.items()]

    if not range:
        ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    else:
        plt.ylim([0,5])
    plt.legend(labels=df['Label'].tolist(), handles=patches, title=name, bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

    plt.savefig(file_name, dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
    plt.clf()
    plt.close()

