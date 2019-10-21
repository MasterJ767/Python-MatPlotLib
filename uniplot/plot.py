import matplotlib.pyplot as plt


def plot_bar_show(d):
    """Create a bar chart"""
    # A list of numbers as long as the elements in d
    r = range(0, len(d))
    # Prepare a figure
    plt.figure()

    # Add bars, one at each x position, with the values of d
    plt.bar(r, d.values())
    # Add labels to the x-axis, with the keys of d
    plt.xticks(r, d.keys())
    # Squash everything up so there is no white space
    plt.tight_layout()
    # Show the graph
    plt.show()


def plot_pie_show(d):
    """Create pie chart"""
    labels = d.keys()
    sizes = []
    for i in d:
        size = d.values()/len(d)
        sizes.append(size)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
