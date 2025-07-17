from flask import Flask, request
import pickle
import sklearn

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Human!"

model_pickle = open("classifier.pkl", "rb")
clf = pickle.load(model_pickle)

@app.route("/prediction", methods=['POST'])
def prediction():
    '''Returns loan application status using ML model
    '''
    loan_req = request.get_json()
    if loan_req['Gender'] == 'Male':
        gender = 0
    else:
        gender = 1
    
    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']

    result = clf.predict([[gender,Married,Credit_History,ApplicantIncome,LoanAmount]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"loan_approval_status": pred} 

if __name__ == "__main__":
    app.run(debug=True)


#input
#  {
#     'Gender': "Male",
#     'Married': "Unmarried",
#     'ApplicantIncome': 50000,
#     'Credit_History': "Cleared Debts",
#     'LoanAmount': 500000
# }

