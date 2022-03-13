import csv
import sys
import pandas as pd

#to get the name from col_list based on index 'i'
def getColName(i, col_list):
    col = col_list[i]
    return col


def list_Toppers(df, col_list):
    for i in range(1, 7):
        col = getColName(i, col_list)

		#find the highest mark in a single subject
        max_marks.append(max(df[col]))

		#Retreiving only the 'Name' and column to find the topper(s)
        name = pd.read_csv(file_name, usecols=["Name", col], index_col=False)

		#Getting the name and marks of the student 
		# if he/she scores the highest mark in that subject, and converting them to a list
        temp = name[name[col] == max_marks[i-1]].values.tolist()
        if(len(temp) == 1):
            print("\nTopper in ", col, " is ", temp[0][0])
        if(len(temp) == 2):
            print("\nTopper in ", col, " is ", temp[0][0], ",", temp[1][0])

#to get the second element from the list
def takeSecond(elem):
    return elem[1]

def list_Ranks(df, col_list, file_name):
	total_marks = []
	with open(file_name, 'r') as f:
		mycsv = csv.reader(f)
		next(mycsv)
		for row in mycsv:
			temp=[]
			total=int(row[1]) + int(row[2]) + int(row[3]) + int(row[4]) + int(row[5]) + int(row[6])
			temp.append(row[0])
			temp.append(total)
			total_marks.append(temp)
	#sorting the list based on the student's total in reverse order
	total_marks.sort(key=takeSecond,reverse=True)
	print("\nBest students in the class are ",total_marks[0][0],",",total_marks[1][0],",",total_marks[2][0],"\n")

if __name__ == '__main__':

	#get file name from the arguement
    file_name = sys.argv[1]

    data = pd.read_csv(file_name)

    col_list = ["Name", "Maths", "Biology",
                "English", "Physics", "Chemistry", "Hindi"]

    df = pd.read_csv("Student_marks_list.csv", usecols=col_list)

    # list which contains the highest marks recieved
    # by a student in a single subject
    max_marks = []

	#to list the toppers in each subject
    list_Toppers(df, col_list)

	#to list the top 3 rank holders
    list_Ranks(df, col_list, file_name)
    
