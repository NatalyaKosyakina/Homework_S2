# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import math

num_s = int(input("Сумма загаданных чисел:  "))
num_p = int(input("Произседение загаданных чисел:  "))

diskriminant = num_s*num_s - num_p*4
if diskriminant < 0 :
    print("Таких чисел нет")
else :
    num_x1 = int((num_s + math.sqrt(diskriminant)) / 2)
    num_x2 = int((num_s - math.sqrt(diskriminant)) / 2)
    print(num_x1, num_x2)