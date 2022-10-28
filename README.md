# simple_CRUD for beginers

Simple Student/Person data using Mongo_db

Library used:- pymongo (pip install pymongo)
Connection:- mongodb://localhost:27017
Database name :-Student
Collection Name:-persons
Number of Documents:14
Collection description:- \_id,firstName,lastName,gender,age,number
Data file:-can be found '../persons.json'
CRUD:-Create Read Update and Delete

    To Create :-
        The function has to be called with the document you want to insert to the collection the collection name and number of documents to be inserted as parameters.

        example:-
            print(input_document({'firstName':"felicia",'lastName':"Samson",'gender':"female",'age':19,'number':"881234085"},mycol,1))

    To Read :-
        The function has to be called with the query and projection,thw query can be left empty to display all element that matches the projection parameters.

        example:-
            print(search(mycol,{},{'firstName':'Joe'}))

    To Update :-
        The function is called with collection name, the query to update the new query and the number of documents to be updated parameters

        example:-
            print (edit(mycol,{'firstName':"felicia",'lastName':"Samson",'gender':"female",'age':19,'number':"881234085"},{'firstName':"felicia",'lastName':"Gates",'gender':"female",'age':29,'number':"8812317654"},1))

    To Delete .-
        The function is called with the collection name,query to be deleted and number of documents to be deleted.

        example:-
            print(remove_doc(coll,query,num_doc));
