import pandas as pd
from scipy import stats


def correlaciones_chi2(fraudes_str: pd.DataFrame, fraudes: pd.DataFrame) -> dict:
    """ Otorga las variables que poseen mayor correlación  con la variable objetivo.

    Args:
        fraudes_str: Data de trabajo con solo variables categoricas
        fraudes:  Data original de trabajo.

    Return:
        Variables con mayor correlacción con la variable objetivo.
    """
    corr_chi2 = {}
    for col in fraudes_str.columns:
        if col != "fraudfound_p":
            data_crosstab = pd.crosstab(
                fraudes["fraudfound_p"], fraudes_str[col], margins=False
            )
            pvalue_chi2 = stats.chi2_contingency(data_crosstab).pvalue
            if pvalue_chi2 < 0.05:
                corr_chi2[col] = pvalue_chi2.round(3)

    return corr_chi2
