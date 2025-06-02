def calculate_total_spent(num_items):
    total_spent = 0
    for _ in range(num_items):
        price, quantity = map(int, input().split())
        total_spent += price * quantity
    return total_spent

def main():
    initial_money = int(input())
    num_item_types = int(input())
    
    total_spent = calculate_total_spent(num_item_types)
    
    if initial_money - total_spent == 0:
        print("Yes")
    else:
        print("No")
    
if __name__ == "__main__":
    main()