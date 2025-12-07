class Day1:
    zero_count = 0
    passing_count = 0
    dial_current = 50

    def splitter(self, direction: str, count: int) -> int:
        """
        Designed to Perform the initial Subtraction and Addition then return the result.
        :param direction: describes the direction the dial needs to turn
        :param count: number of clicks needed to turn
        :return: result of turning the dial
        """
        if direction == "L":
            new_num = self.dial_current - count
        elif direction == "R":
            new_num = self.dial_current + count
        else:
            print("error")
        return new_num

    def zero_check(self, num: int) -> None:
        """
        Designed to check if the number ends on zero then Increment Zero count.
        :param num: the number the dial is currently set to
        """
        if num == 0:
            self.zero_count += 1

    def lap_counter(self, num: int) -> tuple[int,int]:
        """
        Counts the number of laps and returns the laps and remaining number of clicks
        :param num: Number of clicks we need to turn the dial
        :return: Number of laps we have completed around the dial, and remaining number of clicks
        """

        # Aryas Example of a better  solution
        """laps = num // 100
        clicks = num % 100
        return laps, clicks"""

        # this will perform both the flor division and mod at the same time
            #laps, clicks = divmod(num, 100)

        # My Solution
        laps = 0
        while num > 99:
            num -= 100
            laps += 1
        return laps, num

    def checker(self, num: int) -> int:
        """
        Checks if number is greater than or less than the Boundary and that it that is doesnt start on zero, then increment passing count by one.
        :param num: Number of clicks
        :return: Remaining clicks after Modulus
        """
        if (num <= 0 or num > 99) and self.dial_current != 0:
            self.passing_count += 1

        return num % 100

    def run(self):
        """
        Runs the Bulk of the code.
        """
        with open("day1_input.txt", "r") as f:
            for x in f:
                # separates the Direction and number from the Input.
                direction = x[0]
                clicks = int(x[1:])

                # takes in the number of laps and clicks left over, increments the passing count by number of laps then passes clicks into the splitter function.
                laps, clicks = self.lap_counter(clicks)
                self.passing_count += laps
                new_num = self.splitter(direction, clicks)
                new_num = self.checker(new_num)
                self.zero_check(new_num)
                self.dial_current = new_num



        # Prints the Final Results of the Code
        print("Final Result 1: ", self.zero_count)
        print("Final Result 2: ", self.passing_count)

if __name__ == "__main__":
    Day1().run()