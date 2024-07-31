import matplotlib.pyplot as plt

def calculate_pmf(values, probabilities):
    if len(values) != len(probabilities):
        raise ValueError("Values and probabilities lists must have the same length.")
    
    total_prob = sum(probabilities)
    if abs(total_prob - 1.0) > 1e-9:
        print("Normalizing probabilities as they do not sum to 1.")
        probabilities = [p / total_prob for p in probabilities]
    
    return {values[i]: probabilities[i] for i in range(len(values))}

def calculate_cdf(pmf):
    sorted_values = sorted(pmf.keys())
    cdf = {}
    cumulative_prob = 0.0
    for value in sorted_values:
        cumulative_prob += pmf[value]
        cdf[value] = cumulative_prob
    return cdf

def plot_distribution(pmf, cdf=None):
    values = list(pmf.keys())
    probabilities = list(pmf.values())
    
    fig, ax1 = plt.subplots()
    ax1.bar(values, probabilities, width=0.4, color='b', alpha=0.7, label='PMF')
    ax1.set_xlabel('Values')
    ax1.set_ylabel('Probability', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.set_title('PMF and CDF')
    
    if cdf:
        ax2 = ax1.twinx()
        cdf_values = list(cdf.values())
        ax2.plot(values, cdf_values, color='r', marker='o', label='CDF')
        ax2.set_ylabel('Cumulative Probability', color='r')
        ax2.tick_params(axis='y', labelcolor='r')

    fig.tight_layout()
    plt.legend(loc='upper left')
    plt.show()

def main():
    print("Welcome to the PMF and CDF Calculator!")
    values = list(map(int, input("Enter discrete values separated by spaces: ").split()))
    probabilities = list(map(float, input("Enter corresponding probabilities separated by spaces: ").split()))

    try:
        pmf = calculate_pmf(values, probabilities)
        print("PMF:", pmf)

        cdf = calculate_cdf(pmf)
        print("CDF:", cdf)

        plot_distribution(pmf, cdf)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
