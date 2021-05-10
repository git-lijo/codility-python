# IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops() 
# should return 
# [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].

def scoops(ingredient, topping):
	re = [ [] for i in range(0,len(ingredient))]
	for i in range(len(ingredient)):
		re[i].append(ingredient[i])

		re[i].append(topping[0])

	return re


print(scoops(["vanilla", "chocolate"], ["chocolate sauce"]))
