# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.


s = int(input('Enter the sum of numbers: '))
p = int(input("Enter the result of numbers' multiplication: "))

x = 0
y = 0
for x in range(s):
    for y in range(s):
        if x + y == s and x*y == p:
            print(x, y)
        
            

