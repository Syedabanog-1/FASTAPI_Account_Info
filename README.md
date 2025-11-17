
💳 FastAPI Bank Transfer App

This is a simple FastAPI application that simulates a basic banking system. It supports individual and multi-user authentication, balance checking, and bank transfers between users. Built with Python, FastAPI, and Pydantic, this project is ideal for beginners learning APIs, RESTful principles, and authentication workflows.

🚀 Features

*User Authentication*
---------------------

Authenticate a single user by name and PIN.
Authenticate multiple users simultaneously.

*Bank Transfer*
----------------

Transfer money from one user to another.
Validates authentication, user existence, and sufficient funds.

*Balance Check*
---------------

View balance for a single user.
Get updated account details for all users.

*Run the FastAPI server*
------------------------
uv run uvicorn account:app --reload

*Open your browser to view docs*
---------------------------------
http://127.0.0.1:8000/docs

🔗 API Endpoints
------------------

Method	   Endpoint	                   Description
POST	    /authenticate	          Authenticate one user
POST	    /authenticate-both	    Authenticate two users at once
POST	    /bank-transfer	        Transfer balance between users
GET	      /balance/{name}	        Check balance of a specific user
GET	      /update-accounts	     Get updated account details (both)

📌 Notes

The authentication is stored temporarily in memory using a Python set().
The user database is simulated using a Python dictionary.



https://github.com/user-attachments/assets/aa6a25d7-ecc3-4774-95c0-59667226f041

<img width="1607" height="903" alt="follow link " src="https://github.com/user-attachments/assets/e396e27e-956d-4560-8e75-3422bf640481" />

<img width="1610" height="904" alt="fastapi-running application" src="https://github.com/user-attachments/assets/8b07fddc-c5f0-43ae-8ed1-71e67a8c63d9" />

<img width="1609" height="904" alt="account-output" src="https://github.com/user-attachments/assets/5496a10c-8820-486f-adf8-b334ff8d985a" />

<img width="1610" height="905" alt="fastapi-code" src="https://github.com/user-attachments/assets/354c97a4-1cca-49a0-8e8d-253374a7b957" />

<img width="1613" height="901" alt="FASTAPI-helloworld" src="https://github.com/user-attachments/assets/ef96d56f-7d73-4577-9204-f460cbe4ce81" />

<img width="1609" height="901" alt="FASTAPI2" src="https://github.com/user-attachments/assets/71cd59ca-8bb7-4724-ab43-af23c78635d6" />

<img width="1612" height="903" alt="FASTAPI1" src="https://github.com/user-attachments/assets/a674544e-386b-47dc-9cfc-94a68efecaf9" />




