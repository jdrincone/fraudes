import pandas as pd


from fraudes.python.metadata.paths import Paths
from fraudes.python.utils.correlaciones import correlaciones_chi2


def data_preparada() -> pd.DataFrame:
    fraudes = pd.read_csv(Paths.path_s3)
    cols = [col.lower() for col in fraudes.columns]
    fraudes.columns = cols

    fraudes_str = fraudes.select_dtypes(include=["object"])

    corr_chi2 = correlaciones_chi2(fraudes_str, fraudes)
    cols_str = list(corr_chi2.keys())
    cols_num = ['age', 'fraudfound_p', 'deductible', 'driverrating', 'yearr']
    sel_cols = cols_str + cols_num
    fraudes_model = fraudes.loc[:, sel_cols]

    cond_edad = fraudes_model['age'] >= 17
    fraudes_model = fraudes_model[cond_edad]
    return fraudes_model


def save_data_preparada():
    df = data_preparada()
    df.to_csv(Paths.data_prep, index=False, sep=';')
