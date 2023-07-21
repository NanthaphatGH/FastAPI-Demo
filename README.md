# FastAPI-Demo
Create FastAPI using MongoDB, this project required a Mongodbcompass program to create a simple database.

1. Create a virtual environment name [env] by using the command --> python -m venv env   
2. (Begin here)Activate scripts using the command --> .\env\Scripts\activate
3. Install uvicorn in the Terminal--> pip install fastapi uvicorn
4. Install library pymongo --> pip install pymongo 
5. Open the Mongodbcompass program and connect to URI(mongodb://localhost:27017)
6. Back to the terminal and initiate API --> uvicorn main:app --reload
7. Use the Postman program to manage the information in the database by using this URL --> http://127.0.0.1:8000/votes/

