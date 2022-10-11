import configparser

config = configparser.RawConfigParser()
config.read("../configurations/config.ini")

class ReadConfig:

    @staticmethod
    def getBaseURL():
        url = config.get("common login info", "baseURl")
        return url

    @staticmethod
    def getUserID():
        userID = config.get("common login info", "userID")
        return userID

    @staticmethod
    def getPassword():
        password = config.get("common login info", "password")
        return password

    @staticmethod
    def getXcel():
        path = config.get("excel path", "path")
        return path