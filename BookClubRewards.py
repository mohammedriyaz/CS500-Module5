class BookClubRewards():
    
    def __init__(self): # constructor
        self.books_purchased = 0
        self.get_user_input()
        self.emit_output()
        
    def get_user_input(self):
        self.books_purchased = int(input("\nEnter the number of books purchased: "))
        
    def calc_reward_points(self, book_count):
        """ 0 5 15 30 60 120 240 480
        reward pints for book count is like a sequence of 0, 5, 15, 30, 60, 120, 240, 480
        It emans , up to 1 book, student won't get any reward points, for 2 books, student will get 5 reward points, for 3 books, student will get 15 reward pointsand so on.
        This function will calculate the reward points for the given book count
        """
        # get lower two factors of book_count, ex if book_count is 5, then 4 and if book_count is 6, then 6. if book_count is 1, then 0
        if book_count < 2:
            count_by_2s = 0
        else:
            count_by_2s = (book_count - (book_count % 2)) if book_count % 2 != 0 else book_count
        # memoize the result to optimize the performance or reduce the time complexity
        self.cache = {}
        #  base cases
        if (count_by_2s <= 0):
            return 0
        elif (count_by_2s == 2):
            return 5
        elif (count_by_2s == 4):
            return 15
        else:
            if count_by_2s in self.cache:
                return self.cache[count_by_2s]
            last_reward = self.calc_reward_points(count_by_2s - 2)
            if last_reward == 15: # in this sequence 15 is the only number is not following the pattern, so we need to handle it separately
                return last_reward * 2
            return last_reward + ((last_reward - self.calc_reward_points(count_by_2s - 4)) * 2) # ex 0, 5, 15, 30, ((30 + ((30 - 15) * 2))=60)

    def emit_output(self):
        print(f"\nYou have earned {self.calc_reward_points(self.books_purchased)} Reward point(s) for purchasing {self.books_purchased} book(s)\n")
        
# Main
BookClubRewards()