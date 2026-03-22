import matplotlib.pyplot as plt

def plot_results():
    methods = ["Traditional", "RL Model"]
    utilization = [75, 92]

    plt.bar(methods, utilization, color=["red", "green"])
    plt.title("Bed Utilization Comparison")
    plt.xlabel("Method")
    plt.ylabel("Utilization (%)")
    plt.show()


if __name__ == "__main__":
    plot_results()