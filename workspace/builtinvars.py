import os
import random
import string
from pseudoapi.settings import BASE_DIR

class BuiltinVars:
    
    def randomLetter(self) -> str:
        return random.choices(string.ascii_lowercase)

    def randomInt(self) -> int:
        return random.randint(0, 10)

    @property
    def variables(self) -> dict:
        result = dict(
            random_int=self.randomInt(),
            random_letter=self.randomLetter
        )
        return result