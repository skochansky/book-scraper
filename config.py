# PSL
from dataclasses import dataclass
from string import ascii_letters, digits
from random import sample


@dataclass
class Config:
    SECRET_KEY: str = "".join(sample(ascii_letters + digits, 10))

