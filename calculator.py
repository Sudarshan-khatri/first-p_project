# import math function for perform various type of operation such as trignometric function ,hyperbolic function etc
import math as mp
# In this calculator ,we can make simple calculator using different operation
# 1: Basic calculator that perform addition ,subtraction,product,division operation
# 2:Basic calculator that perform trignometric function
# 3:Calculator that perform hyperbolic function
# 4:calculator that perform power and logrithmic function
# 5:calculator that can convert angle
# import colorma for setting the color
#import fraction to find output in fraction method
from fractions  import Fraction
from colorama import Fore ,Style
print("\n\n\n")
# impor pyfiglet for making the calculator more attractive
import pyfiglet
s_format=pyfiglet.figlet_format("WELCOME   TO   MINI   CALCULATOR",font="mini")
print(f"{Fore.RED}{s_format}")
print(f"{Fore.GREEN}1:Arithmetic operation        {Fore.YELLOW}  2:Trignometic operation")
print(f"{Fore.MAGENTA}3:Hyperbolic operation      {Fore.CYAN}    4:Expon & log operation")
# create the choice for using case for every operation
choice=int(input(f"{Fore.LIGHTCYAN_EX}Enter the choice:"))
# matching the choice 
match choice:
    case 1:
        print("\n\n\n")
        print(f"{Fore.RED}WELCOME TO ARITHMETIC OPERATION")
        print(f"{Fore.GREEN}a:Addition operation       {Fore.YELLOW}  b:Subtraction operation")
        print(f"{Fore.MAGENTA}c:Multiplication operation {Fore.CYAN}  d:Division operation")
        alp=str(input("Enter the choice for arithmetic operation:"))
        # matchin case for artihmetic operation
        match alp:
            # case a for find the sum of number given by user using function and loop 
            case 'a':
                def sum():
                    n=int(input("Enter the number to find sum:"))
                    sum=0
                    for i in range(n):
                        s_num=float(input(f"Enter the number{i+1}:"))
                        sum+=s_num
                    print(f"{Fore.LIGHTGREEN_EX}sum of {n} number :{sum}")
                # calling the function
                sum()
            case 'b':
                # this function subtract float number from randomly in sequence like 1-2-3-..................
                def sub():
                    s_num=int(input("Enter the number for subtraction:"))
                    sub_t=0
                    for i in range(s_num):
                        sub_num=float(input(f"Enter the number{i+1}:"))
                        sub_t-=sub_num
                    print(f"{Fore.LIGHTGREEN_EX}subtraction of {s_num} number:{sub_t}")
                #Calling the function 
                sub()
            # find the product of given number using the function and loop
            case 'c':
                def prod():
                    p_num=int(input("Enter the how many number you want to multiply:"))
                    p_prod=1
                    for i in range(p_num):
                        m_num=float(input("Enter the number:"))
                        p_prod*=m_num
                    print(f"{Fore.LIGHTGREEN_EX}product of {p_num} number:{p_prod}")
                #calling function
                prod()
            # find the division of two number
            case 'd':
                def div(num1,num2):
                  if num2!=0:
                      return num1/num2
                  else:
                      return 0
                # calling the function
                # n1 represent numenator number and n2 represent denominator number for divison 
                n1=float(input("Enter numenator number"))
                n2=float(input("Enter denomenator number"))
                result=div(n1,n2)
                print(f"{Fore.LIGHTGREEN_EX}Division:{result}")
    case 2:
        print("\n\n\n")
        print(f"{Fore.RED}WELCOME TO TRIGNOMETRIC  OPERATION")
        print(f"{Fore.GREEN}A:Sine        {Fore.YELLOW}  B:Cosine")
        print(f"{Fore.MAGENTA}C:Tan")
        u_alp=str(input("Enter the option(A/B/C):"))
        # matchin the case with upper case string  
        match u_alp:
            # case A is for finding the value of sine angle 
            case 'A':
                angle_in_degree=float(input("Enter the angle:"))
                angle_in_radian=mp.radians(angle_in_degree)
                value=mp.sin(angle_in_radian)
                # limit_denominator avoid the large denominator
                sine_fraction=Fraction(value).limit_denominator()
                # Rounding the sine value
                v_rounded = round(value, 3)
                print(f"{Fore.LIGHTGREEN_EX}value of sin{angle_in_degree}::{v_rounded}")
                print(f"{Fore.LIGHTGREEN_EX}value of sin{angle_in_degree}::{sine_fraction}")
            
            # case B for finding the  value of cosine angle
            case 'B':
                angle_degree=float(input("Enter the angle:"))
                angle_radian=mp.radians(angle_degree)
                c_value=mp.cos(angle_radian)
                # convert the cosine value in Fraction
                c_fraction=Fraction(c_value).limit_denominator()
                #rounding the cosine value
                c_rounded=round(c_value,3)
                print(f"{Fore.LIGHTGREEN_EX}value of cos{angle_degree}::{c_rounded}")
                print(f"{Fore.LIGHTGREEN_EX}value of cos{angle_degree}::{c_fraction}")
            # case c for finding the  value of tangent angle
            case 'C':
                t_degree=float(input("Enter the angle:"))
                t_radian=mp.radians(t_degree)
                t_value=mp.tan(t_radian)
                # convert the cosine value in Fraction
                t_fraction=Fraction(t_value).limit_denominator()
                #rounding the cosine value
                t_rounded=round(t_value,3)
                print(f"{Fore.LIGHTGREEN_EX}value of cos{t_degree}::{t_rounded}")
                print(f"{Fore.LIGHTGREEN_EX}value of cos{t_degree}::{t_fraction}")
    case 3:
        print("\n\n\n")
        print(f"{Fore.RED}WELCOME TO HYPERBOLIC  OPERATION")
        print(f"{Fore.GREEN}x:SinhX       {Fore.YELLOW}  y:CoshX")
        print(f"{Fore.MAGENTA}z:TanhX")
        opt=str(input("Enter the option(x/y/z):"))
        # matching case for the hyperbolic function
        match opt:
            # case x for finding the value of hyperbolic sine function 
            case 'x':
                def v_sine(value):
                    return mp.sinh(value)
                # calling the value 
                a_degree=float(input("Enter the angle in degree:"))
                a_rad=mp.radians(a_degree)
                sinhx=v_sine(a_rad)
                # rounded value in decimal 
                s_rounded=round(sinhx,3)
                print(f"value of sinh{a_degree}::{s_rounded}")
            # case y for  find the value of hyperbolic cos function 
            case 'y':
                def v_cos(value1):
                    return mp.sinh(value1)
                # calling the value 
                h_degree=float(input("Enter the angle in degree:"))
                h_rad=mp.radians(h_degree)
                coshx=v_cos(h_rad)
                # rounded value in decimal 
                h_rounded=round(coshx,3)
                print(f"value of cosh{h_degree}::{h_rounded}")
            # case z for  find the value of hyperbolic cos function 
            case 'z':
                def v_tan(value2):
                    return mp.sinh(value2)
                # calling the value 
                t_degree=float(input("Enter the angle in degree:"))
                t_rad=mp.radians(t_degree)
                tanhx=v_tan(t_rad)
                # rounded value in decimal 
                t_rounded=round(tanhx,3)
                print(f"value of cosh{t_degree}::{t_rounded}")
    case 4:
        print("\n\n\n")
        print(f"{Fore.GREEN}X:Power     {Fore.YELLOW}  Y:lograthmetic operation")
        print(f"{Fore.MAGENTA}Z:Exponential operation")
        opt1=str(input("Enter the option:"))
        #match the following operation using match
        match opt1:
            # case X for find the power of the given number
            case 'X':
                print("\n")
                def b_power(base,power):
                    return mp.pow(base,power)
                # calling the function 
                base1=int(input("Enter the base number:"))
                power1=int(input("Enter the power number:"))
                result=int(b_power(base1,power1))
                print(f"{base1} power {power1}::{result}")
            case 'Y':
                print("\n")
                def log_fun(num):
                    if num==0:
                        return 1
                    
                    







                     

                       

