pizza = int(input("Сколько было кусков пиццы?"))
SlicePiz = (int(input("Сколько ты сьел?")))
SumSlice = pizza - SlicePiz
if SumSlice == 1:
    print("У тебя осталось " + str(pizza - SlicePiz) + " кусок пиццы")
elif 2 <= SumSlice <= 4:
    print("У тебя осталось " + str(pizza - SlicePiz) + " куска пиццы")
else:
    print("У тебя осталось " + str(pizza - SlicePiz) + " кусков пиццы")
input()