age=int(input("ป้อนอายุของคุณ :"))
#35
if age>=15 and age <=20:  #15-20
    print("วัยรุ่น")
elif age>=21 and age<=29:   #21-29
    print("วัยหนุ่มสาว")
elif age>=30 and age<=39:   #30-39
    print("วัยผู้ใหญ่")
elif age>=80:               #>=80
    print("วัยชรา")
else :                      #ไม่เข้ากรณีใดเลย     
    print("วัยเด็ก")

print("จบโปรแกรม")

# 15 - 20 => วัยรุ่น
# 21 - 29 => วัยหนุ่มสาว
# 30 - 39 => วัยผู้ใหญ่


# and or not 

#การเขียนโปรแกรมคำนวณเกรด
# จาก 0->100 (Yes)
# 80->0 (no)


#Ternary Operator
print("วัยรุ่น") if age>=15 else print("วัยเด็ก")

print("จบโปรแกรม")