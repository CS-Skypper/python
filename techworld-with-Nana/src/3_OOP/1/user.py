# User class

"""
The flow will be:
  1. Object will be created with initial values
    tom = User("tt@tt.com", "Tom", "pwd", "Developer")
      so the object will be created
  2. Call funtion on that Object to change its password
"""

class User:
  # all of the logic beneath is called "Class body"
  # then we have the init constructor that sets the initial values for the class atributes whenever we create a specific Object for that class; when we "construct a new object". Then on that Constructed Object we can change_password; change_job_title
  # functions that belongs to a Class are called methods
  # User Class gives us 2 Methods

  # class definition
  ## attributes for the class. attributes have no value. the values will be set when we will create an objoect from the class
  ## we need a function that will take these values and assign to the object created from the class
  def __init__(self, email, name, password, current_job_title):  # this __init__ function is a constructor; self -> refers to the current instance of the class;
    ### email, name, password, current_job_title -> are reference parameters, they could be anything else. constitution says: use the same as in the attributes of the class (self.email)
    self.email = email # instead after the "=" the value of the attributes must be the same
    self.name = name
    self.password = password
    self.current_job_title = current_job_title 
  
  ## some behavior
  ### if I don't get it wrong, self as first parameter in the function is needed so the function can access attributes on that class in that function
  def change_password(self, new_password): # Methon must have a first parameter, usually called 'sefl'
    self.password = new_password
  
  def change_job_title(self, new_job_title):
    self.current_job_title = new_job_title
  
  def change_email(self, new_email):
    self.email = new_email

  def get_user_info(self):
    print(f"User {self.name} currently works as a {self.current_job_title}. Can be contacted at {self.email}")
