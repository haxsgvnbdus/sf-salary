import pandas as pd

sal = pd.read_csv('Salaries.csv')
# num_entries = sal.info()

avgPay = sal['BasePay'].mean()
print("Average Payment: {}".format(avgPay))						#64k/year 

maxOTPay = sal.OvertimePay.max()
print("Maximum Overtime Compensation: {}".format(maxOTPay))

info = sal[sal.EmployeeName == 'JOSEPH DRISCOLL'].JobTitle
benefit = sal[sal.EmployeeName == 'JOSEPH DRISCOLL'].TotalPayBenefits	
#incidentally make sure there is one person named Joseph Driscoll as there is only one returned value as True

print("Josheph Driscoll \nJob title: {}\nBenefits: {}".format(info, benefit))


#Name of highest paid person?
p = sal[sal.TotalPayBenefits == sal.TotalPayBenefits.max()]

#Name of lowest paid person? 
#Strange point: negative data

p = sal[sal.TotalPayBenefits == sal.TotalPayBenefits.min()]

#Average mean BasePay per year 
report = sal.groupby('Year').mean().BasePay
 
#Unique jobs 
num_jobs = sal.JobTitle.nunique()
print("Number of unique jobs: {}".format(num_jobs))

#Top 5 most common jobs 
common_jobs = sal.JobTitle.value_counts().head(5)
print("Most common job titles: {}".format(common_jobs))

#Job titles with only one occurence in 2013 
num_uniques = sum(sal[sal.Year == 2013].JobTitle.value_counts() == 1)	
print("Number of unique jobs: {}".format(num_uniques))

#How many people have the word Chief in their titles?
def isChief(title):
	return True if 'chief' in title.lower() else False

total = sum(sal.JobTitle.apply(lambda x: isChief(x))) 
print("Number of Chief: {}".format(total))

#Is there a correlation between length of the job title string and salary?

