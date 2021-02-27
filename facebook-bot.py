from fbchat import Client
from fbchat.models import Message

# facebook user credentials
username = "email.or.username"
password = "account.password"

# login
client = Client(username, password)

# get 20 users you most recently talked to
users = client.fetchThreadList()
print(users)

# get the detailed information about these users
detailed_users = [list(client.fetchThreadInfo(user.uid).values())[1] for user in users]

# sort by number of messages
sorted_detailed_users = sorted(detailed_users, key=lambda u: u.message_count, reverse=True)

# print best friend
best_friend = sorted_detailed_users[0]
print("Best friend: ", best_friend.name, "with a message count of", best_friend.message_count)

# message the best friend
client.send(Message(
    text=f"Congratulations {best_friend.name}, you are my best friend with {best_friend.message_count} messages!"),
            thread_id=best_friend.uid)

# get all users talked to in messenger in your account
all_users = client.fetchAllUsers()
print("you talked with a total of", len(all_users), "users!")

# logout
client.logout()
