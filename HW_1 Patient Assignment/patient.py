import csv # allows python to open and read pateint metadata file


class Patient: #defines patient object

    all_patients = [] # every pateitn from csv list will be stored here

    def __init__(self, donor_id: str, age_at_death: int, sex: str,
                 apoe_genotype: str, cognitive_status: str,
                 abeta40: float, abeta42: float,
                 ttau: float, ptau: float): # THIS IS THE CONSTRUCTOR, it lists each pateitn attribute and data type

        self.donor_id = donor_id # all these self.(...) save the pateitns specific info inside that patient object
        self.age_at_death = age_at_death
        self.sex = sex
        self.apoe_genotype = apoe_genotype
        self.cognitive_status = cognitive_status
        self.abeta40 = abeta40
        self.abeta42 = abeta42
        self.ttau = ttau
        self.ptau = ptau

        Patient.all_patients.append(self) #for each time the constructor creates a pateint, this adds that pateint object to the all_patients list

    def __repr__(self): #THIS IS THE REPRESENTER, it conotrols how the papteint object will appear when i print it
        return f"{self.donor_id}: ({self.age_at_death} | {self.sex} | {self.apoe_genotype} | {self.cognitive_status} | ABeta42: {self.abeta42})"

    @classmethod # this makes the method belong to the whole Patient Class and not just each individual pateint
    def instantiate_from_csv(cls, filename: str): #instantiate is what they used in the example so ill use it too...?
        # #the code below will open the .csv file and create a list of all the rows in your spreadsheet

        with open(filename, encoding="utf8") as f: #will open the .csv file and create a list of all the rows in  spreadsheet
            reader = csv.DictReader(f)  #reads each row using the column headers, allows me to retrieve data using the headers
            rows_of_patients = list(reader) # turnsall csv rows into a list

            for row in rows_of_patients:
                Patient(
                    donor_id=row["Donor ID"], #using row to retrieve each pateints individual values, it liek temporaily represents each row in the csv file during each loop 
                    age_at_death=int(row["Age at Death"]), #converts age at death to an integer
                    sex=row["Sex"],
                    apoe_genotype=row["APOE Genotype"],
                    cognitive_status=row["Cognitive Status"],
                    abeta40=float(row["ABeta40 pg/ug"]),
                    abeta42=float(row["ABeta42 pg/ug"]),
                    ttau=float(row["tTAU pg/ug"]),
                    ptau=float(row["pTAU pg/ug"])
                )

    def get_abeta42(self): #this is to retrieve each patients ABeta42 value, which is what i want to sort for
        return self.abeta42

    @classmethod #makes filter belong to whole pateitn class
    def filter(cls, list, sex: str = "any", #no attribute restrictions by default but can be specified when calling the method
               apoe_genotype: str = "any",
               cognitive_status: str = "any"):

        all_patients = list #holds list wew want to filter
        remove_list = [] #holds patients that do not meet the filter criteria, will be removed from all_patients list

        attr_list = ( #stores the attributes we want to filter by
            sex,
            apoe_genotype,
            cognitive_status
        )

        attr_name = ( #stores corresponding attribute names used inside each patient object
            "sex",
            "apoe_genotype",
            "cognitive_status"
        )

        for attr in range(len(attr_list)): #checks each filtering attribute to see if it is set to "any" or a specific value, if it is a specific value then it will remove all patients that do not meet that criteria
            if attr_list[attr] != "any":
                for patient in all_patients:
                    if getattr(patient, attr_name[attr]) != attr_list[attr]: #if no relevant attributem, adds patient to remove list
                        remove_list.append(patient)

                all_patients = [ #rebuilds list without patients who failed filter
                    patient for patient in all_patients
                    if patient not in remove_list
                ]

                remove_list.clear() #empties remove list before checking next attribute

        return all_patients