# def list():
# 	list1=[5,10,15,20,25]
# 	list=list1[0],list1[-1]
# 	return (list)
# print (list())


# a=[1,1,2,3,5,8,13,21,34,55,89]
# b=[]
# def list2():
# 	for index in a:
# 		if index <=5:
# 			print (index)
# 			a.append()


def FirstAndLast(NumList):
	newlist = []
	newlist.append(NumList[0])
	newlist.append(NumList[-1])
	print(newlist)

FirstAndLast([1,2,3,4,5])


def IfLessThanFive(list1):
	for elms in list1:
		if elms < 5:
			print(elms)

IfLessThanFive([0,2,78,123,1,9,4,3,-8])

def elements(list1 , list2):
	newList = []
	for numbers in list1:
		if numbers in list2:
			newList.append(numbers)
	print(newList)

elements([1,3,4,67,45,25,12],[1,34,4,54,45,12])

