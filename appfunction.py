#class consist of all the functionalities of a phoneook app

#name of class is operation



class operation:

    def __setup_connection(self):

        import pymongo
        try:
            client=pymongo.MongoClient("mongodb+srv://9125366556:ib4d6PDNfzCTNYP8@cluster0.xwtnq.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")    #MongoClient is use for connection with database cluster



            client.server_info() # trigger exception if cannot connect the database

        except Exception as ex:


            print('**************************')
            print(ex)
            print('****************************')
            print('ERROR - can not connect to cluster')
            print('Please try another chance or check URL or check internet connection ')
        return client


    def connect_collection(self): #creating helper function to connect the database

        client=self.__setup_connection()
        collection=client['PhoneBook']['Phonebook']

        return collection





    #--------------------------------------------------------------------------------------------------




    def add_contact(self,details):  #creating a funtion that can perform ading of contact to a data base



        #details will contain all the data of phone book for Example
        ''' {'Name':'xyz',
         'Phone_Number':'12345647895',
          'Email':'abhisheklumiamicro@gmail.com'}'''


        try:

            #log.info("adding contact ")
            collection=self.connect_collection()   #connecting to Phone book  database

            email_check=details['Email']  #fecthing email  value

            name=details['Name'] #fetching name value

            Email=details['Email']  #fetching Email


            if(len(list(collection.find({'Email':email_check})))):  #checking Email exist or not

                output={'status':'Email exist'}  #output

            else:
                dbResponse=collection.insert_one(details) #inserting one

                output={'status':'Contact added ' ,'Name' : name,"Email":Email} #output





            return output #returing output





        except Exception as ex:

            print(ex)

    #---------------------------------------------------------------------------------------------------------------------------------------------

    def update_contact(self,data): #modify existing contact

        #filtter variable consist of field you want to search on for example {'name':'xyz'}

        #updated_value consist of upadted value for example {'name':'zxy'}

        #it will update only first contact of the filtered value
        try:

            filter=data['filter'] #fetching filter variable

            new_value={ "$set": data['update_value']} ##fetching updated value

            collection=self.connect_collection()  # callling collection

            dbResponse=collection.update_one(filter,new_value)  #update the value

            output = {'Status': 'Successfully Updated' if dbResponse.modified_count > 0 else "Nothing was updated."}

            return output

        except Exception as ex:


            print(ex)




    #---------------------------------------------------------------------------------------------------------------------------------------------------

    def delete_contact(self,data): #it will delete the contact

        #contact_to_delete will consist of filter criteria which contact to delete for example {'Name':'xyz'}

        try:

            Filter=data['Filter'] #fetching Filter value

            collection=self.connect_collection() #connection with data base


            dbResponse=collection.delete_one(Filter) #deleting conatct

            output = {'Status': 'Successfully Deleted' if dbResponse.deleted_count > 0 else "Document not found."}

            return output

        except Exception as ex:


            print(ex)


    #---------------------------------------------------------------------------------------------------------



    def all_contact(self,number_of_contact_to_fetch=10): # find all contact from the data base


        collection=self.connect_collection() #connect to database

        total_contact=list(collection.find({}))  #find all contact and convert into a list

        if(len(total_contact)>=number_of_contact_to_fetch): #check weather total contact is greater than number of contact to fetch

            result ='{} contacts out of {} contact '.format(number_of_contact_to_fetch,len(total_contact))  #store how many value of contact we get out of total


            return_contact=total_contact[0:number_of_contact_to_fetch+1] #return number of contact to fecth

            for val in return_contact:
                del val['_id']

            output={'contact':return_contact,'result':result}


        else:

            result='{} contacts out of {} contact '.format(len(total_contact),len(total_contact))  #return number of contact to fecth

            return_contact=total_contact

            for val in return_contact:
                del val['_id']

            output={'contact':str(return_contact),'result':result}

        return output

    #__________________________________________________________________________________________________________________________________


    def search_contact(self,data): # search contact by name or email adddress

        filter_value=data['Filter']
        
        number_of_contact_to_print=int(data['value_to_print'])

        collection=self.connect_collection()

        total_filter_contact=list(collection.find(filter_value))

        if(len(total_filter_contact)>=number_of_contact_to_print):

            result='{} contacts out of {} filter contact '.format(number_of_contact_to_print,len(total_filter_contact))

            return_contact=total_contact[0:number_of_contact_to_print+1]

            for val in return_contact:
                del val['_id']

            output={'contact':return_contact,'result':result}


        else:

            result='{} contacts out of {} filter contact '.format(len(total_filter_contact),len(total_filter_contact))

            return_contact=total_filter_contact
            for val in return_contact:
                del val['_id']

            output={'contact':return_contact,'result':result}

        return output
