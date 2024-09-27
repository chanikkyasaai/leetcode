class MyCalendarTwo:

    def __init__(self):
        self.bookings = []  # List to track all bookings
        self.overlaps = []  # List to track double overlaps
    
    def book(self, start: int, end: int) -> bool:
        # Check if the new booking causes a triple overlap
        for overlap_start, overlap_end in self.overlaps:
            if max(start, overlap_start) < min(end, overlap_end):  # If it overlaps with any double booking
                return False
        
        # Check if the new booking overlaps with any existing booking
        for book_start, book_end in self.bookings:
            if max(start, book_start) < min(end, book_end):  # If it overlaps
                overlap_start = max(start, book_start)  # Find the overlap range
                overlap_end = min(end, book_end)
                self.overlaps.append([overlap_start, overlap_end])  # Store the overlap
        
        # If no triple overlap, add this new booking
        self.bookings.append([start, end])
        
        return True




# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)