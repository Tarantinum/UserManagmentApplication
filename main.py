# 3-tiers architecture
# we have 2 ways to do the layers :
# 1. in previous course we did this project using directory and creating folders
# 2. Using python package . a python package is a folder .
# the difference between python package and a directory is that there is a __init__.py file in python package
# this __init__ file means create an instant to the python interpreter
# First we create layering : presentation layer , business layer , data access layer , common layer
# Second we should create the database , using sqlite >> creating a text document in source folder >> change the suffix to .db
# >> create a database file >> because it is already empty we use SQlite to create Data in it
# After creating needed tables and columns on database using SQlite , then we add data in the file .
# Now we are going to bring the Data into our program
# the program is a login page . when it is being opening it will show us the username and lastname entries
# for first step we will go on Common layer


# the implantation of presentation layer is going to be based on MultiFrameApplication
# in this way we only have one Frame . and each page of our software application should be a Frame
# A frame is a container that can hold button , entry , label ,... in itself . so it looks like a form
# it doesn't have the nature separation from the form for example it doesn't have the minimize and maximize button . you cannot open it, but you can place on the form
# but how should we manage this frames ? as we said we need a frame for each page ?
# there is an intermediate layer called Coordinator
# in Coordinator we have both form and different frames . and its duty is that to manage which form should be displayed on the frame
# this is possible by using the inheritance class
# This implementation is going to be in the presentation layer
# Note that all the frames should be responsive it means that all the frame should be placed on row zero and column 0
# we give all the frame nswe stickies


# Role Base Authentication :We have different users with different access levels like simple user or admin.
# So our treatment toward each one should be different . ( Home page for admin is different from home page for a normal user )
# So we are going to create different access level for different users
# for this aim we need to make some changes toward sqlite
# top to now we had only one table (user table ) with his information . this time we add a "role " table
# this table is going to have id and a title columns
# After creating this table , we should make a connection between user and role inorder to define role of each user
# we add a new column in user table : role_id
# with : Not null >> Default ( set as 2 it means each user that is already in the db is a default user )
# make connection using foreign key >> Role table >> id column
# note that if you do any edite such as adding new columns to a table , your db will fist make a backup of the current statues then put it in the temp_table
# after that destroy the current table and add the backup to the table and destroy the temp table . it means that it a high performance needed job
# this work will down your program, so you should consider a downtime for large databases .


# After crating a special page for the admin entrance, next step is to create UserManagement page for admin
# we create a file for this in Presentation layer in Frame Directory

# a security hint: if your database is stored in such a way that access to people password is plain , the risk of hacker
# gaining full access to your user's information is much higher
# for preventing this , we need to do some changes on how to save passwords
# A method to prevent is to use " hash MD5 "
# it is an algorithm that receives a value and convert it to another value . but the point is that you can not switch hash to its original value
# so hash is a one-way convertor. if you need a 2 way one , use encryption (encryption) and decryption (decryption) ( with a ket you can convert )
# So if the hacker access the key , he has everything !
# our preference is to use hashing method
#  when a user enters his password , first we convert it to a hash code then save the hash code to the database
# the reason of insist on not having simple passwords is that there are some common hash codes that can be easily be identified
# first step : by use of a md5 convertor , we convert all the user's passwords in our db
# But it is obvious that user can not enter the application from now on by his original password .




# from BusinessLayer.user_business_logic import UserBusinessLogic
#
# user_business_logic = UserBusinessLogic()
# response = user_business_logic.login("Ali123","123")
#
# if response.success :
#     print ( f"welcome {response.data.username}")
# else:
#     print(response.message)


# from PresentationLayer.window import Window
# window = Window()
# window.show()

from PeresntationLayer.main_view import MainView

MainView()
