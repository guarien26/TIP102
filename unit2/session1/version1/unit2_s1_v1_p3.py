def total_sales(ticket_sales):
    return sum([val for val in ticket_sales.values()])

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))