class UiGroup:
    def __init__(self):
        self.elements = [] #create a map called elements

    def add_element(self, element): #adds element to the elements map
        self.elements.append(element)

    def set_visible(self, value): #set visible flag for each item in elements map
        for e in self.elements:
            e.set_visible(value)

    def inputs(self, events): # execute event queue for each element in elements map
        for e in self.elements:
            e.inputs(events)

    def update(self): # runs udate code of each element in elements
        for e in self.elements:
            e.update()

    def draw(self, screen): #draws each element in elements onto screen
        for e in self.elements:
            e.draw(screen)