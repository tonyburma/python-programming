def main():
    math = float(input("Enter Math score:"))
    eng = float(input("Enter English score:"))
    sci = float(input("Enter Science score:"))
    total = math + eng + sci
    average = total / 3

    if average >= 80 and math >= 75 and eng >= 75:
        print("Eligible for admission")
    else:
        print("Not eligible for admission")

main()