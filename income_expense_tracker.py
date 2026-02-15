import json
from datetime import datetime

def entering():

    date_format = "%Y-%m"
    name = input("Enter income's source or expence:").strip()

    while True:
        try:
            Amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid Amount. Try again.")
   
    while True:        
        Date = input("Enter date YYYY-MM:").strip()
        try:
            date_obj = datetime.strptime(Date,date_format)
            date_str = date_obj.strftime("%Y-%m")
            break
        except ValueError:
            print("Invalid date format. Try again.")
   
    Description = input("Enter Description: ").strip()
    return  name, Amount, date_str, Description


def add_expense():
    
    expense_data = load_data("expenses1.json")
    
    category, Amount, date_str, Description = entering()
    
    expense_info = {        
            "Category": category,
            "Amount": Amount,
            "Date": date_str,
            "Description": Description
    }
    
    expense_data.append(expense_info)
    save_data("expenses1.json",expense_data)

def add_income():

    incomes_data = load_data("incomes.json")

    Source, Amount, date_str, Description = entering()
    
    income_info = {
        "Source" : Source,
        "Amount" : Amount,
        "Date"   : date_str,
        "Description" : Description
    }
    
    incomes_data.append(income_info)         
    save_data("incomes.json", incomes_data)


def save_data(filename, data):
   with open(filename,"w")as f:
       json.dump(data, f, indent=4)


def load_data(filename):
    try:
        with open(filename,"r")as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def check_date():
    load_income = load_data("incomes.json")
    load_expense = load_data("expenses1.json")

    date_format = "%Y-%m"
    date_stack = []

    while True:
        date = input("Enter the date YYYY-MM: ")
        try:
            date_obj = datetime.strptime(date, date_format)
            date_str = date_obj.strftime("%Y-%m")
            break
        except ValueError:
            print("Invalid date format. Try again.")

    for item in load_income:
        date_stack.append(item["Date"])

    for item in load_expense:
        date_stack.append(item["Date"])

    if date_str not in date_stack:
        print(f"No Data for {date_str}")
        return None
    else:
        return date_obj



def reports(load,date): 
    results = []
    if not load  :
        return []  
    for c in load:
        if  date == c["Date"] and "Category" in c and "Amount" in c :
              results.append((c['Category'],c['Amount']))
        elif date == c["Date"] and  "Source" in c and "Amount" in c: 
              results.append((c['Source'],c['Amount']))
    return results
        

def category_report_view():
   load_expense = load_data("expenses1.json")
   date_format = "%Y-%m"
   date_str = ""
   date_cat = check_date() 
   if date_cat is None:
      return 
   date_str = date_cat.strftime("%Y-%m") 
   category_amount = reports(load_expense,date_str)
   for i, j in category_amount: 
       print(f"{i:<4}: {j:>8.1f}\n")


def monthly_summary_view():
   
   date_format = "%Y-%m"
   date_str = ""
   date_month = check_date() 
   if date_month is None:
      return 
   date_str = date_month.strftime("%Y-%m") 
   total_income, total_expenses, savings = monthly_summary(date_str)
   print(f"Total income:${total_income}\nTotal expenses:${total_expenses}\nSavings:${savings}") 
        
def monthly_summary(date):
       load_income = load_data("incomes.json")
       load_expense = load_data("expenses1.json") 
    
       if not load_expense and not load_income:
            print("\nNo expenses or income.\n")
            return 0, 0, 0 
           
       total_expenses = sum(exp["Amount"] for exp in load_expense if date == exp["Date"])
       total_income = sum(i["Amount"] for i in load_income if date == i["Date"])
       savings = total_income - total_expenses
       return total_income, total_expenses, savings 

    
def export_report():
    
   load_income = load_data("incomes.json")
   load_expense = load_data("expenses1.json")
   label_width = 15
    
   centered_line = "Expense Breakdown".center(30, "=")
   centered_line2 = "Income Sources".center(30, "=")
   date_rep = check_date() 
   if date_rep is None:
      return 
   date_str = date_rep.strftime("%Y-%m") 
   date_str1 = date_rep.strftime("%Y_%m")
   time_now = datetime.now()
    
   monthly_report = f"report_{date_str1}.txt"
    
   total_income, total_expenses, savings = monthly_summary(date_str)
   category_amount = reports(load_expense,date_str) 
   income_amount = reports(load_income,date_str)
 
   str_result = f"{'=':=>29}\n{'MONTHLY FINANCIAL REPORT':^30}\n{date_str:^30}\n{'=':=>29}\n\n{'Total Income' :<{label_width}}: ${total_income:>8.1f}\n{'Total Expenses' :<{label_width}}: ${total_expenses:>8.1f}\n{'-':->29}\n{'Savings' :<{label_width}}: ${savings:>8.1f}\n\n{centered_line}\n" 
   
   with open(monthly_report,"w")as f:
       f.write( str_result )
   if category_amount == None:
        with open(monthly_report,"a")as f:
               f.write("No Expense for this month!!!\n")
   else: 
       for i, j in category_amount:           
           with open(monthly_report,"a")as f:
               f.write(f"{i:<{label_width}}: ${j:>8.1f}\n")

   with open(monthly_report,"a")as f:
           f.write(f"{centered_line2}\n")         

   if income_amount == None:
        with open(monthly_report,"a")as f:
               f.write("No income for this month!!!\n") 
   else:         
        for i, j in income_amount:
           with open(monthly_report,"a")as f:
               f.write(f"{i:<{label_width}}: ${j:>8.1f}\n")
       
   with open(monthly_report,"a")as f:
       f.write(f"\n{'=':=>29}\n{'Generated on' :<{label_width}}: {time_now}\n{'=':=>29}")
   print(f"Monthly report generated successfully! \nFile saved as:{monthly_report}")
    

def main():

    while True:
        print("1 - Add Income")
        print("2 - Add Expense")
        print("3 - Monthly Summary")
        print("4 - Category Report")
        print("5 - Export Report")
        print("E - Exit")
        
        choose = input("Enter number:").lower()

        if choose == '1':
            add_income()
        elif choose == '2':
            add_expense()
        elif choose == '3':
            monthly_summary_view()
        elif choose == '4':
            category_report_view()
        elif choose == '5':
            export_report()
        elif choose == 'e':
            break
        else:
            print("Please choose number from the list ")

if  __name__ == "__main__":
    main()

