# Dictionary to store user credentials
users_db = {}

def sign_up(username, password):
    """
    Simulates a sign-up function.

    Args:
        username (str): The username for sign-up.
        password (str): The password for sign-up.

    Returns:
        str: Success or failure message.
    """
    if username in users_db:
        return "Username already exists. Please choose a different username."
    if len(password) < 6:
        return "Password must be at least 6 characters long."
    
    users_db[username] = password
    return "Sign-up successful!"

def login(username, password):
    """
    Simulates a login function.

    Args:
        username (str): The username for login.
        password (str): The password for login.

    Returns:
        str: Success or failure message.
    """
    if username in users_db and users_db[username] == password:
        return "Login successful!"
    return "Invalid username or password."

def sum_two_values(a, b):
    """
    Returns the sum of two values.

    Args:
        a (int or float): The first value.
        b (int or float): The second value.

    Returns:
        int or float: The sum of the two values.
    """
    return a + b

# Example usage
if __name__ == "__main__":
    # Sign-up examples
    print(sign_up("admin", "password123"))  # Expected: Sign-up successful!
    print(sign_up("admin", "pass"))         # Expected: Password must be at least 6 characters long.
    print(sign_up("admin", "newpass"))      # Expected: Username already exists.

    # Login examples
    print(login("admin", "password123"))    # Expected: Login successful!
    print(login("user", "pass"))            # Expected: Invalid username or password.

    # Sum examples
    print(sum_two_values(10, 20))           # Expected: 30
    print(sum_two_values(3.5, 4.5))         # Expected: 8.0
