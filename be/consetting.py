class Setting():
    def GetConectionString(self):
        with open("connection.txt") as f:
            return str(f.read())