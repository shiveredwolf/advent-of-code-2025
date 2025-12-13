class Day3:
    result = 0

    def data_input(self):
        battery_banks = [ ]
        with open("day3_input.txt", "r") as f:
            for x in f.readlines():
                battery_banks.append(x.strip())
            #print(battery_banks)
        return battery_banks

    def joltage_calc(self):

        for x in self.data_input():
            battery1, battery2 = -1, -1
            b_index1, b_index2 = -1, -1
            print(f"Current battery Bank: {x}")
            for y in range(9, -1, -1):
                if str(y) in x:
                    if battery1 == -1 and x.find(str(y)) != len(x) - 1:
                        battery1 = y
                        b_index1 = x.find(str(y))
                        print(f"battery1: {battery1}")
                        print(f"b_pos1: {b_index1}")
                        break
                    else: continue
            for t in range(9, -1, -1):
                if str(t) in x:
                    if battery2 == -1 and x.find(str(t)) > b_index1:
                        battery2 = t
                        b_index2 = x.find(str(t))
                        print(f"battery2: {battery2}")
                        print(f"b_pos2: {b_index2}")
                        break
                    else: continue
            print(f"Joltage: {battery1}{battery2}")

if __name__ == "__main__":
    Day3().joltage_calc()