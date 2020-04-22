name=input('enter your name')
password=input('enter the password')
password_length=len(password)
hidden_password='*' * password_length
print(f'{name}, your password ,{hidden_password}, is {password_length} letters long')
