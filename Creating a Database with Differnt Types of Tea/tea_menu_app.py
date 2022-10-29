import tea_database

Menu_Template = """--Tea Selection App --
Please select an option:

1) Add a type of tea.
2) Find a type of tea.
3) View all the types of teas.
4) View the country the tea originiates from.
5) Exit.

Your selection:"""

def menu():
    connection = tea_database.connect()
    tea_database.create_tables(connection)

    while(user_input := input(Menu_Template)) != "5":
        if user_input == "1":
            insert_new_tea_template(connection)

        elif user_input == "2":
            find_tea_template(connection)

        elif user_input == "3":
            view_all_teas_template(connection)

        elif user_input == "4":
            find_country_template(connection)
            
        else:
            print("Invalid input, please select correct option!")

def insert_new_tea_template(connection):
    type = input("Enter the type of tea: ")
    country = input("Enter which country the tea is from: ")
    rating = int(input("Enter a rating between 1 and 100: "))

    tea_database.insert_tea(connection, type, country, rating)

def find_tea_template(connection):
    type = input("Enter the type of tea to find: ")
    teas = tea_database.get_teas_by_type(connection, type)

    for tea in teas:
        print(f"{tea[1]} ({tea[2]}) - {tea[3]}/100")

def view_all_teas_template(connection):
    teas = tea_database.get_all_teas(connection)

    for tea in teas:
        print(f"{tea[1]} ({tea[2]}) - {tea[3]}/100")   

def find_country_template(connection):
    type = input("Enter the type of tea to find: ")
    country_originated_from = tea_database.Get_Country_Origin(connection, type)

    print(f"{type} originated from the country {country_originated_from[2]}")

menu()