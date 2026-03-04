class Area:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits


    def describe(self):
        print(f"You are in {self.name}.")
        print(self.description)
        print("directions", ", ".join(self.exits.keys()))

areas = {
    "Bedroom": "Bedroom",
    "Hallway": "Hallway",
    "Bathroom": "Bathroom",

}

'''
class Game:
    def __init__(self):
        self.areas = {}
        self.current_area = None
        self.running = True


    def add_area(self, area):
        self.areas[area.name] = area


    def set_start(self, area_name):
        if area_name in self.areas:
            self.current_area = self.areas[area_name]
        else:
            raise ValueError(f"area '{area_name}' not isnt real")


    def move(self, direction):
        if direction in self.current_area.exits:
            next_area_name = self.current_area.exits[direction]
            self.current_area = self.areas[next_area_name]
        else:
            print("you cant go there")


    def run(self):
        print("test run 3")
        while self.running:
            self.current_area.describe()
            command = input("where would you like to go? ").strip().lower()


            if command in ["quit", "exit"]:
                print("bye")
                self.running = False
            elif command in self.areas:
                if command == self.current_area:
                    print("You're already there")
                else:
                    self.move(command)
            else:
                print("invaild command try agsin")


game = Game()


game.add_area(Area(
    "Bedroom",
    "It’s your bedroom. You should really tidy up more.",
    {"north": "Hallway"}
))


game.add_area(Area(
    "Hallway",
    "A small hallway",
    {"south": "Bedroom", "east": "Bathroom"}
))


game.add_area(Area(
    "Bathroom",
    "It’s cleaner then the rest of your house.",
    {"west": "Hallway"}
))


game.set_start("Bedroom")


if __name__ == "__main__":
    try:
        game.run()
    except KeyboardInterrupt:
        print("You quit the game.")
'''