"""
Exercise (3): Advanced Customer Data Manipulation

Tasks:
1. Print the name of each customer who is a VIP member.
   - Iterate through the list of customers and check the 'vip_member' key.
   - Print the names of customers where 'vip_member' is True.

2. Calculate the total amount spent by each customer:
   - Sum up the amounts from all orders in the 'order_history' for each customer.
   - Add the total amount as a new key-value pair ('total_spent') to each customer's data.

3. Check if any customer has placed more than 5 orders:
   - If a customer has more than 5 orders in their 'order_history', print that the customer is a "frequent shopper."

4. Update the preferences for customers who have spent more than $1000:
   - If a customer has spent more than $1000, add "Exclusive Discounts" to their list of preferences.

   """

# Data
customers = [
    {
        "name": "Emily Carter",
        "age": 34,
        "email": "emily.carter@example.com",
        "order_history": [
            {"order_id": 101, "amount": 120},
            {"order_id": 102, "amount": 80},
            {"order_id": 103, "amount": 200}
        ],
        "preferences": ["Electronics", "Fashion"],
        "vip_member": False
    },
    {
        "name": "James Brown",
        "age": 28,
        "email": "james.brown@example.com",
        "order_history": [
            {"order_id": 104, "amount": 300},
            {"order_id": 105, "amount": 150},
            {"order_id": 106, "amount": 250},
            {"order_id": 107, "amount": 100},
            {"order_id": 108, "amount": 400},
            {"order_id": 109, "amount": 50}
        ],
        "preferences": ["Home Decor", "Books"],
        "vip_member": True
    },
    {
        "name": "Sophia Lee",
        "age": 42,
        "email": "sophia.lee@example.com",
        "order_history": [
            {"order_id": 110, "amount": 600},
            {"order_id": 111, "amount": 450},
            {"order_id": 112, "amount": 300}
        ],
        "preferences": ["Fitness", "Outdoor Gear"],
        "vip_member": True
    }
]


"""
(1): Print the name of each customer who is a VIP member
"""
for customer in customer 
    if
print("name")

"""
(2): Calculate the total amount spent by each customer and store it in 'total_spent'
"""
for customer in customers:
    orders = customer['order_history']
    total_amount = 0

    for order in orders:
        amount = order['amount']
        total_amount = total_amount + amount
    
    customer['total_spent']=total_amount

print(customers)
"""
(3) Check if any customer has placed more than 5 orders
"""
for customer in customers:
    order_count= len(customer['order_history'])
    if order_count > 5:
        print(customer['name'])

"""
(4) Update the preferences for customers who have spent more than $1000
"""

for customer in customers:
    print(customer['total_spent'])
    if customer["total_spent"] > 1000:
        customer['preferences']='over spend'
print(customer)
