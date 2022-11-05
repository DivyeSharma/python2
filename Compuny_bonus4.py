bs = float(input("Enter the Basic Salary :"))
if(bs<1500):
	hra=bs*0.1
	da=bs*0.9
else:
	hra=500
	da=bs*0.98
 
gs=bs + hra + da
print("Gross Salary Rs :", gs)