import pandas as pd
import numpy as np
from django.shortcuts import render,redirect
import pickle
from sklearn.preprocessing import MinMaxScaler
from django.contrib import messages
from SmartApp.models import Registration


def gas_forecasting(request):
    if request.method=="POST":
        uploaded_file = request.FILES['file']
        Gas = pd.read_csv(uploaded_file)
        new_df = Gas.filter(['Gas'])

        # Preprocessing steps (similar to the code you provided)
        scaler = MinMaxScaler()
        last_60_days = new_df[-60:].values
        last_60_days_scaled = scaler.fit_transform(last_60_days)

        X_test = []
        X_test.append(last_60_days_scaled)
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

        # Load the trained model
        model = pickle.load(open("Gas_forecasting.h5", "rb"))

        # Make predictions
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        # Extract numerical value from the list
        predicted_price_value = pred_price[0][0]

        x=round(predicted_price_value,2)

        context = {'x': x}
    return render(request,'Home.html', context)

def Electricity_forecasting(request):
    if request.method=="POST":
        uploaded_file = request.FILES['file']
        Electricity = pd.read_csv(uploaded_file)
        new_df = Electricity.filter(['Electricity'])

        # Preprocessing steps (similar to the code you provided)
        scaler = MinMaxScaler()
        last_60_days = new_df[-60:].values
        last_60_days_scaled = scaler.fit_transform(last_60_days)

        X_test = []
        X_test.append(last_60_days_scaled)
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

        # Load the trained model
        model = pickle.load(open("Electricity_forecasing.h5", "rb"))

        # Make predictions
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        # Extract numerical value from the list
        predicted_price_value = pred_price[0][0]  # Assuming it's a single prediction
        x = round(predicted_price_value, 2)
        # Pass the prediction value to the template
        context = {'x': x}
        print(predicted_price_value)
    return render(request,'Home.html', context)

def Water_forecasting(request):
    if request.method=="POST":
        uploaded_file = request.FILES['file']
        Water = pd.read_csv(uploaded_file)
        new_df = Water.filter(['Water '])

        scaler = MinMaxScaler()
        last_60_days = new_df[-60:].values
        last_60_days_scaled = scaler.fit_transform(last_60_days)

        X_test = []
        X_test.append(last_60_days_scaled)
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

        # Load the trained model
        model = pickle.load(open("Water_Price_forecasting.h5", "rb"))

        # Make predictions
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        # Extract numerical value from the list
        predicted_price_value = pred_price[0][0]  # Assuming it's a single prediction
        x = round(predicted_price_value, 2)
        # Pass the prediction value to the template
        context = {'x': x}
    return render(request,"Home.html", context)

def Login_pg(request):
    return render(request,"Login Page.html")

def Register_Page(request):
    return render(request,"Register Page.html")

def Registration_save(request):
    if request.method == "POST":
        nm = request.POST.get('name')
        em = request.POST.get('email')
        passw = request.POST.get('password')
        registration = Registration(username=nm, Email=em, Password=passw)
        registration.save()
        messages.success(request,"Registered Successfully.Please Login")
        return redirect(Login_pg)

def Login_fun(request):
    if request.method=="POST":
        nm=request.POST.get('email')
        pwd=request.POST.get('password')
        if Registration.objects.filter(Email=nm,Password=pwd).exists():
            request.session['Email']=nm
            request.session['Password']=pwd
            messages.success(request, "Logged in Successfully")
            return redirect(Home)
        else:
            messages.warning(request, "Check Your Credentials")
            return redirect(Login_pg)
    else:
        messages.warning(request, "Check Your Credentials Or Sign Up ")
        return redirect(Login_pg)

def Logout_fn(request):
    del request.session['Email']
    del request.session['Password']
    messages.success(request, "Logged Out Successfully")
    return redirect(Login_pg)

def Home(req):
    return render(req,"Home.html") 