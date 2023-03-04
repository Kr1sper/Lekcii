op=open("1.txt", "r")
wr=open("2.txt", "w")

A=op.read()
wr.write(A)

op.close()
wr.close()