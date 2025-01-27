def login(username, password):
    if password == "password123":
        return "Login successful!"
    return "Invalid username or password."

def sum_two_values(a, b):
    
    return a+b

if __name__ == "__main__":
    print(login("admin", "password123"))  
    print(login("user123", "pass"))       

    print(sum_two_values(10, 20))         
    print(sum_two_values(3.5, 4.5))       
    print(sum_two_values(-5, 10))         
