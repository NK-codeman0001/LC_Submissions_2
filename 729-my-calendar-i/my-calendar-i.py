from sortedcontainers import SortedList


START = 0
END = 1

class MyCalendar:
    def __init__(self):
        self.booked = SortedList()


    def book(self, start: int, end: int) -> bool:
        index = self.booked.bisect_right((start, end))
        if index > 0 and start < self.booked[index-1][END]:
            # Collision with previous interval
            return False
        elif index < len(self.booked) and self.booked[index][START] < end:
            # Collision with next interval
            return False

        self.booked.add((start, end))

        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)