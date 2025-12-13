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

    def checker(self, number:int):
        """
        Checks if the given number is a valid ID
        :param number: Current number we are checking
        """
        num_str = str(number)
        length = len(num_str)
        current_digit_count = 0
        if length == 1: return #skips any single digit IDs

        for x in num_str:
            current_digit_count += 1
            current_set = num_str[:current_digit_count]
            if current_set == num_str[current_digit_count:current_digit_count + current_digit_count]:
                set_digits = len(current_set)
                num_of_set = num_str.count(current_set)
                ref_num, zero_check = divmod(length, set_digits)
                if ref_num == num_of_set and zero_check == 0:
                    self.result += number
                    break


    def run(self):
        """
        loops the numbers in a given ID range and checks if the number is valid
        """
        for x in self.id_range():
            start = int(x[0])
            end = int(x[1])
            for y in range(start, end + 1):
                self.checker(y)
        print(f"Final Result: {self.result}")


if __name__ == "__main__":
    Day2().run()