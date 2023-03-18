import os.path

flag = 'false'
if os.path.isfile("data/app.conf"):
    with open("data/app.conf", "r") as f:
        for line in f:
            a, b, c = line.split()

else:
    with open("data/app.conf", "w+") as g:
        g.write(input())
    with open("data/app.conf", "r") as e:
        for line in e:
            a, b, c = line.split()

my_arr=[] * int(a)
for i in range(0, int(a)):
    d = int(b)*i+int(c)
    my_arr.insert(i, d)

with open("data/result.dat","w+") as v:
    v.write(' '.join(map(str,my_arr)))
