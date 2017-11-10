// hashed the _id
db.testCollection.createIndex( { _id : "hashed" } )   


//shard the exampleCollection	
sh.shardCollection( "exampleDB.testCollection", { "_id" : "hashed" } ) 
