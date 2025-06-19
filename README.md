# 🔐 Password Manager (Python)

This is a basic **Password Manager** built in Python by **Veeru**.  
It uses object-oriented programming concepts, especially **encapsulation**, to handle password management securely and interactively.

---

## 🚀 Features

- Set a **new password**
- **Check** if a password matches the current one
- **Change** the password using the correct current password
- Private password attribute using **encapsulation**

---

## 🧑‍💻 Code Overview

```python
class PasswordManager:
    def __init__(self):
        self.__password = ''

    def check_password(self, pa):
        ...

    def change_password(self, old_password, new_password):
        ...

    def new_password(self, set_password):
        ...
