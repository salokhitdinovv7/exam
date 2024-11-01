#Amaliy
# 1. while siklining ishlash tartibini tushuntirib bering? 
# Javob:While sik bu forga oxshidi va for bilan while ning farqi while cheksiz aylanadi 
# Misol👇
# while True:
#     print("Bu Natija", end=" ")
# 2. List ma’lumot turidagi append() va expand() metodlari orasiddagi farq nimada?
# javob: Extend bilan append ning farqi extend listga str qoshadi va append esa intni va str ni qo'shadi
# list = [7,8,9]
# list.extend('b')
# list.append(12)
# 3. Dict ma’lumot turida dict ichidagi ma’lum bir elementni o’chirishning qanday usullari mavjud?
# Javob Dictda pop funcsiyasini ishlatidim va 3 sonini berdim pop  funcsiyasi boyicha savol berishingiz mumkin va niima vazifani bajaradi deb pop itemlarni ochirib tashlaydi
# Misol 👇
# dict = {
#     1:{'a'},
#     2:{'b'},
#     3:{'c'}
# }
# dict.pop(2)
# print(dict)
# 4. For orqali sonlarni teskari tartibda chiqarish uchun nima qilish kerak?
# Nima uchun -1 va -1 qildimm -1 bu teskari tartibda chiqaridh uchun 
#Misol👇
# for i in range(100,-1,-1):
#     print(i)


#nazariy


# Students nomli bo’sh dict yaratilsin. While True orqali shu dictga element qo’shish, elementni chiqarish, elementni yangilash va elementni o’chirish buyruqlari bo’lsin. Ya’ni whileni ichida savol nomli o’zgaruvchi inputda son qabul qiladi.

# savol = int(input(”””

# 1. Student qo’shish
# 2. Studentlarni chiqarish
# 3. Studentni chiqarish
# 4. Studentni o’chirish

# Buyruqlardan birini tanlang: “””)

# 1- vazifa:

# Agar savol 1ga teng bo’lsa, Students nomli dictga student_id ni kalit sifatida, uning ismi, familiyasi guruh nomini o’sha kalitning qiymat(value)i sifatida qo’shilsin.

# 2-vazifa:

# Agar savol 2ga teng bo’lsa, barcha studentlar ma’lumotlari tartib bilan chiqarilsin

# 3-vazifa:

# Agar savol 3ga teng bo’lsa, student_id so’ralsin va o’sha student_id ga qiymat sifada kiritilgan studentning ismi, familiyasi va guruh printga chiqarilsin

# 3-vazifa:

# Agar savol 4ga teng bo’lsa, student_id so’ralsin va o’sha studnet_id ga qiymat sifatida kiritilgan ma’lumotlar va o’sha student_id ga teng bo’lgan kalit ham dictdan o’chirib yuborilsin
# Misol👇
student = {
    1:{"Name":"Ziynatulloh", "School":"249", "Class": 10,"Age":15},
    2:{"Name":"Salohitdin" ,"School":"232", "Class": 8,"Age":46},
    3:{"Name":"Asomiddin", "School":"45", "Class": 11,"Age":35},
    4:{"Name":"Zaynidddin", "School":"324", "Class": 9,"Age":15}
}

while True:
    change = int(input("1:Student QO'shish \n2:Studentlarni Chiqarish \n3:Studentni Chiqarish \n4: Studentni o'chirish\n -> "))
    if change == 1:
        for i in range(1):
         student_name = input("Name: ")
         students_school = input("chool: ")
         student_grade = input("Grade: ")
         student_age = input("Age: ")
        student[len(student)+1] = {"name": student_name,"schooll":students_school, "Grade": student_grade, "age": student_age}
        for key,vaule in student.items():
           print(key,vaule)
    elif change == 2:
       for key,value in student.items():
          print(key,value)
    elif change == 3:
          student_id = int(input("Srudentni Tanlang: 1,2,3,4 "))
          if student_id==1:
              print(student[1])
          elif student_id==2:
              print(student[2])
          elif student_id==3:
              print(student[3])
          elif student_id==4:
              print(student[4])
    elif change == 4:

        rem = int(input("Srudentni  Qaysibirini O'chirmoqchisiz: 1,2,3,4 "))
        if rem == 1:
          student.pop(1)
          print(student)
        elif rem == 2:
          student.pop(2)
          print(student)
        elif rem == 3:
          student.pop(3)
          print(student)
        elif rem == 4:
          student.pop(4)
          print(student)
        else:
           print(" 1 dan 4 tagacha bo'lgan sonlarni kiriting: ")


         