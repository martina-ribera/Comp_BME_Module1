from patient import * #this imports the patient class from patient.py
import matplotlib.pyplot as plt #creates graph
import numpy as np #creates error bars
from scipy import stats #used to perform t-test
import statistics #calculates mean and sd
import pandas as pd #used to read csv file
from sklearn.linear_model import LinearRegression #used to make regression line

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

#the two no dementia groups are for the ANOVA test, where im testing whether avg ab42 level difers among sex and dementia groups
female_no_dementia_patients = Patient.filter(
    Patient.all_patients,
    sex="Female",
    cognitive_status="No dementia"
)

male_no_dementia_patients = Patient.filter(
    Patient.all_patients,
    sex="Male",
    cognitive_status="No dementia"
)
male_dementia_patients = Patient.filter(
    Patient.all_patients,
    sex="Male",
    cognitive_status="Dementia"
)

female_abeta42 = [] #both are empty lists to hold the AB42 measumrents
male_abeta42 = []
#this is the new stuff for ANOVA test
female_no_dementia_abeta42 = []
male_no_dementia_abeta42 = []

for patient in female_no_dementia_patients:
    female_no_dementia_abeta42.append(patient.abeta42)

for patient in male_no_dementia_patients:
    male_no_dementia_abeta42.append(patient.abeta42)
#up to here for anova

#both of the for loops below retriebe the AB42 values for each patient in the filtered groups and add them to the empty lists above
for patient in female_dementia_patients:
    female_abeta42.append(patient.abeta42)

for patient in male_dementia_patients:
    male_abeta42.append(patient.abeta42)

#EVERYTHING BELOW THIS IS FOR THE GRAPHS AND STATS
female_abeta42_mean = statistics.mean(female_abeta42) #finds female mean
male_abeta42_mean = statistics.mean(male_abeta42)

#these next 4 lines are for ANOVA test
female_no_dementia_abeta42_mean = statistics.mean(female_no_dementia_abeta42)
male_no_dementia_abeta42_mean = statistics.mean(male_no_dementia_abeta42)

female_no_dementia_abeta42_stdev = statistics.stdev(female_no_dementia_abeta42)
male_no_dementia_abeta42_stdev = statistics.stdev(male_no_dementia_abeta42)
#up to here


female_abeta42_stdev = statistics.stdev(female_abeta42)#finds female sd across all patients
male_abeta42_stdev = statistics.stdev(male_abeta42)

print(f"Female dementia ABeta42 mean: {female_abeta42_mean}")
print(f"Female dementia ABeta42 standard deviation: {female_abeta42_stdev}")

print(f"Male dementia ABeta42 mean: {male_abeta42_mean}")
print(f"Male dementia ABeta42 standard deviation: {male_abeta42_stdev}")

#STATS TEST 
t_stat, p_val = stats.ttest_ind(female_abeta42, male_abeta42) #performs t-test to see if the two groups are significantly different 
print(f"t_stat={t_stat}, p_ val={p_val}") #prints the t-test results and p value

# Runs one-way ANOVA across the four groups
f_stat, p_value = stats.f_oneway( 
    female_no_dementia_abeta42,
    male_no_dementia_abeta42,
    female_abeta42,
    male_abeta42
) #this compares the 4 mean groups to see if they are significantly different from each other, the null hypothesis is that all 4 means are equal, the alternative is that at least one mean is different

#these two lines display the results of the ANOVA test, the f-statistic and the p-value
print("F-statistic:", f_stat)
print("ANOVA p-value:", p_value)

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

y_max = max(mean_abeta42) + max(stdev_abeta42) * 0.4

plt.text(
    0.5, y_max,
    f"t = {t_stat:.2f}\np = {p_val:.3e}",
    ha="center",
    va="bottom"
)
plt.show() 

# ANOVA BAR GRAPH
anova_groups = [
    "Healthy Female",
    "Healthy Male",
    "Dementia Female",
    "Dementia Male"
]

anova_means = [
    female_no_dementia_abeta42_mean,
    male_no_dementia_abeta42_mean,
    female_abeta42_mean,
    male_abeta42_mean
]

anova_stdev = [
    female_no_dementia_abeta42_stdev,
    male_no_dementia_abeta42_stdev,
    female_abeta42_stdev,
    male_abeta42_stdev
]

anova_yerr = [
    np.zeros(len(anova_means)),
    anova_stdev
]

plt.bar(
    anova_groups,
    anova_means,
    yerr=anova_yerr,
    capsize=10,
    color=["red", "blue", "pink", "skyblue"]
)

plt.title("ABeta42 Levels")
plt.xlabel("Sex and Dementia Status")
plt.ylabel("Average ABeta42 Level (pg/ug)")

plt.text(
    1.5, 380,
    f"One-Way ANOVA: p = {p_value:.3f}",
    ha="right",
    va="top",
    fontsize=12
)

plt.show()

#everything below this is for the scatter plot of ABeta42 vs age at death
patient_ages = [] 
patient_abeta42 = []

for patient in Patient.all_patients: #these two for loops retrieve each patients age and ab42 values
    patient_ages.append(patient.age_at_death) 

for patient in Patient.all_patients:
    patient_abeta42.append(patient.abeta42)

#adding the regression line to the scatter plot
X = np.array(patient_ages).reshape(-1, 1) #independent variable
y = np.array(patient_abeta42) #dependent variable

model = LinearRegression() #creates the regression model
model.fit(X, y) #fits the regression line to age and ABeta42 data

slope = model.coef_[0] #slope of regression line
intercept = model.intercept_ #point where line crosses y-axis
r2 = model.score(X, y) #measures how well the line fits the data
equation = f"y = {slope:.2f}x + {intercept:.2f}\nR² = {r2:.2f}"

plt.text(
    X.min(),
    y.max(),
    equation,
    color="red",
    fontsize=12,
    verticalalignment="top"
)
    #makes scatter plot
plt.scatter(X, y, color="green")
plt.plot(X, model.predict(X), color="red") #plots the regression line
plt.xlabel("Age at Death (years)")
plt.ylabel("ABeta42 Level (pg/ug)")
plt.title("ABeta42 Level vs. Age at Death")
plt.show()