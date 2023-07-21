from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from bson.objectid import ObjectId

app = FastAPI()

Client = MongoClient("mongodb://localhost:27017")
db = Client["votes"]
collection = db["votes"]

#Create data model
class Vote(BaseModel):
    name: str
    count: int

@app.get("/")
async def root():
    return {"message" : "HI mother"}

#Create CRUD (POST)
@app.post("/votes/")
async def create_vote(vote: Vote):
    result = collection.insert_one(vote.dict())
    return {
        #Use function to create text id
        "id" : str(result.inserted_id),
        "name" : vote.name,
        "count" : vote.count,
    }

#Read Database (GET)
@app.get("/votes/{vote_id}")
async def read_vote(vote_id: str):
    vote = collection.find_one({"_id": ObjectId(vote_id)})
    if vote: # If find vote values
        return {"id": str(vote["_id"]), "name" : vote["name"], "count" : vote["count"]}
    else: # If not cannot find vote data
        raise HTTPException(status_code=404, detail = "Vote not found")
    
#Update (PUT)
@app.put("/votes/{vote_id}")
async def update_vote(vote_id : str, vote : Vote):
    result = collection.update_one(
        {"_id" : ObjectId(vote_id)}, {"$set": vote.dict(exclude_unset=True)}
    )
    if result.modified_count == 1:
        return {"id" : vote_id, "name" : vote.name, "count" : vote.count}
    else:
        raise HTTPException(status_code=404, detail="Vote not found" )

#Delete 
@app.delete("/votes/{vote_id}")
async def delete_vote(vote_id: str):
    result = collection.delete_one({"_id" : ObjectId(vote_id)})
    if result.deleted_count == 1:
        return {"status" : "ok"}
    else:
        raise HTTPException(status_code=404, detail="Vote not found")
