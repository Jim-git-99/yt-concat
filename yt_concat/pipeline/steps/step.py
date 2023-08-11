from abc import ABC, abstractmethod


class Step(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data, inputs):
        pass


class StepException(Exception):
    pass
