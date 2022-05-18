import user
## or
from user import User
from post import Post

# Create an Object | Construct a new Object from the User Class
## whenever we call a Class, in the background, his own __init__ function will be called and it requires the parameters defined in the Class
### import user
app_user_one = user.User("csskypper@.com", "CS Skypper", "password", "DevOps") ## and we have to provide all of those parameters
app_user_one.get_user_info()

app_user_one.change_job_title("DevOps Engineer")
app_user_one.change_email("csskypper@yahoo.com")
app_user_one.get_user_info()

### from user import User
app_user_two = User("ciao@ciao.it", "Ciao Ciao", "CiaoCiao", "Multimedia Manager lol")
app_user_two.get_user_info()


new_post = Post("On a secret mission today. Stay tuned to learn more", app_user_two.name)
new_post.get_post_info()
