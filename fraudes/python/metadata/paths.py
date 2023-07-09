import os


class Paths:
    path_file = os.path.dirname(os.path.abspath(__file__))
    path_input = os.path.join(path_file, "..", "..", "..", "input")
    cred_posgres = os.path.join(path_input, "cred_bd_posgres.yaml")
    path_s3 = os.path.join("https://jdrincone.s3.us-east-2.amazonaws.com/fraud.csv")
    query = os.path.join(path_input, "querys.yaml")

    model = os.path.join(path_file, "..", "..", "model", 'model.pkl')
    report = os.path.join(path_file, "..", "..", "..", 'report.txt')
    data_prep = os.path.join(path_file, "..", "..",  "..", "data", 'data_preparada.csv')
    confusion_matrix = os.path.join(path_file, "..", "..",  "..", "images", 'confusion_matrix.png')
