def number_adder():
    def get(order):
        while True:
            try:
                num = int(input(f'Enter your {order} integer: '))
                
                if num > 0:
                    return num   
            except ValueError:
                print("Please input an integer")

    def num():
        a = get("first")
        b = get("second")
        print(a+b)

    def main():
        print('This allows you to add numbers')
        
        while True:
            num()
            again = input('run again? y/n ').lower()
            
            if again == 'n':
                break
    main()