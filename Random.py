import random
sample_list = ["A","B","C","D","E"]
print("Original list : ")
print(sample_list)

random.shuffle(sample_list)
print("\n After the first shuffle: ")
print(sample_list)

random.shuffle(sample_list)
print("\n After the second shuffle")
print(sample_list)