import pymongo 
client = pymongo.MongoClient("mongodb+srv://dsa17:1234@cluster0.nhysy.mongodb.net/?retryWrites=true&w=majority") 
db = client.virtusa 

records=db.superwomen

d={"name":input("enter name"),"ph":int(input("enter phone number")),"mail":input("enter emailid")} 
records.insert_one(d)
print("inserted sucessfully")
read=records.find()
for x in read:
    print(x)




