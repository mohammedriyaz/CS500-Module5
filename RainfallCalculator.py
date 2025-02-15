class RainFallCalculator():
    """
    This class calculates the total rainfall for given number of years and average rainfall per month.
    """
    def __init__(self): # constructor
        self.noy = 0
        self.rf_by_year = {}
        self.total_mobths = 0
        self.total_rf = 0
        self.avarage_rf = 0
        self.get_user_input()
        self.calculate()
        self.display()
        
    def get_monthly_rainfall(self, year):
        """
        This method will get the rainfall data for each month of the given year.

        Args:
            year (int): the year for which rainfall data needs to be collected.
        """
        rf_list = []
        for m in range(12):
            rainfall = int(input(f"Enter the rainfall in inches for {m+1} month of {year}: "))
            rf_list.append(rainfall)
            # calculate the total rainfall and total months
            self.total_rf += rainfall
            self.total_mobths += 1
        self.rf_by_year[year] = rf_list

    def get_user_input(self):
        """
        This method will get the number of years and the list of years for which rainfall data need to be collected.
        """
        self.noy = int(input("Enter the number of years to collect rainfall data: "))
        for y in range(self.noy):
            year = input("Enter the year: ")
            self.get_monthly_rainfall(year)
        
    def calculate(self):
        """
        This method will calculate the average rainfall per month.
        """
        if self.total_mobths > 0:
            self.avarage_rf = self.total_rf / self.total_mobths
            
    def display(self):
        """
        This method will display the total months, total rainfall and average rainfall per month.
        """
        print()
        print("Rainfall data".center(100, "="))
        print(f"Total months: {self.total_mobths}")
        print(f"Total rainfall for given {self.noy} year(s): {self.total_rf} inches")
        print(f"Average rainfall per month: {self.avarage_rf:.2f} inches\n")
        
# Main
rfc = RainFallCalculator()
