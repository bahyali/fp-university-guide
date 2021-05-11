import types
from flask_seeder.generator import Generator


class FakerIntegration(Generator):
    def __init__(self, func):
        super().__init__()
        self.func = func

    def generate(self):
        return self.func()
