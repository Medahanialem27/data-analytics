department_code = 27
match department_code:
    case 1:
     print("Marketing")
    case 5:
     print("Human Resources")
    case 10:
     print("Acounting")
    case 12:
     print("Legal")
    case 18:
     print("IT")
    case 20:
     print("Customer Relations")
    case _:
     print("Unknown department")