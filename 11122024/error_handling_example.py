def save_user_data(username, age):
    #username must be letters
    #age must be between 18 to 150
    try:
        if not username.isalpha():
            raise ValueError("username must contain only letters!")
        user_age = int(age)
        if user_age < 18 or user_age >150:
            raise ValueError("age must be between 18 and 150")
        
        with open("users.txt", "a") as file:
            file.write(f"{username}, {user_age}\n")
    except ValueError as e:
        print(e)
    except IOError:
        print("File read/write error")
    except:
        print("unknown error occurred")
    else:
        print("User saved successfully")
    finally:
        print("Thank you for using our program")



save_user_data("azmainadel", 27)
save_user_data("azmainadel123", 27)