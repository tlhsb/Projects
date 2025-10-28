
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.posts = []
    
    def create_post(self, content):

        new_post = Post(content, self)
        self.posts.append(new_post)
        return new_post


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
    
    def __str__(self):
        return f"comment: {self.content} (author: {self.author.username})"


if __name__ == "__main__":

    user1 = User("zzz", "zzz@xx.com")
    user2 = User("XDD", "XDD@xx.com")
    

    post1 = user1.create_post("Hello,nice to meet u")
    post2 = user1.create_post("Do you play video games?")
    post3 = user2.create_post("zzzzzzzz")
    
    
    print(f"comment of {user1.username}  ({len(user1.posts)}):")
    for i, post in enumerate(user1.posts, 1):
        print(f"  {i}. {post}")
    
    print(f"\n comment of {user2.username} ({len(user2.posts)}):")
    for i, post in enumerate(user2.posts, 1):
        print(f"  {i}. {post}")
    
    print(f"User: {user1.username}")
    print(f"Email: {user1.email}")
    print(f"Posts number: {len(user1.posts)}")



