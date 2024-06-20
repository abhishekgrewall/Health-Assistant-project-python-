class HealthAssistant:
    def __init__(self):
        self.user_data = {'name': '', 'age': 0, 'weight': 0, 'height': 0, 'symptoms': []}
        self.medicine_recommendations = {
            'fever': ['Tylenol', 'Advil'],
            'cough': ['Robitussin', 'Delsym'],
            'headache': ['Aspirin', 'Ibuprofen'],
            'cold': ['DayQuil', 'NyQuil'],
            'allergy': ['Zyrtec', 'Claritin']
        }
    
    def collect_user_data(self):
        self.user_data.update({
            'name': input("Name: "),
            'age': int(input("Age: ")),
            'weight': float(input("Weight (kg): ")),
            'height': float(input("Height (cm): ")),
            'symptoms': input("Symptoms (comma-separated): ").lower().split(',')
        })
    
    def bmi_status(self):
        bmi = self.user_data['weight'] / (self.user_data['height'] / 100) ** 2
        return "Underweight" if bmi < 18.5 else "Normal weight" if 18.5 <= bmi < 25 else "Overweight"
    
    def check_symptoms(self, cough, fever):
        if cough and fever:
            return "You may have a cold or flu. It's recommended to see a doctor and take some over-the-counter medications like ibuprofen or paracetamol."
        elif cough:
            return "You may have a cough. Get some rest and stay hydrated. You can also take cough syrup or lozenges to soothe your throat."
        elif fever:
            return "You may have a fever. Take some paracetamol and get rest. Drink plenty of fluids and consider seeing a doctor if your fever persists."
        else:
            return "You seem to be fine. Take care of yourself and stay healthy!"
    
    def provide_feedback(self):
        print(f"\nHello {self.user_data['name']}!\nYour BMI is: {self.user_data['weight'] / (self.user_data['height'] / 100) ** 2:.2f}\nYou are {self.bmi_status()}.")
        print("\nMedication recommendations:")
        for symptom in self.user_data['symptoms']:
            meds = ', '.join(self.medicine_recommendations.get(symptom.strip(), ["No specific recommendation"]))
            print(f"For {symptom.strip()}, consider: {meds}.")
        print("\nSymptoms check result:")
        result = self.check_symptoms('cough' in self.user_data['symptoms'], 'fever' in self.user_data['symptoms'])
        print(result)
    
    def run(self):
        self.collect_user_data()
        self.provide_feedback()

if __name__ == "__main__":
    HealthAssistant().run()
