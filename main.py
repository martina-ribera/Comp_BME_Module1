from patient import *
import matplotlib.pyplot as plt
import numpy as np
import statistics

# ---------------------------------------------------------------------------
# 4) Create patient objects from the .csv file of demographic + Luminex data
# ---------------------------------------------------------------------------
Patient.instantiate_from_csv("/Users/imtiagea./Desktop/BME 2315/Mod 1/Comp_BME_Module1/Metadata and Protein Data for Module 1.csv")

print(f"Total number of patients loaded: {len(Patient.all_patients)}")
print()

# quick example of the getter + repr from steps 2/3
print("Example patient object:")
print(Patient.all_patients[0])
print()

# ---------------------------------------------------------------------------
# 5) Sort and print the patients by a specific attribute
#    Here we sort by Age at Death, youngest to oldest
# ---------------------------------------------------------------------------
Patient.all_patients.sort(key=Patient.get_age_at_death, reverse=False)

print("Patients sorted by Age at Death (youngest to oldest):")
for patient in Patient.all_patients:
    print(patient)
print()

# ---------------------------------------------------------------------------
# 6) Filter and print a sub-set of patients based on at least two attributes
#    Example 1: female patients with dementia
#    Example 2: male patients with APOE 4/4 alleles
# ---------------------------------------------------------------------------
female_dementia_patients = Patient.filter(Patient.all_patients, sex="Female", cognitive_status="Dementia")
print(f"Number of female patients with dementia = {len(female_dementia_patients)}")
for patient in female_dementia_patients:
    print(patient)
print()

male_apoe44_patients = Patient.filter(Patient.all_patients, sex="Male", apoe_genotype="4_4")
print(f"Number of male patients with APOE 4/4 = {len(male_apoe44_patients)}")
for patient in male_apoe44_patients:
    print(patient)
print()

# ---------------------------------------------------------------------------
# 7) Bar graph: mean (+/- standard deviation) of ABeta42 levels in female vs.
#    male patients who have dementia
# ---------------------------------------------------------------------------
female_dementia = Patient.filter(Patient.all_patients, sex="Female", cognitive_status="Dementia")
male_dementia = Patient.filter(Patient.all_patients, sex="Male", cognitive_status="Dementia")

abeta42_female = [p.abeta42 for p in female_dementia if p.abeta42 is not None]
abeta42_male = [p.abeta42 for p in male_dementia if p.abeta42 is not None]

mean_female = statistics.mean(abeta42_female)
mean_male = statistics.mean(abeta42_male)
stdev_female = statistics.stdev(abeta42_female)
stdev_male = statistics.stdev(abeta42_male)

print(f"Female dementia patients: mean ABeta42 = {mean_female:.2f}, stdev = {stdev_female:.2f}, n = {len(abeta42_female)}")
print(f"Male dementia patients: mean ABeta42 = {mean_male:.2f}, stdev = {stdev_male:.2f}, n = {len(abeta42_male)}")
print()

sex_labels = ['Female', 'Male']
mean_abeta42 = [mean_female, mean_male]
stdev_abeta42 = [stdev_female, stdev_male]
yerr = [np.zeros(len(mean_abeta42)), stdev_abeta42]

plt.figure()
plt.bar(sex_labels, mean_abeta42, yerr=yerr, capsize=10, color=["mediumvioletred", "steelblue"])
plt.title("Amyloid-Beta42 Levels in Female vs. Male Patients with Dementia")
plt.xlabel("Sex")
plt.ylabel("Mean ABeta42 (pg/ug)")
plt.savefig("bar_graph_abeta42_by_sex.png", dpi=150, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# 8) Scatter plot: one quantitative, continuous attribute vs. another
#    Here: ABeta42 levels (y-axis) vs. Age at Death (x-axis)
#    NOTE: we do NOT use Thal score here, since it is a Likert-type/ordinal
#    score (0-5), not a continuous measurement.
# ---------------------------------------------------------------------------
age_at_death = []
abeta42_levels = []

for patient in Patient.all_patients:
    if patient.age_at_death is not None and patient.abeta42 is not None:
        age_at_death.append(patient.age_at_death)
        abeta42_levels.append(patient.abeta42)

X = age_at_death        # independent variable
y = abeta42_levels      # dependent variable

plt.figure()
plt.scatter(X, y, color='darkgreen')
plt.xlabel('Age at Death')
plt.ylabel('ABeta42 (pg/ug)')
plt.title('Scatter Plot of Age at Death vs. Amyloid-Beta42 Levels')
plt.savefig("scatter_plot_age_vs_abeta42.png", dpi=150, bbox_inches="tight")
plt.show()
