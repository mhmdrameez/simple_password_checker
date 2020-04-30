user_name=input("Enter your name:")
password=input("Enter the password:")
pass_length=len(password)
hidden_pass='*' * pass_length
print(f'{user_name},Your password "{hidden_pass}" is {pass_length} letter long')
