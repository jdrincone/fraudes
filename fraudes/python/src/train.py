import logging
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from fraudes.python.src.prepare import data_preparada
from fraudes.python.utils.prepocesar_data import prepocesar_data
from fraudes.python.utils.info_model import update_model, save_simple_metrics_report, image_confusion_matrix

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def train_model():
    logging.info("Loading Data preprocesada...")
    fraudes_model = data_preparada()
    X = prepocesar_data(fraudes_model)
    X.drop("fraudfound_p", axis=1, inplace=True)
    y = fraudes_model.fraudfound_p.astype("int")

    logger.info("Separating dataset into train and test")
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2023)

    modelo = DecisionTreeClassifier(max_depth=32, criterion="gini", random_state=2023)
    modelo.fit(X_train, y_train)

    predicciones = modelo.predict(X=X_test)

    conf_matrix = confusion_matrix(y_true=y_test, y_pred=predicciones)
    logger.info(f"confusion_matrix: {conf_matrix}")
    image_confusion_matrix(y_test, predicciones)

    accuracy = accuracy_score(y_true=y_test, y_pred=predicciones, normalize=True)
    logger.info(f"El accuracy score: {np.round(100 * accuracy,1)} %")

    update_model(modelo)
    save_simple_metrics_report(conf_matrix, accuracy)
    logger.info("Training Finished")
