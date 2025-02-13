class Student:
    def __init__(self,id,user_name):
        self.id = id
        self.user_name = user_name
        self.followers = 0
        self.following = 0
    def follow(self,user):
        self.following +=1
        user.followers +=1

user_1 = Student("001","Denzel")
user_2 = Student("002","john")

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)