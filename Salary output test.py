def days_check(user_input):
    if user_input<30:
        return f"You won't get any salary"
    elif user_input<366:
        return f"You will get {user_input//30} month(s) salary"
    else:
        return f"You didn't recieve any salary last one year. You won't get anymore"

def output_execution():
    if data.isdigit():
        output=days_check(int(data))
        print(output)
    else:
        print(f"Enter your exact day's count in digit. Don't ruin my programme")

data=''
while data!='exit':
    data = input('Enter your total working days\n>> ')
    output_execution()