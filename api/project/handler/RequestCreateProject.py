class RequestCreateProject:
    def __init__(self, name):
        self.name = name
        
    def do(self):
        return "create-project {}".format(self.name)