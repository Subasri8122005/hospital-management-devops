from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

patients = [
    {
        "id": "PT-1001",
        "name": "Arun Kumar",
        "age": 34,
        "gender": "Male",
        "department": "Cardiology",
        "status": "Active"
    },
    {
        "id": "PT-1002",
        "name": "Priya Sharma",
        "age": 28,
        "gender": "Female",
        "department": "Neurology",
        "status": "Active"
    },
    {
        "id": "PT-1003",
        "name": "Rahul Raj",
        "age": 45,
        "gender": "Male",
        "department": "Orthopedics",
        "status": "Discharged"
    }
]

doctors = [
    {
        "id": "DR-101",
        "name": "Dr. Anitha Kumar",
        "specialization": "Cardiologist",
        "department": "Cardiology",
        "status": "Available"
    },
    {
        "id": "DR-102",
        "name": "Dr. Karthik Raj",
        "specialization": "Neurologist",
        "department": "Neurology",
        "status": "Available"
    },
    {
        "id": "DR-103",
        "name": "Dr. Meena Devi",
        "specialization": "Orthopedic",
        "department": "Orthopedics",
        "status": "On Duty"
    }
]

appointments = [
    {
        "id": "AP-501",
        "patient": "Arun Kumar",
        "doctor": "Dr. Anitha Kumar",
        "department": "Cardiology",
        "date": "2026-09-04",
        "time": "10:30 AM",
        "status": "Confirmed"
    },
    {
        "id": "AP-502",
        "patient": "Priya Sharma",
        "doctor": "Dr. Karthik Raj",
        "department": "Neurology",
        "date": "2026-09-04",
        "time": "11:30 AM",
        "status": "Pending"
    },
    {
        "id": "AP-503",
        "patient": "Rahul Raj",
        "doctor": "Dr. Meena Devi",
        "department": "Orthopedics",
        "date": "2026-09-05",
        "time": "02:00 PM",
        "status": "Confirmed"
    }
]


@app.route("/")
def dashboard():
    return render_template(
        "index.html",
        patients=patients,
        doctors=doctors,
        appointments=appointments
    )


@app.route("/patients")
def patient_list():
    return render_template(
        "patients.html",
        patients=patients
    )


@app.route("/doctors")
def doctor_list():
    return render_template(
        "doctors.html",
        doctors=doctors
    )


@app.route("/appointments")
def appointment_list():
    return render_template(
        "appointments.html",
        appointments=appointments
    )


@app.route("/add_patient", methods=["POST"])
def add_patient():

    patient = {
        "id": f"PT-{1000 + len(patients) + 1}",
        "name": request.form["name"],
        "age": request.form["age"],
        "gender": request.form["gender"],
        "department": request.form["department"],
        "status": "Active"
    }

    patients.append(patient)

    return redirect(url_for("patient_list"))


@app.route("/add_doctor", methods=["POST"])
def add_doctor():

    doctor = {
        "id": f"DR-{100 + len(doctors) + 1}",
        "name": request.form["name"],
        "specialization": request.form["specialization"],
        "department": request.form["department"],
        "status": "Available"
    }

    doctors.append(doctor)

    return redirect(url_for("doctor_list"))


@app.route("/add_appointment", methods=["POST"])
def add_appointment():

    appointment = {
        "id": f"AP-{500 + len(appointments) + 1}",
        "patient": request.form["patient"],
        "doctor": request.form["doctor"],
        "department": request.form["department"],
        "date": request.form["date"],
        "time": request.form["time"],
        "status": "Pending"
    }

    appointments.append(appointment)

    return redirect(url_for("appointment_list"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
