
# from django.shortcuts import render

# def Home(request):
#     # Constants
#     MIN_MARKS = 40
#     PASS_STATUS = "PASS"
#     FAIL_STATUS = "FAIL"

#     # Get student name
#     name = request.GET.get('username')

#     # Get marks for each subject and convert to integers, handle potential conversion errors
#     subjects = ['sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6']
#     try:
#         marks = [int(request.GET.get(sub, 0)) for sub in subjects]
#     except ValueError:
#         return HttpResponse("Invalid input! Marks should be integers.")

#     # Calculate total marks and percentage
#     total_marks = sum(marks)
#     percentage = total_marks // len(marks)

#     # Determine pass/fail status for each subject
#     remarks = [PASS_STATUS if mark >= MIN_MARKS else FAIL_STATUS for mark in marks]

#     # Render the result with calculated data
#     return render(request, 'Result.html', {
#         'Name': name,
#         'Min': MIN_MARKS,
#         'sub1M': marks[0],
#         'sub2M': marks[1],
#         'sub3M': marks[2],
#         'sub4M': marks[3],
#         'sub5M': marks[4],
#         'sub6M': marks[5],
#         'Total': total_marks,
#         'subR1': remarks[0],
#         'subR2': remarks[1],
#         'subR3': remarks[2],
#         'subR4': remarks[3],
#         'subR5': remarks[4],
#         'subR6': remarks[5],
#         'Percentage': percentage
#     })

a=1
sum=0
while(a!=21):
    sum=sum+a
    a=a+1
print("sum=",sum)