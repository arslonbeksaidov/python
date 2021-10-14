# ------------- Gapni boshlashda katta harf bilan boshlash uchun.
txt = "hello, and welcome to my world."

x = txt.capitalize()

# -------------- Textni kichik harflarga o'tkazib chiqadi.
txt = "Hello, And Welcome To My World!"

x = txt.casefold()
# --------------- Textni berilgan son bo'yicha shuncha marta o'ngga suradi

txt = "banana"

x = txt.center(5)

#------------ Berilgan string ni text ni ichida nechi marta qatnashganini hisoblaydigan funksiya. # ta parametri bor 1- qidirilayotgan text, 2- boshlang'ich o'rni, 3- tugash o'rni.
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

# ------------------------ Text berigan so'z bilan tugaydimi params:(value,start,end)
txt = "Hello, welcome to my world."

x = txt.endswith(".")
# -------------------------- Tablarni berilgan son bo'yicha qo'yish
txt = "H\te\tl\tl\to"

x =  txt.expandtabs(3)
# ------------------  Berilgan textni topish va uni textda qaysi indexdan boshlanganini qaytarish. Agar topmasa -1 qaytaradi. Params: (value,start, end)
txt = "Hello, welcome to my world."

x = txt.find("welcome") # 7
# -------------------- Textni formatlab chiqarish
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49)) 
# ------------------------------Text ni ichidan textni qidirish , agar topsa birinchi harfni indexini chiqarish agar topolmasa error berish.Params: value, start, end
 txt = "Hello, welcome to my world."

x = txt.index("e")
# ------------------------------ Text ichida faqat raqam va harflar bo'lsa True qaytaradi agan @#$ topilsa False qaytadi.
txt = "Company 12"

x = txt.isalnum()
# ----------------------------- Agar hamma belgilar harflarda iborat bo'lsa True aks holda False. @$%12 lar harflar emas agar qatnashsa False.
txt = "CompanyX"

x = txt.isalpha()

print(x)



