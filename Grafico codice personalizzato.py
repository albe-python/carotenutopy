import matplotlib.pyplot as plt

data = {'Rosario': 7, 'Marco': 4, 'Franco': 5, 'Paolo': 8}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Voti di matematica nel corso')


plt.show()
