#dictionary used to store data values in key:value pairs
#oreder
#changable
#does not allows duplicate value

myDictionary = {
    "name":"Nikhil",
    "age":22,
    "gender":"male",
    "percentage":80.5
}
#age = myDictionary.get("age")
#print(age)
#keys=myDictionary.keys()
#print(keys)
#v#alue=myDictionary.value()
#print(value)

#items=myDictionary.value.items()
#print(items)
#myDictionary["roll no"] = 11
#print(myDictionary)

#myDictionary.pop("age")
#
# 
# dict1print(myDictionary)
#
# 
# dict1myDictionary.popitem()
#
# 
# dict1print(myDictionary)


#del0
#dict1={"one":1,"two":2,"three":3}
#dict2={"four":4,"five":5,"six":6}
#d#ict3 = dict2.copy()
#d#ict3.update(dict1)
#print(dict3)

dict1 = {
    "class":{
        "student":{
            "name":"xyz",
            "marks":{
                "python":100,
                "web":90
            }
        }
    }
}
print(dict1.get("class",{}.get("student",{}.get("marks",{}.get("web",{})))))