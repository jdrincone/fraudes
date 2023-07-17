class CategoricalValues:
    """ Valoeres categoricos para el modelo"""
    month = [
        "Dec",
        "Jan",
        "Oct",
        "Jun",
        "Feb",
        "Nov",
        "Apr",
        "Mar",
        "Aug",
        "Jul",
        "May",
        "Sep",
    ]

    make = [
        "Honda",
        "Toyota",
        "Ford",
        "Mazda",
        "Chevrolet",
        "Pontiac",
        "Accura",
        "Dodge",
        "Mercury",
        "Jaguar",
        "Nisson",
        "VW",
        "Saab",
        "Saturn",
        "Porche",
        "BMW",
        "Mecedes",
        "Ferrari",
        "Lexus",
    ]

    accident_area = ["Urban", "Rural"]

    month_claim = [
        "Jan",
        "Nov",
        "Jul",
        "Feb",
        "Mar",
        "Dec",
        "Apr",
        "Aug",
        "May",
        "Jun",
        "Sep",
        "Oct",
    ]

    sex = ["Female", "Male"]

    fault = ["Policy Holder", "Third Party"]

    policytype = [
        "Sport - Liability",
        "Sport - Collision",
        "Sedan - Liability",
        "Utility - All Perils",
        "Sedan - All Perils",
        "Sedan - Collision",
        "Utility - Collision",
        "Utility - Liability",
        "Sport - All Perils",
    ]

    vehiclecategory = ["Sport", "Utility", "Sedan"]

    vehicleprice = [
        "more than 69000",
        "20000 to 29000",
        "30000 to 39000",
        "less than 20000",
        "40000 to 59000",
        "60000 to 69000",
    ]

    days_policy_accident = ["more than 30", "15 to 30", "none", "1 to 7", "8 to 15"]

    pastnumberofclaims = ["more than 30", "15 to 30", "8 to 15", "none"]

    ageofvehicle = [
        "3 years",
        "6 years",
        "7 years",
        "more than 7",
        "5 years",
        "new",
        "4 years",
        "2 years",
    ]

    ageofpolicyholder = [
        "26 to 30",
        "31 to 35",
        "41 to 50",
        "51 to 65",
        "21 to 25",
        "36 to 40",
        "16 to 17",
        "over 65",
        "18 to 20",
    ]

    agenttype = ["External", "Internal"]

    numberofsuppliments = ["none", "more than 5", "3 to 5", "1 to 2"]

    addresschange_claim = [
        "1 year",
        "no change",
        "4 to 8 years",
        "2 to 3 years",
        "under 6 months",
    ]

    basepolicy = ["Liability", "Collision", "All Perils"]

    age = [x for x in range(17, 80)]

    deductible = [300, 400, 500, 700]

    driverrating = [1, 4, 3, 2]

    yearr = [1994, 1995, 1996]
