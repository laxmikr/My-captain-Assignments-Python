import csv

def write_func(info_list):
    with open("info.csv",'a', newline='') as file:

        writer=csv.writer(file)
        if file.tell()==0:
            writer.writerow(['Name','Age','Contact Number','E-mail'])
        writer.writerow(info_list)

if __name__ == '__main__':
    condition=True
    student=1
    while(condition):
        student_info=input("Enter the information of the student {} in following format(Name, Age, Contact Number, E-mail id): ".format(student))
        student_info_list=student_info.split(" ")
        print("\nEntered information-\nName:{}\nAge:{}\nContact Number:{}\nE-mail:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input("Is the information correct(yes/no): ")
        if choice_check=='yes':
            write_func(student_info_list)
            check=input("Do you want to add another student(yes/no): ")
            if(check=="yes"):
                condition=True
                student=student+1
            elif check=="no":
                condition=False
            else:
                print("Please enter a valid choice")


        elif choice_check=='no':
            print("Enter the correct values : ")
