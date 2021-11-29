import json
name=input('enter the name: ')
print('werlcome dear',name,"!!!")
print("1.signup")
print("2.login")
main_dict={}
list=[]
dict={}
user_info={}
option=int(input('enter the number(signup or login)___________________________ '))

if option==1:
    username=input('enter the name of the user:_____  ')
    password=input('enter the name of the password:_____  ')
    if ("a" in password or "b" in password or "c" in password or "d" in password or "e" in password or "f" in password or "g" in password or "h" in password or "i" in password or "j" in password or "k" in password or "l" in password or "m" in password or "n" in password or "o" in password or "p" in password or "q" in password or "r" in password or "s" in password or "t" in password or "u" in password or "v" in password or "w" in password or "x" in password or "y" in password or "z" in password) and ("A" in password or "B" in password or "C" in password or "D" in password or "E" in password or "D" in password or "E" in password or "F" in password or "G" in password or "H" in password or "I" in password or "J" in password or "K" in password or "L" in password or "M" in password or "N" in password or "O" in password or "P" in password or "Q" in password or "R" in password or "S" in password or "T" in password or "U" in password or "V" in password or "W" in password or "X" in password or "Y" in password or "Z" in password) and ("0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password) and ("@" in password or "#" in password or "$" in password or "&" in password):
        print('password is valid_____')
        try:
            with open("data.json","r") as output:
                user_data=json.load(output)        
        except:
            pass 
        comform_password=input('enter the comfirm password:_______ ')
        if password==comform_password:            
            if  ("data.json"):
                print("Congractstulations!!!",username,"You are signed up Succesfully","\U0001F929")
                description=input("Enter your Description:______ ")
                birth_date=input("enter Your Date Of Birth: __________")
                Gender=input("enter your Gender:__________ ")
                hobbies=input("Enter Your hobby:____________ ")
                try:
                    user_info["description"]=description
                    user_info["d_o_b"]=birth_date
                    user_info["Gender"]=Gender
                    user_info["Hobbies"]=hobbies
                    dict["Username"]=username
                    dict["Password"]=password
                    dict["Profile"]=user_info
                    list.append(dict)
                    main_dict["user"]=list
                    with open("data.json","r+") as file:
                        read_file= file.read()
                        userdata=json.loads(read_file)
                        for i in userdata:
                            if i =="user":
                                x=userdata[i]
                                x.append(dict.copy())
                                main_dict["user"]=x
                                json.dumps(main_dict,file)
                                file.close()
                except:
                    with open("data.json","w") as f:
                        f.write(json.dumps(main_dict, indent=4))
        else: 
            print('both passwords are not correct ')
    else:
        print("At least password should contain one Specail number or one digit")
# _____Login_______
elif option==2:
    username=input("enter your username: ")
    login_password=input("enter your Log in Password: ")
    with open("data.json","r") as login_file:
        login_info=json.load(login_file)
        for output_data in login_info["user"]:
            if output_data["Username"] == username and output_data["Password"]==login_password:
                print(username , "You Logged In Succesfully","\U0001F929")
                print("         PROFILE       ")
                print("___")
                print("Username",":",output_data["Username"])
                print("Gender",":",output_data["Profile"]["Gender"])
                print("Bio",":",output_data["Profile"]["description"])
                print("Dob",":",output_data["Profile"]["d_o_b"])
                break
        else:
            print("Password and username are Invalid")
else:
    print('you typed out of options')