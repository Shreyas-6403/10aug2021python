from prettytable import PrettyTable


t = PrettyTable(['Id', 'Name', 'Mobile Number', 'Email Address', 'Salary', 'Blood Group'])

emp_Id=str(input("\nEnter your Employee Id: "))
name=str(input("\nEnter your name: "))
mobile=str(input("\nEnter your mobile number: "))
email=str(input("\nEnter your email id: "))
salary=str(input("\nEnter your salary: "))
blood=str(input("\nEnter your blood group: "))

inputs = [emp_Id, name, mobile, email, salary, blood ]
t.add_row(inputs)
print(t)


# print("\n")
# print("-------------------ID Card----------------------")
# print("|    Employ Id                ",Emp_Id)
# print("|    Employ Name              ",name)
# print("|    Employee Mobile Number   ",mobile)
# print("|    Employee Email Number    ",email)
# print("|    Employ Salary            ",salary)
# print("|    Employee Blood Group     ",blood)

# print("------------------------------------------------")

