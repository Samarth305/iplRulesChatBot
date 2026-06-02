from abc import ABC, abstractmethod
from typing import List, Dict


class BaseResponseGenerator(ABC):

    @abstractmethod
    def generate_response(self, query: str, context: List[str], history: List[Dict] = None) -> str:
        pass
