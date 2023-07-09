

import pandas as pd
from pydantic import BaseModel
from joblib import load
from io import BytesIO

from sklearn.pipeline import Pipeline

from fraudes.python.metadata.paths import Paths
from fraudes.python.src.prepare import data_preparada
from fraudes.python.utils.prepocesar_data import prepocesar_data


def load_model() -> Pipeline:
    with open(Paths.model, "rb") as model_file:
        model = load(BytesIO(model_file.read()))
        print(model)
    return model


def transform_prediction(predict: int) -> str:
    if predict == 0:
        result = 'El insidente no es un Fraude!!!'
    else:
        result = 'El insidente puede ser un Fraude!!!'
    return result


def transform_request(class_model: BaseModel):
    transition_dictionary = {key: [value] for key, value in class_model.dict().items()}
    request_df = pd.DataFrame(transition_dictionary)

    fraudes_model = data_preparada()

    total_fraudes = pd.concat([fraudes_model, request_df])
    total_fraudes.drop('fraudfound_p', axis=1, inplace=True)
    total_fraudes.drop_duplicates(inplace=True)
    total_fraudes_pre = prepocesar_data(total_fraudes)

    request_new = total_fraudes_pre.tail(1)

    return request_new


