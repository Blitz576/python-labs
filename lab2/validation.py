import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validation():
    user_name = input("Enter your name: ")
    if user_name == "" or not user_name.isalpha():
        return "Please enter a valid username";
    else:
      user_email = input("Enter your email address:");
      if is_valid_email(user_email):
          return [user_email,user_name];
      else: return "Please enter a valid email address";



print(validation());