class Role:
    def __init__(self,id,title):
        self.id=id
        self.title=title


    def get_information(self):
        return f"{self.id}_{self.title}"
