from __db__ import Connect
from __field__ import Field
from __model__ import Model
import Models.UsersModel as Model

def main():
    # Creating the table with the same name "user":
    Model.Users.create_table()

    # Creation of User:
    user = Model.Users(ID=1, NAME="ASHRAF", LAST_NAME="KHABAR", CNE="152SDF53", EMAIL="khabarachraf@gmail.com")
    user.save()

    # Updating the user:
    user.name = "ASHRAF"
    user.update()

    # Getting an element based on a parameter:
    # Assuming you have a Users model
    user1 = Model.Users.get(NAME="ASHRAF")  # Retrieve the user with ID 1

    if user1:
        print("User found:")
        print(f"ID: {user1.ID}")
        print(f"Name: {user1.NAME}")
        print(f"Last Name: {user1.LAST_NAME}")
        print(f"CNE: {user1.CNE}")
        print(f"email: {user1.EMAIL}")
    else:
        print("User not found.")


if __name__ == "__main__":
    main()

