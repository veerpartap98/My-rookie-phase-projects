import json
import os 

class Patientregestration :
    def desgin(slef):
        company_name = 'Veer Hospital'
        print(f'{'='*35}\n{company_name.center(25)}\n{'='*35}')
        print()
    
    def patient_details(self):
        id = 0
        while True:
            name = input('Enter your name : ')
            age,bloodgroup,ward= input("Enter patient 'Age' and 'Bloodgroup' and Ward' : ").split()
            phone_number = int(input('Enter your phone number : ').strip())
            valid_bloodgroups =  ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
            if any([bloodgroup not in valid_bloodgroups,int(age)==0]):
                print('Please check your age or bloodgorup',end='\n')
            elif all([bloodgroup in valid_bloodgroups,int(age)!=0]):
                id += 1
                patient_id = f'Pid- {phone_number}'
                global list_of_patient_details
                list_of_patient_details = {'Patient Id': patient_id,"Name": name,'Age': age,'Bloodgroup': bloodgroup,'Ward':ward}
                print(f'Details added succesfully')
                break
                
    
    def add_dataofpatient(self):
        if os.path.exists('Hospital record.json'):
            with open('Hospital record.json', 'r') as f:
                all_patients = json.load(f)
        else:
            all_patients = []
                    
        all_patients.append(list_of_patient_details)
                
        with open('Hospital record.json','w') as f :
            json.dump(all_patients,f,indent=2)
                    
            
        
class DiagnosisLogger(Patientregestration) : 
    
    def DiagnosisLogger(self):
        syntoms = ['Chest pain','Short of Breath','Nausea','Fever','Headache','Lower Abdominal Pain','Cough']
        i = 0
        for syntom in syntoms:
            i+=1
            print(i,syntom)
        
        ask = input('Enter your syntoms with commas :').lower()
        
        heart_attack = ['chest pain', 'short of breath', 'nausea']
        Pneumonia = ['fever', 'short of breath', 'cough']
        Urinary_Tract_Infection = ['fever', 'lower abdominal pain', 'nausea']

        self.dignose = []
        self.sevirety = []
        ask = [symptom.strip() for symptom in ask.split(',')]

        if set(ask) == set(heart_attack):
            self.dignose.append('Heart Attack')
            self.sevirety.append('High')
            print('You have chance of HEART ATTACK')

        elif set(ask) == set(Pneumonia):
            self.dignose.append('Pneumonia')
            self.sevirety.append('Medium')
            print('You have chance of Pneumonia')

        elif set(ask) == set(Urinary_Tract_Infection):
            self.dignose.append('Urinary Tract Infection')
            self.sevirety.append('High')
            print('You have chance of Urinary Tract Infection')

        else:
            print('No diagnosis found for given symptoms')
            
    def addingdignose(self):
        try:
            ask_for_id = input('Enter id : ')
            
            if os.path.exists('Hospital record.json'):
                with open('Hospital record.json', 'r') as f:
                    alldata = json.load(f)
            else:
                alldata = []
            
            
            for data in alldata:
                if data['Patient Id'] == ask_for_id:
                    self.DiagnosisLogger()
                    data['Dignose'] = self.dignose[0]
                    data['Sevirety'] = self.sevirety[0]
                else:
                    print('Patient not found')
                    
            with open('Hospital record.json','w')as f :
                json.dump(alldata,f,indent=2)
        except Exception as e :
            print(f'Somthing went wrong {e}')      
        

class Findpatient : 
    
    def patientfinder(self):
        with open('Hospital record.json','r') as f :
            patientdetails = json.load(f)
        patient_id = input('Enter id : ')      
        for patient in patientdetails:
            if patient_id == patient["Patient Id"]:
                print(f'Name : {patient['Name']}\nAge : {patient['Age']}\nBlood group : {patient['Bloodgroup']}\nWard : {patient['Ward']}\nDignose : {patient['Dignose']}')
                break
        else :
                print('Patient not found')
                

class Conclusion :
    
    def finalproduct(self):
        try:
            Patientregestration.desgin(self)
            print()
            while True:
                print('HOW WE CAN HELP YOU')
                service = int(input(f'1 Add Patient\n2 Add dignose\n3 Find patient\n4 exit\nEnter service number :'))
                if service == 1:
                    Patientregestration.patient_details(self)
                    Patientregestration.add_dataofpatient(self)
                    print()
                elif service == 2:
                    DiagnosisLogger.DiagnosisLogger(self)
                    DiagnosisLogger.addingdignose(self)
                    print()
                elif service == 3 :
                    Findpatient.patientfinder(self)
                    print()
                elif service == 4:
                    print('Thanks for visting')
                    Patientregestration.desgin(self)
                    break
                else:
                    print('Enter valid service number')
                    
        except Exception as e :
            print(f'Something went wrong : {e}')
            
Hospital = Conclusion()
Hospital.finalproduct()