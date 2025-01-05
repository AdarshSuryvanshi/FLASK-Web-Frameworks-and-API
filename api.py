### Put and Delete-HTTP Verbs
### Working With API's--Json.....It means that the (Data-Source) on which we are going to PERFORME oprations..that Data-Source will be in the form of JSON means 
#                                IN  THE FORM OF DICTIONARY (KEY AND VALUE) PAIR 

from flask import Flask, jsonify, request,json # THIS ARE ALL MODULE OF PYTHONS 

app = Flask(__name__)
# Here we are trying to create a To -do list .. By using Rest Api /requests module..

##Initial Data in my to do list
# THIS IS THE DATA HERE BASED ON THIS WE ARE PERFORMING OPERATIONS ON 4 HTTP METHODS , BY USING THIS DATA ONLY ...YOU CAN ADD TO  THIS DATA 
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]# This data we have  combine from any json file so it is in the form of "Dictionary "

@app.route('/')     # Home page 
def home():
    return "Welcome To The Sample To DO List App"

## Get: Retrieve all the items from this route .... BASICALLY YAHA PAI MAI GET REQUEST MAI (ITEM_ID) REQUEST KARUNGS TOH SAMNE SAI MUJHE USI (ITEM_ID) KA DATA-SOURCE RETURN HOGA ...and that Data-Source will be in the form of (JSON) 

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items) # Here we are returning data in the form of "json" so that Data will be "return"on   the app in the form of "Dictionary"i.e data will be return (key:value)
"""
NOTE :- SINCE HERE WE ARE CREATING A TO-DO LIST BY REST API , SO HERE WE ARE USING 4 HTTP METHODS TO CREATE THAT "APP"....SO AS WE ALL KNOW FEATURES OF 4 HTTP METHODS 
SO WE AREUSING EVERY METHOD FOR DIFFFRENT WORK CORRESPONDING TO (TO-DO LIST) , THERER IS A SPECIFIC WORK CORRESPONDING TO (TO-DO LIST) OF EVERY SINGLE METHOD
BELOW ARE FUCNTIONS USING 4 DIFFRENT AND INDIVIDUAL HTTP METHODS WRT TO (TO-DO LIST) AND IT'S SUNCTIONALITY ,,,SO WE ARE JUST CREATING THIS "APP" BASED ON TO-DO LIST
WHERE WE ARE USING "4 HTTP METHODS " FOR VARIOUS USE  ......
BASICALLY WE ARE "PERFORMING" , 4 DIFFRENT HTTP MEHOD FOR DIFFRENT USES IN APP ..HERE ARE 4 ROUTES FOR 4 HTTP METHODS 
"""

## get: Retireve a specific item by Id...AS NAME SUGGEST (GET) IS USED TO RETRIVE DATA FROM SPECIFIC ID..CONDITION IS  FOR "RETRIVING DATA FROM SPECIFIC ID" IN  TO-DO LIST 
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None) # Here in this for loop , in each iteration condition wiil be check for item[id]...in above route   
    if item is None:                                                   #If not found then return "None"

        return jsonify({"error":"item not found"}) #. BASICALLY YAHA PAI MAI GET REQUEST MAI (ITEM_ID) REQUEST KARUNGS TOH SAMNE SAI MUJHE USI (ITEM_ID) KA DATA-SOURCE RETURN HOGA ...and that Data-Source will be in the form of (JSON) 
    return jsonify(item)

## Post :create a new task- API...AS HERE IN POST :- WE ARE UPDATING NEW DATA IN TO-DO LIST...BY USING POST METHOD...UPDATING/CREATING  NEW DATA IN TO-DO LIST 
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})      # .BASICALLY YAHA PAI MAI "(POST)" REQUESTHAI USKA KAM  MAI NEW  DATA (new item_id,name and description) KO CREATE KARNA CHAHATA HU .. YAHA PAI POST REQUEST KA KAM HAI "LAST INDEX KAI BAAD NEW (ITEM-ID, NAME AND DESCIPTION )"CREATE KARNE KA 
                                                        # TO CREATE NEW DATA-SOURCE THAT WILL BE IN THE FORM OF "JSON" MEANS (key:value) pair kai form mai  
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name":request.json['name'],
        "description":request.json["description"]


    }
    items.append(new_item)
    return jsonify(new_item)

# Put: Update an existing item  IN PUT :- WE ARE UPDATING NEW DATA IN TO-DO LIST...BY USING PUT METHOD...UPDATING  NEW DATA IN TO-DO LIST 

@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"})                              # .BASICALLY YAHA PAI MAI "(PUT)" REQUEST HAI USKA KAM HAI KI IN THE EXISTING  DATA (KISI SPECIFIC CHEEZ KO ) KO MODIFY KARNA   .. YAHA PAI PUT REQUEST KA KAM HAI "AT PARTICULAR" (ITEM_ID PAI /NAME PAI/DESCRPTION PAI) JO DATA-SOURCE HAI USKO MODIFY KARNA 
                                                        # TO UPDATE IN EXISTING DATA-SOURCE THAT WILL BE IN THE FORM OF "JSON" MEANS (key:value) pair kai form mai 
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# DELETE: Delete an item  WE ARE DELETING ANY SPECIFIC DATA IN TO-DO LIST...BY USING DELETE METHOD DELETING ANY DATA  IN TO-DO LIS
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"})  # TO DELETE A SPECIFIC ITEM_I/ NAME/DESCRIPTION THIS ALL YOU CAN DO HERE 




if __name__ == '__main__':
    app.run(debug=True)
