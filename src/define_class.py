from base_class import Base
from dataclasses import dataclass
from define_print_class import DefinePrinting


@dataclass
class Define(Base):
    def __find_element(self, filename: str):
        pass

    def __find_define_value(self, string: str) -> int:
        pass

    def __find_define_name(self, string: str) -> str:
        pass

    def print_define(self, filename: str) -> list:
        pass
