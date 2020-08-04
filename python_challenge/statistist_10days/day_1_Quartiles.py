# tam = input()
# values = input()
import statistics as st
values = '3 7 8 5 12 14 21 13 18'
values = values.split()
values = [int(x) for x in values]
values.sort()
# print(values)

index_median = 0

def get_median_index(values):
    for i in range(len(values)):
        if (i+1) == ( len(values) // 2):
            if len(values)%2 == 0:
                return i
            else:
                return i + 1
#====================================================
#      
for i in range(len(values)):
    if (i+1) == ( len(values) // 2):
        if len(values)%2 == 0:
            median = (values[i] + values[i + 1]) // 2
            index_median = i
            arr_lef = values[:index_median + 1]
        else:
            median = values[i + 1]
            index_median = i + 1
            arr_lef = values[:index_median]
arr_rigth = values[index_median + 1:]

#Q1
q1_index = get_median_index(arr_lef)

if len(arr_lef) % 2 == 0:
    q1 =  (arr_lef[q1_index] + arr_lef[q1_index + 1]) //2
else:
    q1 = arr_lef[q1_index]
#Q2
q2 = median

#Q3
q3_index = get_median_index(arr_rigth)
if len(arr_lef) % 2 == 0:
    q3 =  (arr_rigth[q3_index] + arr_rigth[q3_index + 1]) //2
else:
    q3 =  arr_rigth[q3_index]

# print(arr_lef)
# print(arr_rigth)
print(q1)
print(q2)
print(q3)



