from fastapi import FastAPI

from api.app.models import PredictionResponse, PredictionRequest
from api.app.views import get_prediction

app = FastAPI(docs_url="/", title='Reto Fraudes Juan David Rincón')


@app.post("/v1/predición si un insidente es un fraude")
async def make_model_prediction(request: PredictionRequest):
    return PredictionResponse(fraudfound_p=get_prediction(request))
