class ManagerInterface:
    def __init__(self, db_path):
        print("Init")

    def create(self, data):
        print("Parent method")

    def retrieve(self, data):
        print("Common method")

    def update(self, data):
        print("Common method")