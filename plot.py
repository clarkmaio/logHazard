import matplotlib.pyplot as plt


def plot_side_by_side(x, y1, y2, y1_title: str = None, y2_title: str = None, title: str = None) -> None:
    '''
    Plot two functions side by side
    '''
    fig, ax = plt.subplots(1, 2, sharex=True, sharey=True)
    fig.suptitle(title, fontweight='bold')

    ax[0].plot(x, y1, label='f', color='black')
    ax[0].set_title(y1_title, fontweight='bold')
    ax[0].grid(linestyle=':')

    ax[1].plot(x, y2, label='f', color='red')
    ax[1].set_title(y2_title, fontweight='bold')
    ax[1].grid(linestyle=':')
    plt.ion()
    plt.show()

def plot(x, y1, y2, y1_label: str = None, y2_label: str = None, title: str = None) -> None:
    '''
    Plot two functions side by side
    '''

    plt.figure()
    plt.plot(x, y1, label=y1_label, color='black')
    plt.plot(x, y2, label=y2_label, color='red')
    plt.title(title)
    plt.legend()
    plt.ion()
    plt.show()
    plt.grid(linestyle=':')
