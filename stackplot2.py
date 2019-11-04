from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


days = [1, 2, 3, 4, 5, 6, 7, 8, 9]


developer1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
developer2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
developer3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]


labels = ['developer1', 'developer2', 'developer3']
colors = ['#6d904f', '#fc4f30', '#008fd5']
plt.stackplot(days, developer1, developer2, developer3, labels=labels, colors=colors)

plt.legend(loc=(0.07, 0.05))

plt.xlabel('Days')
plt.ylabel('Hours Worked')

plt.title("My Awesome Stack Plot2")
plt.tight_layout()

plt.savefig('stackplot2.png')

plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
