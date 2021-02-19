banned_users = ['katie','phil', 'trish', 'daryl', 'megan', 'marti', 'cindy', 'kat']
user = 'jessica'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# This is to check whether a value is not in a list. Line 1 is a list of banned users. Line 2 is a new user. Since Jessica isn't in the list of banned users, she is invited to post a response.