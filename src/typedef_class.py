from dataclasses import dataclass
from base_class import Base
from typedef_print_class import TypedefPrinting


@dataclass
class Typedef(Base):
    def __find_element(self, filename: str):
        pass

    def __find_typedef_declared(self, string: str) -> int:
        pass

    def __find_typedef_target(self, string: str) -> str:
        pass

    def print_typedef(self, filename: str) -> list:
        pass
