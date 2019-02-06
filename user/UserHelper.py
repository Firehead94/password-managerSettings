import json
import os
import settings.config
import uuid
import user.User

################################################################
#
# Contains static methods to assist with user file management
# on local storage. Use update_user when creating new
# user
#
################################################################


class UserHelper:

    # Delete passed User username
    @staticmethod
    def delete_user(username):
        os.remove(settings.config.storage["path" + settings.config.osType] + username + ".txt")

    # Get a user using username and returns user object
    @staticmethod
    def get_user(username):
        with open(settings.config.storage["path" + settings.config.osType] + username + ".txt") as file:
            user = json.load(file)
        file.close()
        retuser = user.User(user)
        return retuser

    # Update User Objects
    @staticmethod
    def update_user(currentuser):
        if isinstance(currentuser, user.User):
            with open(settings.config.storage["path" + settings.config.osType] + currentuser.user["username"]+".txt", "w") as outfile:
                json.dump(currentuser.user, outfile)
            outfile.close()
            return True
        return False

    # Get uuid object, use str(UserHelper.User.getUUID())
    # if you need a string of the hex value
    @staticmethod
    def getUUID():
        return uuid.uuid1()

