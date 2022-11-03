import pymongo
client= pymongo.MongoClient("mongodb+srv://tanupanwar:rtYX5ckBv0CKHf6c@cluster0.1qc5pxj.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)

d={
    "name":"tanu",
     "surname":"panwar",
    "email":"tp220799@gmail.com"
}
db1=client['MONGODB']
coll=db1['test11']
coll.insert_one(d)

