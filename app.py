from flask import Flask,Response,request       #importing flask and request and response

import json  #importing json

from appfunction import operation  #imported  related module

mangoobj=operation( )  #intialization of operation class

app=Flask(__name__)   #creating app

#***********************************************************************************************************************************


@app.route('/')
def base(): #to check working properly

    return Response(response=json.dumps({'Status':'Ready'}),status=200,mimetype='application/json')


#***************************************************************************************************************************************

@app.route('/add_contact',methods=['POST']) #Routing the add contact value
def post_data():

    details=request.json   #accepting request in form of json

    '''{
    "Name":"xyz",
    "Phone_Number":"123456789",
    "Email":"xyz@domain.com"
    }'''

    if( details is None or details == {} or 'Email' not in details ):

        return Response(response=json.dumps({'Error':'Please provide data and email address its a required field'}),
                        status=400,
                        mimetype='application/json')



    response=mangoobj.add_contact(details)

    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


#*************************************************************************************************************************************************

@app.route('/update_contact',methods=['PUT'])  #routing update contact
def update():

    data=request.json  #requesting json value

    '''{
        "filter":{"Name":"XYZ"}  # can have any value name ,phone_number ,Email ,

        "update_value": {'Field' :"updated value "}
    }'''

    if (data is None or data == {} or 'update_value' not in data): # checking weather value exist or not

        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')

    response=mangoobj.update_contact(data) # callling update contact  from appfinction module

    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#*******************************************************************************************************************************************************

@app.route('/delete_contact',methods=['DELETE'])
def delete():

    data=request.json

    '''{
        "Filter":{"Anycolumn":"value"}
    }'''


    if (data is None or data == {} or 'Filter' not in data):  #checking data exist

        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')


    response=mangoobj.delete_contact(data) #calling contact delete

    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


#*************************************************************************************************************************************************************

@app.route('/all_contact/',methods=["GET"])

def get_contact():

    data=request.json  #requesting json file
    '''
    {
    "number_of_contact_to_print":"value example 10,5,4",
    "defualt"="True"
    }
   '''
    if(data['defualt']=='False'): #if value is given like 10,5

        number_of_contact_to_print=int(data['number_of_contact_to_print'].strip())

        response=mangoobj.all_contact(number_of_contact_to_fetch=number_of_contact_to_print)

    else:

        response=mangoobj.all_contact() #else print only defult value

    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#**********************************************************************************************************************************************************************


@app.route('/search_contact',methods=['GET']) #routing searcj contact

def search():

    data=request.json
    '''{

    "Filter":{"Email":"abhisheklumiamicro@gmail.com"},#Filter can be any column and have both column to
    "value_to_print":"10"
}'''

    if(data is None or data =={} or 'Filter' not in data): #checking weather filter  exist or Nothing

        return Response(response=json.dumps({"Error": "Please provide Email or name  information"}),
                        status=400,
                        mimetype='application/json')

    response=mangoobj.search_contact(data) #calling search_contact

    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

#**********************************************************************************************************************************************************************

if __name__ =='__main__':


    app.run(debug=True,port=5001,host='0.0.0.0')                                                                                                                                                                                                                                                                                                                                                                                           
