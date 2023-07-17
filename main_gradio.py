import gradio as gr

from api.app.utils import load_model, transform_output, transform_prediction
from fraudes.python.metadata.categorical_values import CategoricalValues as cv


model = load_model()


def make_prediction(
    monthh: str,
    make: str,
    accidentarea: str,
    monthclaimed: str,
    sex: str,
    fault: str,
    policytype: str,
    vehiclecategory: str,
    vehicleprice: str,
    days_policy_accident: str,
    pastnumberofclaims: str,
    ageofvehicle: str,
    ageofpolicyholder: str,
    agenttype: str,
    numberofsuppliments: str,
    addresschange_claim: str,
    basepolicy: str,
    age: int,
    deductible: int,
    driverrating: int,
    yearr: int,
):
    dict_input = {
        "monthh": [monthh],
        "make": [make],
        "accidentarea": [accidentarea],
        "monthclaimed": [monthclaimed],
        "sex": [sex],
        "fault": [fault],
        "policytype": [policytype],
        "vehiclecategory": [vehiclecategory],
        "vehicleprice": [vehicleprice],
        "days_policy_accident": [days_policy_accident],
        "pastnumberofclaims": [pastnumberofclaims],
        "ageofvehicle": [ageofvehicle],
        "ageofpolicyholder": [ageofpolicyholder],
        "agenttype": [agenttype],
        "numberofsuppliments": [numberofsuppliments],
        "addresschange_claim": [addresschange_claim],
        "basepolicy": [basepolicy],
        "age": [int(age)],
        "deductible": [int(deductible)],
        "driverrating": [int(driverrating)],
        "yearr": [int(yearr)],
    }

    text_out, df_out = transform_output(dict_input)

    prediction = model.predict(text_out)[0]
    prediction = transform_prediction(prediction)

    return [df_out, prediction]


monthh_input = gr.Dropdown(cv.month, label="Month in which the accident occured")
make_input = gr.Dropdown(cv.make, label="Car maker")
accidentarea_input = gr.Radio(
    cv.accident_area, label="Accident occured in rural or urban area"
)
monthclaimed_input = gr.Dropdown(cv.month_claim, label="Month the accident was claimed")
sex_input = gr.Radio(cv.sex, label="Gender of the person involved in the accident")
fault_input = gr.Radio(
    cv.fault, label="If the insurance owner was responsable of the accident"
)
policytype_input = gr.Dropdown(
    cv.policytype, label="Combination between Vehicle Category and Base Policy"
)
vehiclecategory_input = gr.Dropdown(cv.vehiclecategory, label="Vehicle categorization")
vehicleprice_input = gr.Dropdown(cv.vehicleprice, label="Price of the vehicle")
days_policy_accident_input = gr.Dropdown(
    cv.days_policy_accident,
    label="Days between ensurance is acquired and the accident occured",
)
pastnumberofclaims_input = gr.Dropdown(
    cv.pastnumberofclaims, label="Number of past claims of the ensurance owner"
)
ageofvehicle_input = gr.Dropdown(cv.ageofvehicle, label="Age of vehicle")
ageofpolicyholder_input = gr.Dropdown(cv.ageofpolicyholder, label="Age of policy holde")
agenttype_input = gr.Radio(
    cv.agenttype,
    label="Internos son cuando el fraude es realizado por personas trabajando en la empresa de seguros",
)
numberofsuppliments_input = gr.Dropdown(
    cv.numberofsuppliments,
    label="Son daños al vehículo no registrados a la hora de la denuncia, daños extras que no se ven por el exterior",
)
addresschange_claim_input = gr.Dropdown(
    cv.addresschange_claim, label="Address change claim"
)
basepolicy_input = gr.Dropdown(cv.basepolicy, label="Tipe of ensurance")
age_input = gr.Dropdown(cv.age, label="Age")
deductible_input = gr.Dropdown(cv.deductible, label="Deducible")
driverrating_input = gr.Dropdown(cv.driverrating, label="Driverrating")
yearr_input = gr.Dropdown(cv.yearr, label="Year")

inputs = [
    monthh_input,
    make_input,
    accidentarea_input,
    monthclaimed_input,
    sex_input,
    fault_input,
    policytype_input,
    vehiclecategory_input,
    vehicleprice_input,
    days_policy_accident_input,
    pastnumberofclaims_input,
    ageofvehicle_input,
    ageofpolicyholder_input,
    agenttype_input,
    numberofsuppliments_input,
    addresschange_claim_input,
    basepolicy_input,
    age_input,
    deductible_input,
    driverrating_input,
    yearr_input,
]

output1 = gr.Dataframe(label='Datos de entrada')
output2 = gr.Textbox(label="Predición")

app = gr.Interface(
    fn=make_prediction,
    inputs=inputs,
    outputs=[output1, output2],
    title='Fraudes',
    description='App para detectar si un insidente es fraude o no'
)
app.launch()
