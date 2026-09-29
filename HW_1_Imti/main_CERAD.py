from patient_CERAD import * #this imports the patient class from patient.py
import matplotlib.pyplot as plt #creates graph
import numpy as np #creates error bars
from scipy import stats #used to perform t-test
import statistics #calculates mean and sd
import pandas as pd #used to read csv file

Patient.instantiate_from_csv(r"/Users/imtiagea./Desktop/BME 2315/Mod 1/Comp_BME_Module1/HW_1_Imti/Metadata and Protein Data for Module 1.csv")
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

absent_cerad_patients = Patient.filter(
    Patient.all_patients,
    cerad_score="Absent"
)

sparse_cerad_patients = Patient.filter(
    Patient.all_patients,
    cerad_score="Sparse"
)

moderate_cerad_patients = Patient.filter(
    Patient.all_patients,
    cerad_score="Moderate"
)

frequent_cerad_patients = Patient.filter(
    Patient.all_patients,
    cerad_score="Frequent"
)

absent_ptau = []
sparse_ptau = []
moderate_ptau = []
frequent_ptau = []

for patient in absent_cerad_patients:
    absent_ptau.append(patient.ptau)

for patient in sparse_cerad_patients:
    sparse_ptau.append(patient.ptau)

for patient in moderate_cerad_patients:
    moderate_ptau.append(patient.ptau)

for patient in frequent_cerad_patients:
    frequent_ptau.append(patient.ptau)

absent_ptau_mean = statistics.mean(absent_ptau)
sparse_ptau_mean = statistics.mean(sparse_ptau)
moderate_ptau_mean = statistics.mean(moderate_ptau)
frequent_ptau_mean = statistics.mean(frequent_ptau)

absent_ptau_stdev = statistics.stdev(absent_ptau)
sparse_ptau_stdev = statistics.stdev(sparse_ptau)
moderate_ptau_stdev = statistics.stdev(moderate_ptau)
frequent_ptau_stdev = statistics.stdev(frequent_ptau)

print(f"Absent CERAD pTAU mean: {absent_ptau_mean}")
print(f"Sparse CERAD pTAU mean: {sparse_ptau_mean}")
print(f"Moderate CERAD pTAU mean: {moderate_ptau_mean}")
print(f"Frequent CERAD pTAU mean: {frequent_ptau_mean}")

f_stat, p_value = stats.f_oneway(
    absent_ptau,
    sparse_ptau,
    moderate_ptau,
    frequent_ptau
)

print("F-statistic:", f_stat)
print("ANOVA p-value:", p_value)

cerad_groups = [
    "Absent",
    "Sparse",
    "Moderate",
    "Frequent"
]

ptau_means = [
    absent_ptau_mean,
    sparse_ptau_mean,
    moderate_ptau_mean,
    frequent_ptau_mean
]

ptau_stdev = [
    absent_ptau_stdev,
    sparse_ptau_stdev,
    moderate_ptau_stdev,
    frequent_ptau_stdev
]

yerr = [
    np.zeros(len(ptau_means)),
    ptau_stdev
]

plt.bar(
    cerad_groups,
    ptau_means,
    yerr=yerr,
    capsize=10,
    color=["red", "blue", "pink", "skyblue"]
)

plt.title("pTAU Levels by CERAD Score")
plt.xlabel("CERAD Score")
plt.ylabel("Average pTAU Level (pg/ug)")

y_max = max(ptau_means) + max(ptau_stdev) * 1.2

plt.text(
    1.5, y_max,
    f"One-Way ANOVA: p = {p_value:.3f}",
    ha="center",
    va="bottom",
    fontsize=12
)

plt.show()
