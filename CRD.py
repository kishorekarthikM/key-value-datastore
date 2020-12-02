import time

k={} #'k' is the dictionary

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional
def create(key,value,timeinsec=0):
    if key in k: #checking for key in dictionary
        print("error: The given key already exists in database") #error message
    else:
        if(key.isalpha()):
            if k.__sizeof__()<(1024*1024*1024) and value.__sizeof__()<=(16*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB
                if len(key) <= 32:  # constraints for input key_name capped at 32chars
                    if timeinsec==0:
                        m=[value,0]
                    else:
                        m=[value,time.time()+timeinsec]#summing the given timeout with current time in seconds
                    k[key]=m #adding key and value to the dictionary
                else:
                    print("error: The given key has more than 32 characters")#error message
            else:
                print("error: Memory limit exceeded! ")#error message
        else:
            print("error: Key must contain only alphabets")#error message

#for read operation
            
def read(key):
    if key not in k: #checking for key in dictionary
        print("error: The given key does not exist in database. Please enter a valid key") #error message
    else:
        s=k[key]
        if s[1]!=0:
            if time.time()<s[1]: #comparing the present time with expiry time
                print(key+":"+str(s[0])) # The given key with its value is printed
            else:
                print("error: time-to-live of",key,"has expired") #error message
        else:
            print(key+":"+str(s[0]))

#for delete operation

def delete(key):
    if key not in k: #checking for key in dictionary
        print("error: The given key does not exist in database. Please enter a valid key") #error message
    else:
        s=k[key] #Assigning value of key to variable 's'
        if s[1]!=0:
            if time.time()<s[1]: #comparing the current time with expiry time
                del k[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del k[key]
            print("key is successfully deleted")