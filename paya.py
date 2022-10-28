import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['Student']
mycol = mydb['persons']
#Create document
def input_document(document,coll,num_doc):
    if num_doc == 1:
        x = coll.insert_one(document)
        return (f'{x.inserted_id} is inserted into your collection')
    elif num_doc > 1:   
        x = coll.insert_many([document])
        return (f'{x.inserted_ids} is inserted into your collection')
#Search for document
def search(coll,query,proj):
    for i in coll.find(query,proj):
        print(i)
#Edit document
def edit(coll,old_query,new_query,num_doc):
    if num_doc == 1:
        coll.update_one(old_query,new_query)
    elif num_doc >1:
        coll.update_many(old_query,new_query)
#remove document
def remove_doc(coll,query,num_doc):
    if num_doc == 1:
        x=coll.delete_one(query)
    elif num_doc >1:
       x= coll.delete_many(query)
       print(x.deleted_ids, "document deleted") 
#Created document
#input_document({'firstName':"felicia",'lastName':"Samson",'gender':"female",'age':19,'number':"881234085"},mycol,1)
print(search(mycol,{'firstName':'Joe'}))