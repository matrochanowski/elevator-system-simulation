import random


class Elevator:
    def __init__(self, max_people_inside, max_possible_floor):
        self.current_floor = 0
        self.people_inside_int = 0
        self.max_people_inside = max_people_inside
        self.max_possible_floor = max_possible_floor

        self.max_requested_floor = 0
        self.min_requested_floor = max_possible_floor
        self.requested_floors = []
        self.chosen_floors = []
        self.state = "standing"
        self.people_inside_arr = []
        self.heading_to = None
        self.delay = 0

    def enter(self, people_entering_arr):
        #  kod obsługujący kto wchodzi do windy w operator1
        for person in people_entering_arr:
            self.people_inside_arr.append(person)
        self.update_people_inside()

    def leave(self, people_leaving_arr):
        for person in people_leaving_arr:
            self.people_inside_arr.remove(person)
        self.update_people_inside()

    def update_people_inside(self):
        self.people_inside_int = len(self.people_inside_arr)

    def move_elevator(self, new_requested_floor):
        if 1 <= new_requested_floor <= self.max_possible_floor:
            #  the chosen floor is correct
            if new_requested_floor > self.current_floor:
                self.move_elevator_up()
            elif new_requested_floor < self.current_floor:
                self.move_elevator_down()
            self.add_floor_to_requested_queue(new_requested_floor)
            #  in case the elevator already is on the requested floor
            self.decide_if_stop()
        else:
            #  chosen floor is incorrect
            print("Podano nieprawidłowe piętro.")

    def move_elevator_up(self):
        self.state = "going_up"

    def move_elevator_down(self):
        self.state = "going_down"

    def add_floor_to_requested_queue(self, new_floor):
        self.requested_floors.append(new_floor)

    def add_floor_to_chosen_queue(self, new_floor):
        self.chosen_floors.append(new_floor)

    def decide_if_stop(self):
        if self.current_floor in self.requested_floors:
            return True
        if self.current_floor in self.chosen_floors:
            return True
        return False

    def pop_visited_floor(self):
        self.requested_floors.remove(self.current_floor)

    def increase_floor(self):
        if self.current_floor + 1 > self.max_possible_floor:
            print("Nie można pojechać wyżej, osiągnięto najwyższe piętro.")
        else:
            self.current_floor += 1

    def decrease_floor(self):
        if self.current_floor - 1 < 0:
            print("Nie można pojechać niżej, osiągnięto najniższe piętro.")
        else:
            self.current_floor -= 1

    def how_much_space_left(self):
        return self.max_people_inside - self.people_inside_int


class Person:
    def __init__(self, max_floor, desired_floor=None, starting_floor=None):
        if starting_floor is None:
            choice = random.randint(0, 1)
            if choice == 0:
                self.starting_floor = 0
            else:
                self.starting_floor = random.randint(1, max_floor)
        else:
            self.starting_floor = starting_floor

        self.current_floor = starting_floor
        self.wait_time = 0

        if desired_floor is None:
            if self.starting_floor == 0:
                self.desired_floor = random.randint(1, max_floor)
            else:
                self.desired_floor = 0
        else:
            self.desired_floor = desired_floor

    def increase_waiting_time(self, step=1):
        self.wait_time += step