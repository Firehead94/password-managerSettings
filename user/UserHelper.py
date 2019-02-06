import json
import os


class UserHelper:

    # Create New User Object
    @staticmethod
    def new_user(currentuser):
        with open(currentuser["username"]+".txt", "w") as outfile:
            json.dump(currentuser, outfile)
        outfile.close()

    # Delete passed User UUID
    @staticmethod
    def delete_user(username):
        os.remove(username + ".txt")

    # Get a user using username and returns user dictionary
    @staticmethod
    def get_user(username):
        with open(username + ".txt") as file:
            user = json.load(file)
        file.close()
        return user

    # Update User Objects
    @staticmethod
    def update_user(currentuser):
        with open(currentuser["username"]+".txt", "w") as outfile:
            json.dump(currentuser, outfile)
        outfile.close()
