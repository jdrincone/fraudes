import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler


def prepocesar_data(X: pd.DataFrame) -> pd.DataFrame:
    """Se estandarizan las columnas numéricas y se hace one-hot-encoding de las
        columnas cualitativas. Para mantener las columnas a las que no se les aplica
        ninguna transformación se tiene que indicar remainder='passthrough'.

    Args:
        X: data que ha pasado los filtros de limpieza.

    Return:
        Data preposeceda lista para generar modelos
    """

    numeric_cols = X.select_dtypes(include=["int64", "int"]).columns.to_list()
    cat_cols = X.select_dtypes(include=["object", "category"]).columns.to_list()
    preprocessor = ColumnTransformer(
        [
            ("scale", StandardScaler(), numeric_cols),
            ("onehot", OneHotEncoder(handle_unknown="ignore", sparse=False), cat_cols),
        ],
        remainder="passthrough",
    )

    X_prep = preprocessor.fit_transform(X)
    # Convertir el output en dataframe y añadir el nombre de las columnas
    encoded_cat = preprocessor.named_transformers_["onehot"].get_feature_names_out(
        cat_cols
    )
    labels = np.concatenate([numeric_cols, encoded_cat])
    datos_prep = pd.DataFrame(X_prep, columns=labels)

    return datos_prep
