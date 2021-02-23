import matplotlib.pyplot as plt



def Graph(data):
    xAxis, yAxis = None, None
    labels = []

    
    for item in data:
        xAxis = item[2]
        yAxis = item[3]
        labels.append("Lap " + str(item[0]))
        plt.plot(xAxis, yAxis)





    plt.title("Speed over time")
    plt.xlabel("Time")
    plt.ylabel("Speed")
    plt.legend(labels)
    plt.show()


if __name__ == "__main__":
    Graph(None)