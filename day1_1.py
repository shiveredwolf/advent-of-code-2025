
class Day1:
    stop = 0
    while_count = 0
    zero_count = 0
    passing_count = 0
    dial_current = 50

    def counter(self, direction, count):
        if direction == "L":
            new_num = self.dial_current - count
            print(f"{self.dial_current} - {count} = {new_num}")
        elif direction == "R":
            new_num = self.dial_current + count
            print(f"{self.dial_current} + {count} = {new_num}")
        else:
            print("error")
        return new_num

    def zero_check(self, num):
        if num == 0:
            self.zero_count += 1
            print(f"Number Ends on 0 adding to result 1")

    def run(self):
        with open("day1_input.txt", "r") as f:
            for x in f:

                # used for testing. Stops count after 200
                """self.stop += 1
                if self.stop == 200:
                    break"""

                print(f'''Starting Dial Position: {self.dial_current}
Movement: {x}''')
                direction = x[0]
                num = int(x[1:])
                current_num = self.counter(direction, num)

                if current_num == 0:
                    self.zero_count += 1
                    self.passing_count += 1
                    self.dial_current = current_num
                    print(f'''Number Ends on 0
Dial After Change: {str(self.dial_current)}
Result 1: {str(self.zero_count)}
Result 2: {str(self.passing_count)}
-------------''')
                    continue

                elif current_num < 0:
                    while current_num < 0:
                        if self.dial_current == 0 and current_num >= -99:
                            print("skip")
                            current_num = current_num + 100
                            print("looping num: ", current_num)
                            continue
                        else:
                            current_num = current_num + 100
                            print("looping num: ", current_num)
                            self.passing_count += 1
                            self.while_count += 1

                    #print(f"Left while count: {self.while_count}")

                    self.zero_check(current_num)
                    self.dial_current = current_num
                    print(f"""Number is less than 0
Number of Loops:{self.while_count}
New Num:{str(current_num)}
Dial Current: {str(self.dial_current)}
Result 1: {str(self.zero_count)}
Result 2: {str(self.passing_count)}
------------""")

                    self.while_count = 0
                    continue

                elif current_num > 99:
                    while current_num > 99:
                        current_num = current_num - 100
                        self.passing_count += 1
                        self.while_count += 1
                    #print(f"Right while count: {self.while_count}")

                    self.zero_check(current_num)
                    self.dial_current = current_num
                    print(f"""Number is greater than 99
Number of Loops:{self.while_count}
New Num:{str(current_num)}
Dial Current: {str(self.dial_current)}
Result 1: {str(self.zero_count)}
Result 2: {str(self.passing_count)}
------------""")
                    self.while_count = 0
                    continue

                else:
                    self.dial_current = current_num
                    print(f"""Number Does Not breach Threshold. 
Dial Current: {str(self.dial_current)}
Result 1: {str(self.zero_count)}
Result 2: {str(self.passing_count)}
---------""")

        print(f"Final Result 1: {self.zero_count}")
        print(f"Final Result 2: {self.passing_count}")


Day1().run()