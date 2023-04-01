import os.path
import matplotlib.pyplot as plt
import numpy as np

if os.path.isfile("data/app.txt"):
    with open("data/app.txt", "r") as f:
        for line in f:
            a, b, c = line.split()

else:
    with open("data/app.txt", "w+") as g:
        g.write(input())
    with open("data/app.txt", "r") as e:
        for line in e:
            a, b, c = line.split()

x= np.arange(float(a), float(b), float(c))
y= np.sin(x*2*np.pi)

plt.axis([float(a),float(b), -1,1])
plt.title('sin')
plt.plot(x,y)
plt.savefig('res.svg')
plt.show()
