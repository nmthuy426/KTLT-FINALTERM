class User:
    def __init__(self,Fullname,Username,Password):
        self.Fullname=Fullname
        self.Username=Username
        self.Password=Password

    def __str__(self):
        return f"{self.Username} - {self.Password}"