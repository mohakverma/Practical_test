from fastapi import FastAPI, Request 
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pandas as pd
import sqlite3
import uvicorn
from fastapi.templating import Jinja2Templates

# Loading the dataset
titanic_df = pd.read_csv('data/titanic.csv')

# Initializing app
app = FastAPI()
templates = Jinja2Templates(directory="templates") #for HTML templates

class Passenger(BaseModel):
    PassengerId: int
    Survived: int
    Pclass: int
    Name: str
    Sex: str
    Age: float
    SibSp: int
    Parch: int
    Ticket: str
    Fare: float
    Cabin: str = None
    Embarked: str

# Connects to SQLite database
conn = sqlite3.connect('titanic.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS passengers (
    PassengerId INTEGER PRIMARY KEY,
    Survived INTEGER,
    Pclass INTEGER,
    Name TEXT,
    Sex TEXT,
    Age REAL,
    SibSp INTEGER,
    Parch INTEGER,
    Ticket TEXT,
    Fare REAL,
    Cabin TEXT,
    Embarked TEXT)
''')

# Fill data from CSV to SQLite
cursor.execute("SELECT count(*) FROM passengers")
if cursor.fetchone()[0] == 0:
    titanic_df.to_sql('passengers', conn, if_exists='replace', index=False)


# API endpoint to get all passenger data
@app.get("/titanic/")
async def get_all_passengers():
    cursor.execute("SELECT * FROM passengers")
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    result = [dict(zip(columns, row)) for row in rows]
    return result if result else {"message": "No passengers found"}

# Extra endpoitns for Additional functionality:
# API endpoint to get all passenger data in HTML Table format
@app.get("/titanic/table/", response_class=HTMLResponse)
async def get_all_passengers(request: Request):
    cursor.execute("SELECT * FROM passengers")
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    passengers = [dict(zip(columns, row)) for row in rows]
    return templates.TemplateResponse("passengers.html", {"request": request, "passengers": passengers})

# API endpoint to get passenger data by ID
@app.get("/titanic/{passenger_id}")
async def get_passenger(passenger_id: int):
    cursor.execute("SELECT * FROM passengers WHERE PassengerId=?", (passenger_id,))
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    result = [dict(zip(columns, row)) for row in rows]
    return result if result else {"message": "No passengers found"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
