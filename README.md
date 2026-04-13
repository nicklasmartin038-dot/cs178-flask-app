# Nicklas Martin

**CS178: Cloud and Database Systems — Project #1**
**Author:** Nick Martin
**GitHub:** nicklasmartin038-dot
**proposed score** 95/100
---

## Overview
I like to watch movies with my frends and I often have movie nights with them, but i have alot of frends so It can get hard remembering what types of genres of movies all my frends like. So for this project, I made a database ware I can store my frends first_name, last_name, and genre. I have added delete_user, for when I stop being frends with somone, Update_user, for when I need to changes a frends name or genre. add_user, for when I make a new frend to add to the database. Display_all_users, so I cann see a table of all my frends and there favorate movie genre, and a serch my genre, for when I am in the mood for a specific movie and need to see who I should call

---
## Technologies Used
- **Flask** — Python web framework
- **AWS EC2** — hosts the running Flask application
- **AWS RDS (MySQL)** — relational database for storing user information (like name and genre preferances)
- **AWS DynamoDB** — non-relational database for for storesing more flexable and more unstructured data.
- **GitHub Actions** — auto-deploys code from GitHub to EC2 on push
- **Chatgpt** -Used mostely to help me when I got stuck on errors and when writing code


## Website instructions
When you open up my website you will see a homepage with 5 buttons. (delete user, add user, update user, show all users, and serche genre) The delete user button allowes you to remove a user from the list. The add user button allowes you to ass a user. The update user button allowes you to change the atrebutes of a allready created user. the serch genre button allowes you to serch the users favorate movie genre (so we know who to invite to movie night!" and the display all users button shows you a table of all the users in your database. If you want to go back to whare you were you can simply puch the back arrow in your serch engine and it will take you back to your orevius page!

### SQL (MySQL on RDS)

The JOIN query used in this project: I did not use JOIN in my project for the sake of time

### DynamoDB

- **Table name:** `User Log`
- **Partition key:** `activity_id`
- **Used for:** monotering the changes/activity on my website/database

---

## CRUD Operations

| Operation | Route      | Description    |
| --------- | ---------- | -------------- |
| Add User    | `/add-user` | Adds a new user to the database with first name, last name, and favorite genre |
| Display All users| `/display-users` |  Retrieves and displays all users from the database |
| Update User  | `/update-user` | Updates an existing user’s information in the database |
| Delete user   | `/delete-user` | Removes a user from the database based on their name |

---

## Challenges and Insights
One challenge was getting AWS services like EC2, RDS, and DynamoDB to work together and troubleshooting connection issues. From this project, I learned how to build and deploy a Flask app, connect it to databases, and manage cloud resources securely.

---

## AI Assistance
I only used chatgpt, I mostly used it to help me get back on track when I had errors/problems, I also used it to help me write and fix some of my code. expesialy the HTML code as I am the least confident in HTML.
