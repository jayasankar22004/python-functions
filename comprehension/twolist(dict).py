usernames = ["charan", "rahul", "priya", "sneha"]
passwords = ["abc123", "xyz456", "pqr789", "hello123"]
users = {usernames[i]: passwords[i] for i in range(len(usernames))}
print(users)