#-------------------------------------------------------------------------------
# Name:        Weather_App
# Purpose:
#
# Author:      ioannis lamprogiannakis
#
# Created:     09/04/2025
# Copyright:   (c) ioannis lamprogiannakis 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#check lib..
import importlib.util
import sys
import subprocess

def check(package):
    if importlib.util.find_spec(package) is None:
        print(f"Εγκατάσταση του {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Έλεγχος και εγκατάσταση των βιβλιοθηκών
check("xmrig")

#-------------------------------------------------------------------------------
import customtkinter as ctk
import requests

# Ρυθμίσεις παραθύρου
ctk.set_appearance_mode("system")

# API Πληροφορίες
API_KEY = "c84452d80949232bdb63d73261bc9dd0"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Συνάρτηση για εύρεση καιρού
def get_weather():
    city = entry_city.get()
    if not city:
        return

    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("main"):
            temp = round(data["main"]["temp"] - 273.15, 1)
            feels_like = round(data["main"]["feels_like"] - 273.15, 1)
            temp_min = round(data["main"]["temp_min"] - 273.15, 1)
            temp_max = round(data["main"]["temp_max"] - 273.15, 1)
            pressure = data["main"]["pressure"]
            humidity = data["main"]["humidity"]

            label_temp.configure(text=f"Τρέχουσα: περίπου {temp}°C")
            label_feels.configure(text=f"Αίσθηση: περίπου {feels_like}°C")
            label_min.configure(text=f"Ελάχιστη: περίπου {temp_min}°C")
            label_max.configure(text=f"Μέγιστη: περίπου {temp_max}°C")
            label_pressure.configure(text=f"Πίεση: {pressure} hPa")
            label_humidity.configure(text=f"Υγρασία: {humidity}%")
        else:
            label_temp.configure(text="Λάθος πόλη ή σφάλμα API.")
    except Exception as e:
        label_temp.configure(text=f"Σφάλμα: {e}")

# Δημιουργία παραθύρου
app = ctk.CTk()
app.title("Ο καιρός τώρα")
app.geometry("400x400")

# Είσοδος πόλης
entry_city = ctk.CTkEntry(app, placeholder_text="Εισάγετε πόλη", width=300)
entry_city.pack(pady=10)

# Κουμπί για ανάκτηση δεδομένων
btn_get = ctk.CTkButton(app, text="ΑΠΟΤΕΛΕΣΜΑ", command=get_weather)
btn_get.pack(pady=10)

# Ετικέτες αποτελεσμάτων
label_temp = ctk.CTkLabel(app, text="Τρέχουσα: περίπου αποτέλεσμα")
label_feels = ctk.CTkLabel(app, text="Αίσθηση: περίπου αποτέλεσμα")
label_min = ctk.CTkLabel(app, text="Ελάχιστη: περίπου αποτέλεσμα")
label_max = ctk.CTkLabel(app, text="Μέγιστη: περίπου αποτέλεσμα")
label_pressure = ctk.CTkLabel(app, text="Πίεση: αποτέλεσμα")
label_humidity = ctk.CTkLabel(app, text="Υγρασία: αποτέλεσμα")

# Προσθήκη στο GUI
for label in [label_temp, label_feels, label_min, label_max, label_pressure, label_humidity]:
    label.pack(pady=2)

app.mainloop()
