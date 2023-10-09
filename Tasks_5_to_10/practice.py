customer_name = "sowji"
customer_name1 = customer_name + "N"
print(customer_name)
print(customer_name1)

l1 = [1,2,3,4]
l2 = l1.append(20)
print(l1)
print(l2) #None because l2 does not return new list instead it modifies the original list and will returns none

print("shallow copy::::::::::::::::::")
import copy
l1 = [1,2,3,4]
l2 = l1.copy()
print("before changing value:::",id(l1),id(l2))
l2[0] = 100
print("after changing value::::", id(l1),id(l2))
print("both id's are different::::::shallow copy varies")
print(l1)
print((l2))

print("nested lists::::::")
l1 = [1,[2,3],[4,5]]
l2 = l1
l2[2][0] = 400
print("after changing nested value:::::", id(l1[2][0]),id(l2[2][0]))
print("both id's are same:::::::::so shallow copy is applying")
print(l1)
print(l2)


print("deep copy:::::::::::::::::::::")
l1 = [1,[3,4,5],[6,7,8],[9,10,11]]
l2 = l1
deep_copy = copy.deepcopy(l2)
deep_copy[2][1] = 234565
print(deep_copy)
print(l1)
