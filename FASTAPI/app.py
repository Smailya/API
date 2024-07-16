
from fastapi import FastAPI, Path, Query, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name:str
    price: float
    brand: Optional[str] = None
    
class UpdateItem(BaseModel):
    name:Optional[str]  = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {}


@app.get("/get-item/{item_id}/")  # Defining a GET endpoint at the path "/get-item/{item_id}/". This function will be called when a GET request is made to this path with an item ID.
def get_item(item_id: int = Path(..., description="The ID of the item you want to see")):  # The item_id path parameter is required (indicated by '...'), and has a description for documentation.
    if item_id in inventory:  # Check if the item_id exists in the inventory.
        return inventory[item_id]  # Returning the details of the item from the 'inventory' dictionary corresponding to the provided 'item_id'.
    else:  # If the item_id does not exist in the inventory.
        return {"error": "Item not found"}  # Returning an error message indicating the item was not found.

@app.get("/get-by-name/")  # Defining a GET endpoint at the path "/get-by-name/". This function will be called when a GET request is made to this path.
def get_item(name: str  = Query(None, title="Name", description= "Name of item."  )):  # using None make the query parameter not required anymore
    for item_id in inventory:  # Iterating through each item ID in the inventory.
        if inventory[item_id].name == name:  # Checking if the item's name matches the provided name.
            return inventory[item_id]  # Returning the item details if a match is found.
    return {"Data": "Not Found"}  # Returning a message indicating that the item was not found if no match is found.
    #   raise HTTPException(status_code=404, detail="Not found")

#creating an item
    
@app.post("/create-item/{item_id}")  # Defining a GET endpoint at the path "/create-item/{item_id}". This function will be called when a GET request is made to this path.
def create_item(item_id: int, item: Item):
    if item_id in inventory:  # Checking if the item_id already exists in the inventory dictionary.
        return {"Error": "Item ID already exists."}  # Returning an error message if the item_id already exists.

    # If the item_id doesn't exist, add the new item to the inventory dictionary.
    inventory[item_id] = item
     
    return inventory[item_id]  # Returning the details of the newly created item from the inventory dictionary.
    #   raise HTTPException(status_code=404, detail="Not found")
#updating items

@app.put("/update-item/{item_id}")  # Defining a PUT endpoint that takes an item_id as a path parameter.
def update_item(item_id: int, item: UpdateItem):  # Defining the update_item function which takes item_id as an integer and item of type UpdateItem.
    if item_id not in inventory:  # Checking if the provided item_id exists in the inventory dictionary.
        return {"Error": "Item ID does not exist."}  # Returning an error message if the item_id does not exist.
    # If the item_id exists, proceed to update the item in the inventory dictionary.
    if item.name !=None :
        inventory[item_id].name= item.name 
    if item.price !=None :
            inventory[item_id].price= item.price 
    if item.brand !=None :
            inventory[item_id].brand= item.brand 
        # Updating the item in the inventory with the new data. .update() method updates the dictionary with the key-value pairs from item.
    return inventory[item_id]  # Returning the updated item details from the inventory dictionary.


@app.put("/update-item/{item_id}")  # Defining a PUT endpoint that takes an item_id as a path parameter.
def update_item(item_id: int, item: UpdateItem):  # Defining the update_item function which takes item_id as an integer and item of type UpdateItem.
    if item_id not in inventory:  # Checking if the provided item_id exists in the inventory dictionary.
        return {"Error": "Item ID does not exist."}  # Returning an error message if the item_id does not exist.
    # If the item_id exists, proceed to update the item in the inventory dictionary.
    if item.name is not None:  # Check if the 'name' field of the item is not None.
        inventory[item_id].name = item.name  # If not None, update the 'name' field of the item in the inventory.
    if item.price is not None:  # Check if the 'price' field of the item is not None.
        inventory[item_id].price = item.price  # If not None, update the 'price' field of the item in the inventory.
    if item.brand is not None:  # Check if the 'brand' field of the item is not None.
        inventory[item_id].brand = item.brand  # If not None, update the 'brand' field of the item in the inventory.
    return inventory[item_id]  # Returning the updated item details from the inventory dictionary.


#Deleting an item
@app.delete("/delete-item")
def delete_item(item_id:int =Query(..., description= "The ID of the item to delete", gt=0 )):
    if item_id not in inventory:
        return {"Error": "ID does not exist"}
    #   raise HTTPException(status_code=404, detail="Does not exist")
    del inventory[item_id]
    return {"Success": "Item deleted"}
    #   raise HTTPException(status_code=404, detail="Does not exist")
