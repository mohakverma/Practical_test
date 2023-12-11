#1. Creating an API Endpoint

This application is built using FastAPI anf provides a RESTful API to interact with the Titanic dataset. It includes endpoints to retreive all passenger records, a visually formatted HTML table of all passengers and an endpoint retrieve individual passenger records.

##Installation and Setup
###Requirements

Install the necessary dependencies by running:
```
pip install -r requirements.txt
```

###Running the Application
To start the server, run the following command in the terminal:
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at http://localhost:8000.

##API Endpoints
### 1. Get All Passengers (/titanic/)
Retrieves a JSON list of all passengers in the Titanic dataset.
Usage: http://localhost:8000/titanic/
### 2. Get Passenger by ID (/titanic/{passenger_id})
Retrieves details of a specific passenger by their Passenger ID.
Usage: http://localhost:8000/titanic/{passenger_id}
Example: http://localhost:8000/titanic/1
### 3. View Passengers in HTML Table (/titanic/table/)
Displays all passenger data in a formatted HTML table.
Usage: http://localhost:8000/titanic/table/

##Project Structure
- main.py: Contains the FastAPI application code
- templates/: Contains HTML templates for rendering data
- data/titanic.csv: The Titanic dataset
- requirements.txt: Contains requirements file
- README.md: Project documentation

#2. Parsing
Code for parsing the given ubo.json file is present in parsing.py

To run:
```
python parsing.py
```

This will generate a tabular dataframe printed and saved in csv format in ubo.csv.