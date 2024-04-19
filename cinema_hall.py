# 1
class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


# 2
class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = [] 
        self.__rows = rows
        self.__cols = cols 
        self.__hall_no = hall_no 
        Star_Cinema().entry_hall(self) 


    # 3
    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        seat_map = []
        for _ in range(self.__rows):
            seat_map.append([0] * self.__cols)
        self.__seats[id] = seat_map


    # 4 & 8
    def book_seats(self, id, seat_list):
        if id in self.__seats:
            for seat in seat_list:
                row, col = seat
                if 1 <= row <= self.__rows and 1 <= col <= self.__cols:
                    if self.__seats[id][row - 1][col - 1] == 0:
                        self.__seats[id][row - 1][col - 1] = 1
                        print(f"Seat {row}-{col} booked successfully.")
                    else:
                        print(f"Seat ({row},{col}) is already booked.\n\n")
                else:
                    print(f"Seat ({row},{col}) is out of range.\n\n")
        else:
            print(f"Show with id {id} not found.\n\n")


    # 5
    def view_show_list(self):
        print("\nShows running in this hall:")
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
        print("\n\n")


    # 6
    def view_available_seats(self, id):
        if id in self.__seats:
            print(f"\nAvailable seats for show ID {id}:")
            for i in range(self.__rows):
                for j in range(self.__cols):
                    if self.__seats[id][i][j] == 0:
                        print(f"Seat ({i+1},{j+1})")
            for i in range(self.__rows):
                for j in range(self.__cols):
                    print(f"{self.__seats[id][i][j]}", end=" ")
                print()
        else:
            print(f"Show with id {id} not found.")
        print("\n\n")

cineplex = Hall(5, 5, 1) 
cineplex.entry_show('111', 'Rolex', '19/04/2024 1:00 PM')
cineplex.entry_show('222', 'Salar', '19/04/2024 5:00 PM')

# cineplex.book_seats('111', [(1, 1), (2, 2)])
# cineplex.book_seats('222', [(3, 3), (4, 4)])


# 7
while True:
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK SEATS")
    print("4. EXIT")
    choice = int(input("ENTER OPTION: "))
    if choice == 1:
        cineplex.view_show_list()
    elif choice == 2:
        show_id = input("Enter show ID: ")
        cineplex.view_available_seats(show_id)
    elif choice == 3:
        show_id = input("Enter show ID: ")
        seats_row = int(input("Enter seat Row: "))
        seats_col = int(input("Enter seat Col: "))
        seats = [(seats_row, seats_col)]
        cineplex.book_seats(show_id, seats)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Try again.")
