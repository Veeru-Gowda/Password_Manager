class PasswordManager:
    def __init__(self):
        self.__password=''

    def check_password(self,pa):
        if not self.__password:
            print("first give a new  password")
        elif pa==self.__password:
            print(True)
        else:
            print(False)
    def change_password(self,old_password,new_password):
        if old_password!=self.__password:
            print("incorrect current password!,try again (only 2 out of 3 chance left)")
        else:
            self.__password=new_password
            print("password updated")

    def new_password(self,set_password):
        self.__password=set_password

pm=PasswordManager()
pm.check_password("veeru")
pm.new_password('veeru')
pm.check_password('gg')
pm.check_password('veeru')
pm.change_password('veer','gowda')
pm.check_password('gowda')
pm.change_password('veeru','gowda')
pm.check_password("gowda")