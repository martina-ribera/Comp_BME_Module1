import csv


class Patient:

    # class variable (static variable) -- shared list of every Patient object we create
    all_patients = []

    # 2) Constructor: lists the attributes we want every patient object to have
    def __init__(self,
                 donor_id: str,
                 sex: str = "n/a",
                 age_at_death: float = None,
                 education: str = "n/a",
                 years_education: float = None,
                 apoe_genotype: str = "n/a",
                 cognitive_status: str = "n/a",
                 age_of_onset: float = None,
                 age_of_diagnosis: float = None,
                 thal_score: int = None,
                 braak_stage: str = "n/a",
                 abeta40: float = None,
                 abeta42: float = None,
                 ttau: float = None,
                 ptau: float = None):

        self.donor_id = donor_id
        self.sex = sex
        self.age_at_death = age_at_death
        self.education = education
        self.years_education = years_education
        self.apoe_genotype = apoe_genotype
        self.cognitive_status = cognitive_status
        self.age_of_onset = age_of_onset
        self.age_of_diagnosis = age_of_diagnosis
        self.thal_score = thal_score
        self.braak_stage = braak_stage
        self.abeta40 = abeta40
        self.abeta42 = abeta42
        self.ttau = ttau
        self.ptau = ptau

        # every time we make a new patient, add it to the class-wide list
        Patient.all_patients.append(self)

    # 3) Representer: what gets shown when we print a patient object
    def __repr__(self):
        return (f"{self.donor_id}: ({self.sex} | Age at death: {self.age_at_death} | "
                f"{self.cognitive_status} | APOE {self.apoe_genotype} | Thal {self.thal_score} | "
                f"ABeta42: {self.abeta42})")

    # ---- getters (instance methods) ----
    def get_age_at_death(self):
        return self.age_at_death

    def get_thal_score(self):
        return self.thal_score

    def get_abeta42(self):
        return self.abeta42

    # helper to turn blank strings from the .csv into None instead of ""
    @staticmethod
    def _to_float_or_none(value):
        if value is None or value == "":
            return None
        return float(value)

    # helper to pull the number out of strings like "Thal 3" -> 3
    @staticmethod
    def _parse_thal(value):
        if value is None or value == "":
            return None
        return int(value.replace("Thal", "").strip())

    # 4) Class method that reads the .csv file and builds a Patient object for each row
    @classmethod
    def instantiate_from_csv(cls, filename: str):

        # open the .csv file and get a list of all the rows in the spreadsheet
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)

        # create a patient object for each row, based on the data
        for row in rows_of_patients:
            Patient(
                donor_id=row['Donor ID'],
                sex=row['Sex'],
                age_at_death=cls._to_float_or_none(row['Age at Death']),
                education=row['Highest level of education'],
                years_education=cls._to_float_or_none(row['Years of education']),
                apoe_genotype=row['APOE Genotype'],
                cognitive_status=row['Cognitive Status'],
                age_of_onset=cls._to_float_or_none(row['Age of onset cognitive symptoms']),
                age_of_diagnosis=cls._to_float_or_none(row['Age of Dementia diagnosis']),
                thal_score=cls._parse_thal(row['Thal']),
                braak_stage=row['Braak'],
                abeta40=cls._to_float_or_none(row['ABeta40 pg/ug']),
                abeta42=cls._to_float_or_none(row['ABeta42 pg/ug']),
                ttau=cls._to_float_or_none(row['tTAU pg/ug']),
                ptau=cls._to_float_or_none(row['pTAU pg/ug']),
            )

    # 5) Getter to find one specific patient by donor ID
    @classmethod
    def get_patient(cls, donor_id):
        for patient in Patient.all_patients:
            if donor_id == patient.donor_id:
                return patient

    # 6) Class method to filter a list of patients by at least two attributes at once
    @classmethod
    def filter(cls, patient_list, sex: str = "any", cognitive_status: str = "any",
               apoe_genotype: str = "any", education: str = "any",
               thal_score="any", braak_stage: str = "any"):

        remaining_patients = patient_list
        remove_list = []

        attr_list = (sex, cognitive_status, apoe_genotype, education, thal_score, braak_stage)
        attr_name = ("sex", "cognitive_status", "apoe_genotype", "education", "thal_score", "braak_stage")

        for attr in range(len(attr_list)):
            if attr_list[attr] != "any":
                for patient in remaining_patients:
                    if getattr(patient, attr_name[attr]) != attr_list[attr]:
                        remove_list.append(patient)
                remaining_patients = [p for p in remaining_patients if p not in remove_list]
                remove_list.clear()

        return remaining_patients
