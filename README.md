# Nicklas Martin

**CS178: Cloud and Database Systems — Project #1**
**Author:** Nick Martin
**GitHub:** nicklasmartin038-dot

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
- 

---

## Project Structure

```
ProjectOne/
├── flaskapp.py          # Main Flask application — routes and app logic
├── dbCode.py            # Database helper functions (MySQL connection + queries)
├── creds_sample.py      # Sample credentials file (see Credential Setup below)
├── templates/
│   ├── home.html        # Landing page
│   ├── [other].html     # Add descriptions for your other templates
├── .gitignore           # Excludes creds.py and other sensitive files
└── README.md
```

---

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies:

   ```bash
   pip3 install flask pymysql boto3
   ```

3. Set up your credentials (see Credential Setup below)

4. Run the app:

   ```bash
   python3 flaskapp.py
   ```

5. Open your browser and go to `http://127.0.0.1:8080`

---

## How to Access in the Cloud

The app is deployed on an AWS EC2 instance. To view the live version:

```
http://[your-ec2-public-ip]:8080
```

_(Note: the EC2 instance may not be running after project submission.)_

---

## Credential Setup

This project requires a `creds.py` file that is **not included in this repository** for security reasons.

Create a file called `creds.py` in the project root with the following format (see `creds_sample.py` for reference):

```python
# creds.py — do not commit this file
host = "your-rds-endpoint"
user = "admin"
password = "your-password"
db = "your-database-name"
```

---

## Database Design

### SQL (MySQL on RDS)

<!-- Briefly describe your relational database schema. What tables do you have? What are the key relationships? -->

**Example:**

- `[TableName]` — stores [description]; primary key is `[key]`
- `[TableName]` — stores [description]; foreign key links to `[other table]`

The JOIN query used in this project: <!-- describe it in plain English -->

### DynamoDB

<!-- Describe your DynamoDB table. What is the partition key? What attributes does each item have? How does it connect to the rest of the app? -->

- **Table name:** `[your-table-name]`
- **Partition key:** `[key-name]`
- **Used for:** [description]

---

## CRUD Operations

| Operation | Route      | Description    |
| --------- | ---------- | -------------- |
| Create    | `/[route]` | [what it does] |
| Read      | `/[route]` | [what it does] |
| Update    | `/[route]` | [what it does] |
| Delete    | `/[route]` | [what it does] |

---

## Challenges and Insights

<!-- What was the hardest part? What did you learn? Any interesting design decisions? -->

---

## AI Assistance

<!-- List any AI tools you used (e.g., ChatGPT) and briefly describe what you used them for. Per course policy, AI use is allowed but must be cited in code comments and noted here. -->
