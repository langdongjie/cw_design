import pickle


# pkl_file = open('../data.pkl', 'rb')
# print(pickle.load(pkl_file).items())
# pkl_file.close()

class LoginManager:
    def __init__(self):
        self.user_dict = {}

    def login(self, user, pwd):
        pkl_file = open('./my_app/data.pkl', 'rb')
        self.user_dict = pickle.load(pkl_file)
        pkl_file.close()
        if self.user_dict.__contains__(user):
            return str(self.user_dict[user]).__eq__(str(pwd))
        return False

    def register(self, user, email, pwd):
        self.user_dict[user] = pwd
        self.user_dict[email] = pwd
        pkl_file = open('./my_app/data.pkl', 'wb')
        pickle.dump(self.user_dict, pkl_file)
        pkl_file.close()


