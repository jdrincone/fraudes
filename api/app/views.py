from api.app.models import PredictionRequest
from api.app.utils import load_model, transform_request, transform_prediction


model = load_model()


def get_prediction(request: PredictionRequest) -> str:
    data_to_predict = transform_request(request)
    prediction = model.predict(data_to_predict)[0]
    prediction = transform_prediction(prediction)

    return prediction

