
# project

import sys
import random
import time

def get_info():
    name = input("Enter Your Name :")
    age = input("Enter Your Age :")
    gender = input("Enter Your Gender :")
    qualification = input("Enter Your Qualification :")
    mail_id = input("Enter Your Mail Id :")
    print("Thank you for your Information ")

    return [name,age,gender,qualification,mail_id]

def generate_otp():
    otp = random.randint(1000,9999)
    return otp

def read_data():
    file = open("peoples_data.txt","a+")
    file.seek(0)
    read_file = file.read()

    file.close()
    return read_file


def write_data():
    info = get_info()
    uniq_code = generate_otp()
    file_data = read_data()

    file = open("peoples_data.txt","a+")
    if str(uniq_code) not in file_data:
        file.write("\n")
        file.write(f"Uniq Code : {uniq_code} for {info[0]}")
        print(f"Uniq Code : {uniq_code} for {info[0]}")

        file.write("\n")
        file.write(f"Name : "+info[0])

        file.write("\n")
        file.write(f"Age : "+info[1])

        file.write("\n")
        file.write(f"Gender : "+info[2])

        file.write("\n")
        file.write(f"Qualification : "+info[3])

        file.write("\n")
        file.write(f"mail_id : "+info[4])
        file.write("\n")
        file.close()
    else:
        print("Retry")
        write_data()

    print("######################################################################")

        
def search_data():
    otp = input("Enter Your Uniq Code :")
    print("\n")
    file = open("peoples_data.txt","a+")

    file.seek(0)

    data = file.readlines()
    #print(data)

    for element in data:
        if otp in element:
            position = data.index(element)
            #print(position)
            file_d = data[position : position+7]
            #print(file_d)
            print("".join(file_d))
    
    
    if otp not in data:
        print("Your Code is not present ,check your code")

    print("##############################################")
    




def main():
    print("Choose Your Options \n1 - Insert Data \n2 - Read All Data\n3 - Read with uniq Code")
    print("4 - Exit")

    # take input from user
    try:
        user_value = int(input("Enter your choice :"))
       

        if user_value == 1:
            print("####################### Insert Data ######################\n")
            write_data()

            return main()

        elif user_value == 2:
            file_data = read_data()
            print("####################### Read All Data ######################\n")
            print("Wait Data is fetching ")
            time.sleep(1)

            if (file_data is None) or (file_data ==""):
                print("No data Available in database File \n Thank You\n")
            else:
                print(file_data)
                print("\n")
            print("############################################################\n")
            

            return main()

        elif user_value == 3:
            print("####################### Search Data ######################\n")
            search_data()
            

            return main()

        elif user_value == 4:
            print("Exit")

        else:
            print("invalid choice ")
            
            return main()
    except ValueError:
        sys.stderr.write("Enter Only Number ...\n")
        return main()



main()