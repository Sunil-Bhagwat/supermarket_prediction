from flask import Flask ,jsonify,render_template,request
from model.utils import SupemarketData

import config

app = Flask(__name__)

@app.route("/")
def hello():
    print("hello flask")
    return render_template("index.html")

@app.route("/Customer_Satisfaction",methods = ["POST","GET"])
def get_customer_satisfaction():
    print("===================")

    if request.method == "GET":
        print("we are using gate method ")
    # data = request.form

    # symboling = eval(data["symboling"])
    # normalized_losses =eval(data["normalized_losses"])
    # fuel_type = data["fuel_type"]
    # aspiration= data["aspiration"]
    # num_of_doors= data["num_of_doors"]
    # drive_wheels=data["drive_wheels"]
    # engine_location= data["engine_location"]
    # wheel_base=eval(data["wheel_base"])
    # length=eval(data["length"])
    # width=eval(data["width"])
    # height=eval(data["height"])
    # curb_weight=eval(data["curb_weight"])
    # num_of_cylinders= data["num_of_cylinders"]
    # engine_size=eval(data["engine_size"])
    # bore=eval(data["bore"])
    # stroke=eval(data["stroke"])
    # compression_ratio=eval(data["compression_ratio"])
    # horsepower=eval(data["horsepower"])
    # peak_rpm=eval(data["peak_rpm"])
    # city_mpg=eval(data["city_mpg"])
    # highway_mpg=eval(data["highway_mpg"])

    # # one hot encoded 
    # make = data["make"]
    # body_style =data["body_style"]
    # engine_type = data["engine_type"]
    # fuel_system = data["fuel_system"]

        Customer_type = (request.args.get("Customer_type"))
        Gender =(request.args.get("Gender"))
        Unit_price = eval(request.args.get("Unit_price"))
        Quantity= eval(request.args.get("Quantity"))
        Tax_5= eval(request.args.get("Tax_5"))
        Total= eval( request.args.get("Total"))
        cogs= eval(request.args.get("cogs"))
        gross_income=eval(request.args.get("gross_income"))
       
        

        # one hot encoded 
        Product_line =request.args.get("Product_line")
        Payment =request.args.get("Payment")
        Branch = request.args.get("Branch")
        City = request.args.get("City")

        Supermarket = SupemarketData(Gender, Quantity, Total, cogs, Branch,City,
            Customer_type, Unit_price, Tax_5, gross_income,
        Product_line,Payment)

        prediction = Supermarket.Satisfaction_prediction()
        if prediction == 1:
            return render_template("index.html",prediction="Hey...! , Customer is satisfied ")
        else:
            return render_template("index.html",prediction="Hey...! , Customer is not satisfied")


    

       
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=False)
