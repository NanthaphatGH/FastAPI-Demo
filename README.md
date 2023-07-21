# FastAPI-Demo
Create FastAPI using MongoDB, this project required a Mongodbcompass program to create a simple database.

1. Create a virtual environment by using the command --> python -m venv
2. Activate scripts using the command --> .\env\Scripts\activate
3. Install Uvicorn in the Terminal--> pip install fastapi uvicorn
4. Open the Mongodbcompass program and connect to URI(mongodb://localhost:27017)
5. Back to the terminal and initiate API --> uvicorn main:app --reload
6. Use the Postman program to manage the information in the database by using this URL --> http://127.0.0.1:8000/votes/

