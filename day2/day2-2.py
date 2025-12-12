class Day2:
    result  = 0

    def id_range(self) -> tuple[tuple[int, int], tuple[int, int]]:
        """
        Opens the input file and parses it into a tuple of tuples
        :return: a tuple containing the number ranges.
        """
        with open("day2_input.txt", "r") as f:
            output_data = [ ]
            input_data = f.read()
            input_data = input_data.split(",")
            for x in input_data:
                ids = x.split("-")
                output_data.append(ids)
            return tuple(output_data)

    def checker(self, number):
        num_str = str(number)
        length = len(num_str)
        num_half = length / 2
        current_digit_count = 0
        #print(f"Current Number: {number}*")
        if length == 1: #skips any single digit IDs
            #print(f"Number Skipped: {number}")
            return
        for x in num_str:
            current_digit_count += 1
            current_set = num_str[:current_digit_count]
            #print(f"Current Digits: {current_set}")
            if current_set == num_str[current_digit_count:current_digit_count + current_digit_count]:
                #print(f"Number Found: {number}")
                set_digits = len(current_set)
                num_of_set = num_str.count(current_set)
                ref_num = length // set_digits
                if ref_num == num_of_set:
                    print(f"Number Found: {number}*")
                    self.result += number
                    break





        """for x in num_str:
            current_digit_count += 1
            current_set = num_str[:current_digit_count]
            print(f"Current Digits: {current_set}")

            if current_set == num_str[current_digit_count:current_digit_count + current_digit_count]:
                print(f"Number Found: {number}")

                if number % len(current_set) != 0: continue

                if number % 2 == 0 and len(current_set) % 2 == 0:
                    if number[num_half:] == number[:num_half]:
                        self.result += number"""

    def find_range(self, num_ranges,checker):
        for x in num_ranges:
            start = int(x[0])
            end = int(x[1])
            print(f"Number Range: {start} - {end}")
            for y in range(start, end + 1):

                checker(y)


    def run(self):
        self.find_range(self.id_range(),self.checker)
        print(f"Final Result: {self.result}")


if __name__ == "__main__":
    Day2().run()