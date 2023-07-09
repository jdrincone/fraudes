from pydantic import BaseModel


class PredictionRequest(BaseModel):
    monthh: str
    make: str
    accidentarea: str
    monthclaimed: str
    sex: str
    fault: str
    policytype: str
    vehiclecategory: str
    vehicleprice: str
    days_policy_accident: str
    pastnumberofclaims: str
    ageofvehicle: str
    ageofpolicyholder: str
    agenttype: str
    numberofsuppliments: str
    addresschange_claim: str
    basepolicy: str
    age: int
    deductible: int
    driverrating: int
    yearr: int


class PredictionResponse(BaseModel):
    fraudfound_p: str
