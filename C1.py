import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Project"]

mycol = mydb["Student"]

name=input("Username")
password=input("Password")
if(name=='Parvej' and password=='1234567'):
    while(1):
        print("1.Insert")
        print("2.Update")
        print("3.delete")
        print("4.display")
        ch=input("enter your choice")
        if(ch=='1'):
            Name=input("Enter the Name")
            RollNo=input("Enter the Roll_NO")
            val={"name1":Name,"rollno":RollNo}
            print(type(val))
            x=mycol.insert_one(val)
            print(x.inserted_id)
        if(ch=="2"):
            uname=input("Enter the name you want to update")
            myquery = {"name1": uname}
            nname=input("Enter new updating name")
            newvalues = {"$set": {"name1": nname}}
            mycol.update_one(myquery, newvalues)
        if(ch=="3"):
            delname =input("Enter the name you want to delete")
            for x in mycol.find({}, {"name": delname}):
                delq = {"name1": delname}
                mycol.delete_one(delq)
        if(ch=='4'):
            for x in mycol.find():
                print(x)



ouput:----
/home/oem/anaconda3/bin/python /home/oem/PycharmProjects/project/mongodb.py
UsernameParvej
Password1234567
1.Insert
2.Update
3.delete
4.display
enter your choice1
Enter the Nameknam
Enter the Roll_NO14
<class 'dict'>
5da541b2483ccbb7ea75f842
1.Insert
2.Update
3.delete
4.display
enter your choice4
{'_id': ObjectId('5d9eb0b04d37d325e1499c87'), 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': ObjectId('5d9eb2110ffabff172f24fc5'), 'name1': 'Amarjett', 'rollno': '322'}
{'_id': ObjectId('5d9eb6fd6fe709d1b3f0d0f2'), 'name1': 'Ruturaj', 'rollno': '368'}
{'_id': ObjectId('5da15ce82c4f3f2ff8c2868d'), 'name1': 'famne', 'rollno': '12'}
{'_id': ObjectId('5da188dc36839ad92742d507'), 'name1': 'Kunal', 'rollno': '325'}
{'_id': ObjectId('5da541b2483ccbb7ea75f842'), 'name1': 'knam', 'rollno': '14'}
1.Insert
2.Update
3.delete
4.display
enter your choice2
Enter the name you want to updateknam
Enter new updating namefgf
1.Insert
2.Update
3.delete
4.display
enter your choice3
Enter the name you want to deleteknam
1.Insert
2.Update
3.delete
4.display
enter your choice4
{'_id': ObjectId('5d9eb0b04d37d325e1499c87'), 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': ObjectId('5d9eb2110ffabff172f24fc5'), 'name1': 'Amarjett', 'rollno': '322'}
{'_id': ObjectId('5d9eb6fd6fe709d1b3f0d0f2'), 'name1': 'Ruturaj', 'rollno': '368'}
{'_id': ObjectId('5da15ce82c4f3f2ff8c2868d'), 'name1': 'famne', 'rollno': '12'}
{'_id': ObjectId('5da188dc36839ad92742d507'), 'name1': 'Kunal', 'rollno': '325'}
{'_id': ObjectId('5da541b2483ccbb7ea75f842'), 'name1': 'fgf', 'rollno': '14'}
1.Insert
2.Update
3.delete
4.display
enter your choice
