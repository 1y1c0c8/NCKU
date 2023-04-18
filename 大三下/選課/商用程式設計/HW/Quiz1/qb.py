# 9*9 without perfect square

for i in range(1, 10):
    for j in range(1, 10):
        if i!=j:
            print(str(i*j) ,end="\t")
        else:
            print("\t", end="")
    print("\n", end="")