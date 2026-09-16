from patient import * #this imports the patient class from patient.py
import matplotlib.pyplot as plt #creates graph
import numpy as np #creates error bars
import statistics #calculates mean and sd

Patient.instantiate_from_csv(r"Comp_BME_Module1/HW_1 Patient Assignment/Metadata and Protein Data for Module 1.csv")
#line above creates the patient objects

print(len(Patient.all_patients)) #test to see if all patients loaded, should be 84
print(Patient.all_patients[0]) #testing by hopefully printing first ptient

Patient.all_patients.sort(key=Patient.get_abeta42, reverse=False) # sorts patients by AB42 levels in ascending order
 #the reverse False is meeant to sort in ascending order low to high


for patient in Patient.all_patients: #loop prints all 84 patients in ascneding order
    print(patient)

apoe4_dementia_patients = Patient.filter( #new varialble that holds filtered group, calls Patient class method
    Patient.all_patients, #list of all patients
    apoe_genotype="4_4", #this and line below are the two filtering conditions
    cognitive_status="Dementia" #all other attributes set to "any" by default so they are not filtered
)

print(f"Number of patients with APOE 4_4 and dementia: {len(apoe4_dementia_patients)}") # counts how many patients passed both conditions

for patient in apoe4_dementia_patients: #prints each patient in filterd group
    print(patient)

#these two groups are for the bar graph, comparing AB42 levels between female and male patients w dementia
female_dementia_patients = Patient.filter( 
    Patient.all_patients,
    sex="Female",
    cognitive_status="Dementia"
)

male_dementia_patients = Patient.filter(
    Patient.all_patients,
    sex="Male",
    cognitive_status="Dementia"
)

female_abeta42 = [] #both are empty lists to hold the AB42 measumrents
male_abeta42 = []

#both of the for loops below retriebe the AB42 values for each patient in the filtered groups and add them to the empty lists above
for patient in female_dementia_patients:
    female_abeta42.append(patient.abeta42)

for patient in male_dementia_patients:
    male_abeta42.append(patient.abeta42)

#EVERYTHING BELOW THIS IS FOR THE GRAPHS AND STATS
female_abeta42_mean = statistics.mean(female_abeta42) #finds female mean
male_abeta42_mean = statistics.mean(male_abeta42)

female_abeta42_stdev = statistics.stdev(female_abeta42)#finds female sd across all patients
male_abeta42_stdev = statistics.stdev(male_abeta42)

print(f"Female dementia ABeta42 mean: {female_abeta42_mean}")
print(f"Female dementia ABeta42 standard deviation: {female_abeta42_stdev}")

print(f"Male dementia ABeta42 mean: {male_abeta42_mean}")
print(f"Male dementia ABeta42 standard deviation: {male_abeta42_stdev}")

patient_sex_groups = ["Female Patients", "Male Patients"] #labels for x axis

mean_abeta42 = [ #bar height
    female_abeta42_mean,
    male_abeta42_mean
]

stdev_abeta42 = [ #stores sd for each
    female_abeta42_stdev,
    male_abeta42_stdev
]

yerr = [ #creates error bars like in dog example
    np.zeros(len(mean_abeta42)),
    stdev_abeta42
]

plt.bar( #makes the bar graph, the yerr is the error bars, capsize is the size of the error bar caps, color is the color of the bars
    patient_sex_groups,
    mean_abeta42,
    yerr=yerr,
    capsize=10,
    color=["purple", "blue"]
)

#EVERYTHING W PLT PLOTS THE GRAPH
plt.title("Average ABeta42 Levels in Patients with Dementia")
plt.xlabel("Sex")
plt.ylabel("Average ABeta42 Level (pg/ug)")
plt.show() 

#everything below this is for the scatter plot of ABeta42 vs age at death
patient_ages = [] 
patient_abeta42 = []

for patient in Patient.all_patients: #these two for loops retrieve each patients age and ab42 values
    patient_ages.append(patient.age_at_death) 

for patient in Patient.all_patients:
    patient_abeta42.append(patient.abeta42)

X = [patient_ages] #creates a list of the ages
y = [patient_abeta42] #creates a list of the ABeta42 values

    #makes scatter plot
plt.scatter(X, y, color="green")
plt.xlabel("Age at Death (years)")
plt.ylabel("ABeta42 Level (pg/ug)")
plt.title("ABeta42 Level vs. Age at Death")
plt.show()