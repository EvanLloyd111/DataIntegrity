import matplotlib.pyplot as plt

x = []

for i in range(10):
    x.append(i)

y1 = [12, 45, 29, 23, 13, 5, 28, 3, 15, 41]
y2 = [33, 37, 48, 46, 14, 35, 48, 45, 23, 15]

plt.plot(x, y1, label="package loss")
plt.plot(x, y2, label = "lost files")

plt.ylabel("Data")
plt.xlabel("Time (Hours)")

plt.legend()
plt.title("Data Integrity")
plt.show()

