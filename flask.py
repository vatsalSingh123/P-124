from asyncio import tasks
from crypt import methods
from email import message
from re import A
from flask import Flask,jsonify,request

app = Flask(__name__)
List = [{
    'id':1,
    'name':'joy',
     'contact':998764456,
     'done':False
},
    {
    'id':2,
    'name':'steve',
     'contact':998764455,
     'done':False
}    
        ]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide The Data"
        },400)
        
    contact = {
        'id': tasks[-1]['id'] + 1,
        'name':request.json['name'],
        'contact':request.json.get('conatct'," "),
        'done':False
    }
    
    List.append(contact)
    return jsonify({
            "status":"successs",
            "message":"contact added successfully"
        })
    
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":List
    })
    

if (__name__=="__main__"):
    app.run(debug=True)