from dbhelper import DBHelper

def main():
    db = DBHelper()
    while True:
        print()
        print("********WELCOME*********")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all the users")
        print("PRESS 3 delete the user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit")
        print()
        try:
            choice = int(input())
            if(choice==1):
                #Insert new user
                uid = int(input("Enter user ID: "))
                username = input("Enter user name: ")
                userphone = input("Enter user phone no: ")
                db.insert_user(uid,username,userphone)            
            elif choice==2:
                #display all users
                db.fetch_all()
            elif choice==3:
                #delete the user
                uid = int(input("Enter user ID to deleted: "))
                db.delete_user(uid)
                pass
            elif choice==4:
                #update the user
                uid = int(input("Enter user ID: "))
                username = input("Enter new user name: ")
                userphone = input("Enter new user phone no: ")
                db.update_user(uid,username,userphone)
                pass
            elif choice==5:
                #exit from the program
                break
            else:
                print("Invalid input ! try again")
        except Exception as e:
            print(e)
            print("Invalid type of input exception thrown")
if __name__== "__main__":
    main()
