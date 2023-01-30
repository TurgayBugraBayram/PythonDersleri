# myList = []
# myList1 = list()
# # print(type(myList1))
# myTuple = ("merhaba",)
# # print(type(myTuple))
# myTuple1 = tuple()
# # print(myTuple[0])
# # myTuple[0]="py"
# # myList2= list(myTuple)
# del myTuple

# mySet = {"python","java","programlama","c","python","programlama"}
# mySet1 = set()
# print(mySet)
# print(len(mySet))
#
# mySet2 = {1,2,3,4}
# mySet3 = {1.0,2.0,3.0}
# mySet4 = {True,False}
# print(mySet2)
# print(mySet3)
# print(mySet4)
#
# mySet5 = {"python",1,False,2.0}
# print(mySet5)

# mySet = {"python","java","programlama","c","python","programlama"}
#
# mySet.add("r")
# print(mySet)
#
# mySet1 = {"bugra","turgay"}
# mySet.update(mySet1)
# print(mySet)
#
# mySet.remove("java")
# print(mySet)
# mySet.remove("python")
# print(mySet)
# mySet.discard("css")
# print(mySet)
#
# mySet.clear()
# print(mySet)
# del mySet
# print(mySet)

"""
dıct
"""

myDict = {
    "marka": "toyota",
    "model": "supra",
    "year": 1995,
    "colors": ["beyaz","kirmizi","mavi"]
}
# print(myDict)
# dict1 = dict()
# dict = {}
print(myDict["marka"])
print(myDict["model"])
print(myDict["year"])
# print(myDict["vites"])
print(len(myDict))
print(myDict["colors"])
print(myDict.get("year"))
print(myDict.keys())
keys = myDict.keys()
myDict["motor"] = 2.0
print(keys)

print(myDict.values())
myDict["model"] = "camry"
print(myDict.values())

print(myDict.items())


print("motor" in myDict)
myDict.update({"year":2000})
print(myDict)
