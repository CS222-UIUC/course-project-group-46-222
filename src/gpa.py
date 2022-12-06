import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np



def createData(number, name, term):
    df = pd.read_csv('data/uiuc-gpa-dataset.csv')
    df = df.rename(columns={'Course Title': 'Course_Title'})
    df = df.rename(columns={'Primary Instructor': 'Primary_Instructor'})    
    name = name.upper()
    yr = ''
    if (term!='all'):
        yr = term.split(' ')[1]
        term = term.split(' ')[0]
    year = yr + '-' + term.lower()[:2]
    #print(number)
    #print(name)
    new_df = df.loc[(df['Number'] == number)  & (df['Subject'] == name)]
    #print(new_df)
    data = []
    years = new_df.YearTerm.unique()
    if (term != 'all'):
        df_year = new_df.loc[(new_df['YearTerm'] == year)]
    else:
        df_year = new_df
    instructors = df_year.Primary_Instructor.unique()
    #df_year
    for instructor in instructors:
        df_instructor = df_year.loc[(df_year['Primary_Instructor']) == instructor]
        new = (df_instructor.sum(axis = 0, skipna = True))
        
        #print(df_year)
    
        num_students = [new['A+']+new['A'], new['A-'], new['B+'], new['B'], new['B-'], new['C+'], new['C'], new['C-'], new['D+'], new['D'], new['D-'], new['F']]
        
        gpa = [4.00, 3.67, 3.33, 3.00, 2.67, 2.33, 2.00, 1.67, 1.33, 1.00, 0.67, 0.00]
        total = sum(num_students, 0)
    
        weighted_sum = []
        for j in range(len(gpa)):
            weighted_sum.append(num_students[j]*gpa[j])
        avg_gpa = sum(weighted_sum) / total
        As = num_students[0] / total

        #print("Year  Instructor      avg gpa   +As  As  B+s Bs  B-s")
        #print("{}  {}  | {} | {}  | {}  ".format(year,instructor,(avg_gpa),total,num_students))
        
        tmp = []
        tmp.append(year)
        tmp.append(instructor)
        tmp.append(avg_gpa)
        tmp.append(num_students)
        data.append(tmp)

    #print(data)    
    df_classyear = pd.DataFrame(data, columns = ['YearTerm', 'Instructor', 'AvgGPA','totalStudents'])
    return df_classyear

def createImages(number, name, year):
    name = name.upper()
    new_df = df.loc[(df['Number'] == number)  & (df['Subject'] == name)]
    data = []
    yrs = []
    ins = []
    gpas = []
    studs = []
    paths = []
    years = new_df.YearTerm.unique()
    df_year = new_df.loc[(new_df['YearTerm'] == year)]
    instructors = df_year.Primary_Instructor.unique()
    df_year
    i = 0
    for instructor in instructors:
        df_instructor = df_year.loc[(df_year['Primary_Instructor']) == instructor]
        new = (df_instructor.sum(axis = 0, skipna = True))

        num_students = [new['A+']+new['A'], new['A-'], new['B+'], new['B'], new['B-'], new['C+'], new['C'], new['C-'], new['D+'], new['D'], new['D-'], new['F']]
        
        gpa = [4.00, 3.67, 3.33, 3.00, 2.67, 2.33, 2.00, 1.67, 1.33, 1.00, 0.67, 0.00]
        total = sum(num_students, 0)
    
        weighted_sum = []
        for j in range(len(gpa)):
            weighted_sum.append(num_students[j]*gpa[j])
        avg_gpa = sum(weighted_sum) / total
        As = num_students[0] / total

        print("{}  {}  | {} | {}  | {}  ".format(year,instructor,(avg_gpa),total,num_students))
        yrs.append(year)
        ins.append(instructor)
        gpas.append(avg_gpa)
        studs.append(num_students)
        tmp = []
        tmp.append(year)
        tmp.append(instructor)
        tmp.append(avg_gpa)
        tmp.append(total)
        data.append(tmp)
        #linegraph(gpa, num_students, instructor)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(gpa, num_students, color='tab:blue')
        ax.set_title(instructor)
        plt.savefig('static/image{}.jpg'.format(i))
        i += 1
        paths.append('static/image{}.jpg'.format(i))


    #print(data)    
    return paths