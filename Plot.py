import matplotlib.pyplot as plt

# Data
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Title
plt.title("Programming Language Usage")

# Show
plt.show()