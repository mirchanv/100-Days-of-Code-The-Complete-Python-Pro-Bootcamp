from prettytable import PrettyTable

# Creating a class called User
class User:

    # constructor to initialize starting values of new User objects
    # self is the actual object being created/initialized
    def __init__(self, user_id, pwd):
        print("constructor called")
        self.user_id = user_id
        self.pwd = pwd
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def account_summary(self):
        table = PrettyTable()
        table.field_names = ["Account", "Password", "Followers", "Following"]
        table.add_row([f"{self.user_id}", f"{self.pwd}", f"{self.followers}", f"{self.following}"])
        print(table)


user_1 = User("j_Bond", "007")
user_2 = User("TheRealMj", 23)

user_1.follow(user_2)
user_1.account_summary()
user_2.account_summary()


