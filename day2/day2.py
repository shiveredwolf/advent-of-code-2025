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

    def find_dupes(self, num_ranges):
        """
        Splits the numbers in half and compares the first half to the second half
        :param num_ranges: Expects the tuple containing the number ranges.
        """
        for x in num_ranges:
            start = int(x[0])
            end = int(x[1])
            print(f"start: {start}, end: {end}")
            for y in range(start, end + 1):
                num_length = len(str(y))
                current_id = str(y)
                half_number = num_length / 2

                #remove odd sized numbers
                if int(num_length) % 2 == 0:

                    #Checks if the first half of each number is the same as the second half
                    if current_id[:int(half_number)] == current_id[int(half_number):]:
                        self.result += int(current_id)
                else:
                    continue


    def run(self):
        self.find_dupes(self.id_range())
        print(f"Final Result: {self.result}")


if __name__ == "__main__":
    Day2().run()