# patient records - data
# name, age, disease
# search by disease

# list of dictionaries
# searching based on disease
# Patient class

class Patient:
    patients = []
    
    def search_by_disease(self, disease):
        search_result = []
        
        for patient in self.patients:
            if patient['Disease'] == disease:
                search_result.append(patient['Name'])
        
        return search_result if len(search_result) > 0 else None
    
    def add_patient(self, name, age, disease):
        patient = {
            'Name': name,
            'Age': age,
            'Disease': disease
        }
        
        self.patients.append(patient)
    

# Testing
patients = Patient()
patients.add_patient('Alice', 30, 'Flu')
patients.add_patient('Bob', 45, 'Diabetes')
patients.add_patient('Charlie', 35, 'Flu')

search_disease = "Flu"
print(f'Patients with {search_disease}: {patients.search_by_disease("Flu")}')