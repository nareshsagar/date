

 
Python Code Snippet
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')
subjects = ['math score', 'reading score', 'writing score']
dataset = df.groupby('gender')[subjects].mean()

indx = np.arange(len(subjects))
score_label = np.arange(0, 110, 10)
male_means = list(dataset.T['male'])
female_means = list(dataset.T['female'])

bar_width = 0.35

fig, ax = plt.subplots()
barMale = ax.bar(indx - bar_width/2, male_means, bar_width, label='Male means')
barFemale = ax.bar(indx + bar_width/2, female_means, bar_width, label='Female means')

# inserting x axis label
ax.set_xticks(indx)
ax.set_xticklabels(subjects)

# inserting y axis label
ax.set_yticks(score_label)
ax.set_yticklabels(score_label)

# inserting legend
ax.legend()

def insert_data_labels(bars):
	for bar in bars:
		bar_height = bar.get_height()
		ax.annotate('{0:.0f}'.format(bar.get_height()),
			xy=(bar.get_x() + bar.get_width() / 2, bar_height),
			xytext=(0, 3),
			textcoords='offset points',
			ha='center',
			va='bottom'
		)

insert_data_labels(barMale)
insert_data_labels(barFemale)



import smtplib
import openpyxl as xl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = str(input('Your Username:'))
password = str(input('Your Password:'))
From = username
Subject = 'Test'
#
# wb = xl.load_workbook(r'C:\Users\\OneDrive\Desktop\insta-web\emailer.xlsx')
# sheet1 = wb['Sheet1'] #wb.get_sheet_by_name('Sheet1')
#
#
# names = []
# emails = []
#
# for cell in sheet1['A']:
#     emails.append(cell.value)
#
# for cell in sheet1['B']:
#     names.append(cell.value)

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(username, password)

# for i in range(len(emails)):
msg = MIMEMultipart()
msg['From'] = username
send_to_email_var = [',']
msg['To'] = ", ".join(send_to_email_var)
msg['Subject'] = Subject
text = '''
Hello Naresh,
test email with python script
'''
msg.attach(MIMEText(text, 'plain'))
message = msg.as_string()
server.sendmail(username,'testmyemail@gmail.com', message)


server.quit()
print('All emails sent successfully!')


