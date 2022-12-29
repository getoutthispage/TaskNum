maxN = int(input("Введите число больше 100"))
minN = int(input("Введите число меньше 10"))

if maxN >= 100 and minN <= 10:
    print("число: " + str(minN) + " помещается " + str(maxN // minN) + ' раз')
else:
    print("введите верные числа")
input()