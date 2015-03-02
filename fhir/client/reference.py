__author__ = 'john'


class Reference():
    def __init__(self):
        self.reference_value = []
        self.display_value = []

    @property
    def reference(self):
        return self.reference_value

    @reference.setter
    def reference(self, reference):
        self.reference_value = reference


    @property
    def display(self):
        return self.display_value

    @display.setter
    def reference(self, display):
        self.display_value = display
