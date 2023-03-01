from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("c2_flight_rf.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("main.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        Duration_hours = abs(arrival_hour - dep_hour)
        Duration_mins = abs(arrival_min - dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Stop = int(request.form["stops"])
        # print(Total_stops)





        Source = request.form["Source"]
        if (Source == 'Delhi'):
            from_Delhi = 1
            from_Kolkata = 0
            from_Mumbai = 0
            from_Chennai = 0
            from_Hyderabad = 0

        elif (Source == 'Kolkata'):
            from_Delhi = 0
            from_Kolkata = 1
            from_Mumbai = 0
            from_Chennai = 0
            from_Hyderabad = 0

        elif (Source == 'Mumbai'):
            from_Delhi = 0
            from_Kolkata = 0
            from_Mumbai = 1
            from_Chennai = 0
            from_Hyderabad = 0

        elif (Source == 'Chennai'):
            from_Delhi = 0
            from_Kolkata = 0
            from_Mumbai = 0
            from_Chennai = 1
            from_Hyderabad = 0

        elif (Source == 'Hyderabad'):
            from_Delhi = 0
            from_Kolkata = 0
            from_Mumbai = 0
            from_Hyderabad = 1
            from_Chennai = 0

        else:
            from_Delhi = 0
            from_Kolkata = 0
            from_Mumbai = 0
            from_Chennai = 0
            from_Hyderabad = 0



        Source = request.form["Destination"]
        if (Source == 'Chennai'):
            to_Chennai = 1
            to_Delhi = 0
            to_Hyderabad = 0
            to_Kolkata = 0
            to_Mumbai = 0
        
        elif (Source == 'Delhi'):
            to_Chennai = 0
            to_Delhi = 1
            to_Hyderabad = 0
            to_Kolkata = 0
            to_Mumbai = 0


        elif (Source == 'Hyderabad'):
            to_Chennai = 0
            to_Delhi = 0
            to_Hyderabad = 1
            to_Kolkata = 0
            to_Mumbai = 0

        elif (Source == 'Kolkata'):
            to_Chennai = 0
            to_Delhi = 0
            to_Hyderabad = 0
            to_Kolkata = 1
            to_Mumbai = 0

        elif (Source == 'Mumbai'):
            to_Chennai = 0
            to_Delhi = 0
            to_Hyderabad = 0
            to_Mumbai = 1
            to_Kolkata = 0

        else:
            to_Mumbai = 0
            to_Delhi = 0
            to_Hyderabad = 0
            to_Kolkata = 0
            to_Chennai = 0


        prediction=model.predict([[
            Stop,
            journey_day,
            journey_month,
            dep_hour,
            dep_min,
            arrival_hour,
            arrival_min,
            Duration_hours,
            Duration_mins,
            from_Chennai,
            from_Delhi,
            from_Hyderabad,
            from_Kolkata,
            from_Mumbai,
            to_Chennai,
            to_Delhi,
            to_Hyderabad,
            to_Kolkata,
            to_Mumbai
        ]])

        output=round(prediction[0],2)

        return render_template('main.html',prediction_text="Predicted Flight Price: Rs. {}".format(output))


    return render_template("main.html")




if __name__ == "__main__":
    app.run(debug=True)