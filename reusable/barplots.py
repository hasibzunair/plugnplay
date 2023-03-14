import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def autolabel(ax, rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{:.2f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=0, fontsize=15)
        #ax.set_ylim(ymin=1)


def autolabel_(ax, rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{:.2f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=0, fontsize=15)
        #ax.set_ylim(ymin=1)


def make_bar_plots(labels: list, name1: str, m1_scores: list, name2:str, m2_scores: list, save_path: str):
    """
    Make bar plots of scores of models on different metrics/datasets etc.

    Args:
        labels (list): List of labels. It can be name of different metrics or datasets
        name1 (str): Name of model
        m1_scores (list): List of scores from one model
        name2 (str): Name of other model
        m2_scores (list): Same as m1 but another model
        save_path (list): Path to save plot

    Returns:
        None

    Examples:
    >>> labels = ["mAP", "CR", "CF1"]
    >>> model1_auc = [67.9, 40.6, 55.0]
    >>> model2_auc = [86.7, 71.3, 79.0]
    >>> make_bar_plots(labels, 
                        "Baseline", model1_auc, 
                        "MSL", model2_auc, 
                        save_path="logs/barplot.pdf")
    """

    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots()
    # colors from https://colorhunt.co/
    rects1 = ax.bar(x - width/2, m1_scores, width, label=name1, color='#E96479') 
    rects2 = ax.bar(x + width/2, m2_scores, width, label=name2, color='#7DB9B6')
    ax.set_ylabel('Score (%)', fontsize=20)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=0, fontsize=20)
    ax.set_ylim([30,100])
    ax.grid(True)
    #ax.patch.set_facecolor('white')
    autolabel(ax, rects1)
    autolabel(ax, rects2)
    fig.tight_layout()
    fig.set_size_inches(8, 4, forward=True)
    plt.title('VOC2007 (\u2191)', loc='left', fontsize=25, color='gray', pad=12)
    plt.legend(loc='upper center', fontsize=18)
    plt.savefig(f"{save_path}", bbox_inches='tight', pad_inches=0, dpi=300)
    plt.show()