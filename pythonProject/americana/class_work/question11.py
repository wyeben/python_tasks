from datetime import datetime


input_date = input("Enter the date for the exams (YYYY-MM-DD HH:MM:SS): ")
exam_date = datetime.strptime(input_date, "%Y-%m-%d %H:%M:%S")
current_date = datetime.now()

time_difference = exam_date - current_date

print(f"The examination will start in {time_difference}")