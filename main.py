import converter
def main():
    print("================Welcome to the Currency Converter================\n")
    base_curency = str(input("Enter the base currency code: "))
    target_curency = str(input("Enter the target currency code: "))
    amount = float(input("Enter the amount you want to convert: "))
    converter.convert(base_curency,target_curency,amount)
    print("\n")
    print("Do you want to convert another currency? (yes/no)")
    answer = input()
    if answer == 'yes':
        main()
    else:
        print("\n================Thanks for using our service================")

if __name__ == "__main__" :
    main()