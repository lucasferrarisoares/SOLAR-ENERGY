class DataModel:
    def __init__(self, date, energy_generation, temperature, performance, id=None):
        self.id = id
        self.date = date
        self.energy_generation = energy_generation
        self.temperature = temperature
        self.performance = performance

    def __repr__(self):
        return (f"DataModel(date={self.date}, energy_generation={self.energy_generation}, "
                f"temperature={self.temperature}, performance={self.performance})")
