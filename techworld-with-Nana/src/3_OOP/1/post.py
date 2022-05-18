class Post:
  def __init__(self, messagge, author):
    self.messagge = messagge
    self.author = author

  def get_post_info(self):
    print(f"Post: {self.messagge} written by {self.author}")
