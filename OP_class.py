import tkinter


class Patient:
    def __init__(self):
        self.__name = ""
        self.__address = ""
        self.__phone_no = ""
        self.__insurance = False
        self.__prescription = ""

    def set_personal_info(self):
        self.__name = input("Enter Name: ")
        self.__address = input("Enter Address: ")
        self.__phone_no = input("Enter Phone Number: ")
        x = input("Patient has insurance (y/n): ")
        if x == "Y" or x == "y":
            self.__insurance = True
        prescription = int(input("Enter 1 if patient has a prescription and 0 if they do not: "))
        if prescription == 1:
            left = input("Enter left eye prescription: ")
            right = input("Enter right eye prescription: ")
            self.__prescription = {"left": left, "right": right}
        else:
            self.__prescription = "N/A"

    def show_personal_info(self):
        print("Name:", self.__name)
        print("Address:", self.__address)
        print("Phone Number:", self.__phone_no)
        print("Insurance:", self.__insurance)
        print("Prescription:", self.__prescription)

    def get_patient_name(self):
        return self.__name

    def update_prescription(self):
        left = input("Enter left eye prescription: ")
        right = input("Enter right eye prescription")
        self.__prescription = {"left": left, "right": right}


class Appointments:
    def __init__(self):
        self.__appointment_date = {}
        self.__appointment_time = ""
        self.__dr_name = ""
        self.__patient_name = ""
        self.__cost = ""

    def set_appointment(self):
        self.__patient_name = input("Enter Patient's Name: ")
        year = input("Enter Year of Appointment: ")
        month = input("Enter Month of Appointment: ")
        day = input("Enter Day of Appointment: ")
        self.__appointment_time = input("Enter Time of Day: ")
        self.__appointment_date = {"year": year, "month": month, "day": day}
        self.__dr_name = input("Enter Doctor's Name: ")

    def show_appointment(self):
        print("Patient Name:", self.__patient_name)
        print("Doctor Name:", self.__dr_name)
        print("Appointment Scheduled for", self.__appointment_time, "on", self.__appointment_date["month"], "/",
              self.__appointment_date["day"], "/", self.__appointment_date["year"])

    def get_patient_name(self):
        return self.__patient_name

    def get_dr_name(self):
        return self.__dr_name

    def get_appointment_date(self):
        return self.__appointment_date


class Doctor:
    def __init__(self):
        self.__dr_name = ""
        self.__specialty = ""

    def add_new_dr(self):
        self.__dr_name = input("Enter doctor's name: ")
        self.__specialty = input("Enter doctor's specialty: ")

    def show_dr_info(self):
        print("Name:", self.__dr_name)
        print("Specialty:", self.__specialty)

    def get_dr_name(self):
        return self.__dr_name


class Billing:
    def __init__(self, name, payment, glasses, insurance, date):
        self.__payment_type = payment
        self.__cost = 100+glasses
        self.__insurance = insurance
        self.__patient_name = name
        if insurance == 1:
            self.__insurance = True
        if self.__insurance:
            self.__cost = self.__cost - 40
        self.__date = date

    def display_billing_info(self):
        print("Name: ", self.__patient_name)
        print("Payment Type: ", self.__payment_type)
        print("Total Price: $", self.__cost)
        print("Appointment Date: ", self.__date)

    def get_patient_name(self):
        return self.__patient_name

    def get_date(self):
        return self.__date

    def get_glasses_price(self):
        return self.__glasses_price

    def get_total_cost(self):
        return self.__cost

    def print_total_cost(self):
        import tkinter
        window = tkinter.Tk()
        window.resizable(False, False)
        myCanvas = tkinter.Canvas(window, bg="white", height=300, width=500)
        total = "Total: $" + str(self.__cost)
        myCanvas.create_text(100, 100, text=total)
        myCanvas.pack()
        window.mainloop()


class Glasses:
    def __init__(self):
        self.__patient_name = ""
        self.__lenses_price = ""
        self.__prescription = ""
        self.__date = ""
        self.__framecost=""
        self.__totalcost=""

    def get_glasses_info(self,frame):
        self.__patient_name = input("Enter Patient Name: ")
        left = input("Enter Left Eye Prescription: ")
        right = input("Enter Right Eye Prescription: ")
        self.__prescription = {"left": left, "right": right}
        self.__date = input("Enter Date in dd/mm/yyyy: ")
        self.__lenses_price = self.calculate_lenses(left, right)
        self.__framecost=frame
        self.__totalcost=self.__framecost+self.__lenses_price

    def calculate_lenses(self, left, right):
        Mild = False
        High = False
        Moderate = False
        Extreme = False
        lens_price = 0

        lens_avg = (abs(float(left)) + abs(float(right))) / 2

        if lens_avg < 0.5:
            print("No prescription needed")
        elif 0.5 <= lens_avg < 3:
            Mild = True
        elif 3 <= lens_avg < 5:
            Moderate = True
        elif 5 <= lens_avg < 10:
            High = True
        elif lens_avg >= 10:
            Extreme = True
        else:
            print("No criteria for:", lens_avg)

        if Mild:
            lens_price = 50.00
        elif Moderate:
            lens_price = 75.00
        elif High:
            lens_price = 100.00
        elif Extreme:
            lens_price = 125.00

        return lens_price

    def display_glasses_info(self):
        print("Name: ", self.__patient_name)
        print("Lens Price: $", self.__lenses_price)
        print("Total Cost: $",self.__totalcost)
        print("Prescription: ", self.__prescription)
        print("Date of Order: ", self.__date)


    def get_patient_name(self):
        return self.__patient_name

    def get_date(self):
        return self.__date

    def get_cost(self):
        return self.__totalcost


class Frames:
    def __init__(self, color, shape, price):
        self.__frame_color = color
        self.__frame_shape = shape
        self.__frame_price = price

    def display_frame_info(self):
        print("Frame Color:", self.__frame_color)
        print("Frame Shape:", self.__frame_shape)
        print("Frame Price:", self.__frame_price)

    def get_price(self):
        return self.__frame_price


def show_frames():
    root = tkinter.Tk()
    root.resizable(False, False)

    myDisplay = tkinter.Canvas(root, bg="white", height=500, width=1200)

    # first row
    fr1 = tkinter.PhotoImage(file="images/blue_oval.png")
    fr1 = fr1.subsample(1, 1)
    fr2 = tkinter.PhotoImage(file="images/pink_circle.png")
    fr2 = fr2.subsample(1, 1)
    fr3 = tkinter.PhotoImage(file="images/cat_eye.png")
    fr3 = fr3.subsample(1, 1)

    # second row
    fr4 = tkinter.PhotoImage(file="images/clear_oval.png")
    fr4 = fr4.subsample(1, 1)
    fr5 = tkinter.PhotoImage(file="images/rectangle_frame.png")
    fr5 = fr5.subsample(1, 1)
    fr6 = tkinter.PhotoImage(file="images/square_frame.png")
    fr6 = fr6.subsample(1, 1)

    # images
    blue_oval = myDisplay.create_image(200, 125, image=fr1)
    pink_circle = myDisplay.create_image(600, 125, image=fr2)
    cat_eye = myDisplay.create_image(1000, 125, image=fr3)
    clear_oval = myDisplay.create_image(200, 350, image=fr4)
    rectangle_frame = myDisplay.create_image(600, 350, image=fr5)
    square_frame = myDisplay.create_image(1000, 350, image=fr6)

    # Text boxes
    f1_text = "1) Blue Oval Frame\n      Price: $" + str(OP.f1.get_price())
    f2_text = "2) Pink Circle Frame\n       Price: $" + str(OP.f2.get_price())
    f3_text = "3) Multi-Color Cat Eye Frame\n            Price: $" + str(OP.f3.get_price())
    f4_text = "4) Transparent Oval Frame\n           Price: $" + str(OP.f4.get_price())
    f5_text = "5) Black Rectangle Frame\n          Price: $" + str(OP.f5.get_price())
    f6_text = "6) Brown Square Frame\n         Price: $" + str(OP.f6.get_price())

    # first row
    blue_oval_text = myDisplay.create_text(200, 215, text=f1_text, fill="black", font=('Helvetica 15'))
    pink_circle_text = myDisplay.create_text(600, 215, text=f2_text, fill="black", font=('Helvetica 15'))
    cat_eye_text = myDisplay.create_text(1000, 215, text=f3_text, fill="black", font=('Helvetica 15'))
    # second row
    clear_oval_text = myDisplay.create_text(200, 440, text=f4_text, fill="black", font=('Helvetica 15'))
    rectangle_frame_text = myDisplay.create_text(600, 440, text=f5_text, fill="black", font=('Helvetica 15'))
    square_text = myDisplay.create_text(1000, 440, text=f6_text, fill="black", font=('Helvetica 15'))

    myDisplay.pack()
    root.mainloop()


# Frame Objects
f1 = Frames("Oval", "Blue", 50.99)
f2 = Frames("Circle", "Pink", 49.99)
f3 = Frames("Cat Eye", "Multi-Color", 64.99)
f4 = Frames("Oval", "Transparent", 50.99)
f5 = Frames("Rectangle", "Black", 54.99)
f6 = Frames("Square", "Brown", 34.99)
