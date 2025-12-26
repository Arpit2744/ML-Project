import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import numpy as np

# Import pipeline logic
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = FastAPI()

# Setup templates directory
templates = Jinja2Templates(directory="templates")

# Route 1: Home Page (Landing)
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route 2: Show the Prediction Form (GET)
@app.get("/predictdata", response_class=HTMLResponse)
async def predict_datapoint_get(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Route 3: Process the Prediction (POST)
@app.post("/predictdata", response_class=HTMLResponse)
async def predict_datapoint(
    request: Request,
    # The variable names here MUST match the 'name' attributes in HTML file
    gender: str = Form(...),
    race_ethnicity: str = Form(...),
    parental_level_of_education: str = Form(...),
    lunch: str = Form(...),
    test_preparation_course: str = Form(...),
    reading_score: float = Form(...),
    writing_score: float = Form(...)
):
    # Mapping HTML form data to our Backend Logic
    data = CustomData(
        gender=gender,
        race_ethnicity= race_ethnicity,  
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )
    
    # Convert incoming data to DataFrame
    pred_df = data.get_data_as_data_frame()
    print("Received Data as DataFrame:")
    print(pred_df)

    # Initialize Pipeline and Predict
    print("Starting Prediction...")
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    print(f"Prediction Result: {results[0]}")
    
    return templates.TemplateResponse(
        "home.html", 
        {"request": request, "results": round(results[0], 2)}
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)