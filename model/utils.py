
import pandas as pd
import numpy as np
import pickle
import json
try:
    import config
except:
    pass


class SupemarketData():
    def __init__(self,Gender, Quantity, Total, cogs, Branch,City,
       Customer_type, Unit_price, Tax_5, gross_income,
        Product_line,Payment ) :

        self.Gender =Gender
        self.Quantity =Quantity
        self.Total =Total
        self.cogs=cogs
        self.Customer_type =Customer_type
        self.Unit_price=Unit_price
        self.Tax_5=Tax_5
        self.gross_income=gross_income
        

        self.Branch = "Branch_" + Branch
        self.City = "City_" + City 
        self.Product_line = "Product_line_" + Product_line
        self.Payment = "Payment_" + Payment

    def load_model(self):
        try:
            with open(config.MODEL_FILE_PATH,"rb") as f:
                self.model = pickle.load(f)
        except:
            with open("svm_normal.pkl","rb") as f:
                self.model = pickle.load(f)

        try:
            with open(config.JSON_FILE_PATH,"r")as f:
                self.json_data = json.load(f)

        except:
            with open("column_dict.json","r")as f:
                self.json_data = json.load(f)

    def Satisfaction_prediction(self):
        self.load_model()

        Product_line_index  = self.json_data["column_name"].index(self.Product_line)
        Payment_index = self.json_data["column_name"].index(self.Payment)
        Branch_index = self.json_data["column_name"].index(self.Branch)
        City_index = self.json_data["column_name"].index(self.City)



        array = np.zeros(len(self.json_data["column_name"]))

        array[10] = self.json_data["values_Customer_type"][self.Customer_type]
        array[0] = self.json_data["values_Gender"][self.Gender]
        array[11] = self.Unit_price
        array[1] = self.Quantity
        array[12] = self.Tax_5
        array[2] = self.Total
        array[3] = self.cogs
        array[13] = self.gross_income



        array[Product_line_index] = 1
        array[Payment_index] = 1
        array[Branch_index] = 1
        array[City_index] = 1

        array
        prediction = self.model.predict([array])[0]
        # print("predicted_price",predicted_price)
        return prediction

if __name__ == "__main__":
    Gender = 'Male'
    Quantity = 7.0000
    Total = 548.9715
    cogs = 522.8300
    Branch = "A"
    City = "Yangon"

    Customer_type = 'Normal'
    Unit_price = 74.6900
    Tax_5 = 26.1415
    gross_income = 26.1415

    # one hot encodded column 
    Product_line = "Health and beauty"
    Payment = "Ewallet"


    obj = SupemarketData(Gender, Quantity, Total, cogs, Branch,City,
            Customer_type, Unit_price, Tax_5, gross_income,
        Product_line,Payment )
    prediction = obj.Satisfaction_prediction()
    if prediction == 1:
        print("Customer is satisfied ")
    else:
        print("Customer is not satisfied")