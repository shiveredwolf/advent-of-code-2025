
temp = 0
other_count_of_zero = 0
count_of_zero = 0
dial_current = 50
with open("day1_input.txt") as input:

    for x in input:
        temp += 1
        if temp == 200:
            break
        if "L" in x:
            num = int(x[1:])
            print(f"L:{num}")
            new_num = dial_current - num

            if new_num < 0:
                while new_num < 0:
                    new_num = new_num + 100
                    print(f"WL-L:{new_num}")
                    other_count_of_zero += 1
                dial_current = new_num

                if dial_current == 0:
                    count_of_zero += 1
                    print(f"D{dial_current}*******")

            else:
                dial_current = new_num
                print(f"D:{dial_current}-----")

                if dial_current == 0:
                    count_of_zero += 1
                    print(f"D{dial_current}*******")
                    other_count_of_zero += 1

        elif "R" in x:
            num = int(x[1:])
            print(f"R:{num}")
            new_num = num + dial_current

            if new_num > 99:
                while new_num > 99:
                    new_num  = new_num - 100
                    print(f"WL-R:{new_num}")
                    other_count_of_zero += 1
                dial_current = new_num

                if dial_current == 0:
                    count_of_zero += 1
                    print(f"D:{dial_current}********")

            else:
                dial_current = new_num
                print(f"D{dial_current}------")

                if dial_current == 0:
                    count_of_zero += 1
                    print(f"D{dial_current}*******")
                    other_count_of_zero += 1

print(f"number of 0's:{count_of_zero}")
print(f"number of other 0's:{other_count_of_zero}")
#print(f"Total number of 0's:{count_of_zero + other_count_of_zero}")