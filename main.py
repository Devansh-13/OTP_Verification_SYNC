import random
import smtplib

digits = ["0","1","2","3","4","5","6","7","8","9"]
otp=""
for i in range(6):
    otp+=random.choice(digits)

gen_otp = int(otp)

connection = smtplib.SMTP("smtp.gmail.com", 587)

connection.starttls()

connection.login(user="devansh15091970@gmail.com", password="okaeyataubltgeuz")

email = input("Enter Your email:")

connection.sendmail(from_addr="devansh15091970@gmail.com", to_addrs=email, msg=f"Subject:OTP "
                                                                                                        f"verification \n\nYour OTP is {gen_otp}")

connection.close()

a = int(input("Enter your OTP:"))

if a==gen_otp:
    print("Verified")

else:
    print("Please check your OTP again!")