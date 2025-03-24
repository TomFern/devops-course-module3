# this file contains a SQL injection vulnerability

def get_user_data(username):
    # Vulnerable to SQL injection due to unsanitized input
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    # Simulated execution of the query
    print("Executing query:", query)


if __name__ == "__main__":
    get_user_data("admin'; DROP TABLE users; --")
