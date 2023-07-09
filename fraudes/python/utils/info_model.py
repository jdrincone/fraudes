
import numpy as np
from sklearn.pipeline import Pipeline
from joblib import dump
from sklearn import metrics
import matplotlib.pyplot as plt

from fraudes.python.metadata.paths import Paths


def update_model(model: Pipeline) -> None:
    dump(model, Paths.model)


def save_simple_metrics_report(
        conf_matrix: np.array, accuracy: float) -> None:
    with open(Paths.report, 'w', encoding='utf-8') as report_file:
        report_file.write('# Métricas del modelo')
        report_file.write(f'### conf_matrix: {conf_matrix}'+'\n')
        report_file.write(f'### accuracy: {accuracy}'+'\n')


def image_confusion_matrix(y_true, y_pred, acuracy):
    fig, ax = plt.subplots()
    fig.set_figheight(8)
    fig.set_figwidth(8)
    confusion_matrix = metrics.confusion_matrix(y_true, y_pred)
    cm_display = metrics.ConfusionMatrixDisplay(
        confusion_matrix=confusion_matrix, display_labels=[False, True])

    cm_display.plot()
    plt.title(f'Acuracy: {acuracy}')
    plt.savefig(Paths.confusion_matrix)
