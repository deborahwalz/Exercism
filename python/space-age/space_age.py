class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
    
    def on_earth(self):
        return self.age(1)

    def on_mercury(self):
        return self.age(0.2408467)

    def on_venus(self):
        return self.age(0.61519726)

    def on_mars(self):
        return self.age(1.8808158)

    def on_jupiter(self):
        return self.age(11.862615)

    def on_saturn(self):
        return self.age(29.447498)

    def on_uranus(self):
        return self.age(84.016846)

    def on_neptune(self):
        return self.age(164.79132)

    def age(self, ratio):
        return round(self.seconds / (ratio * 31557600), 2)