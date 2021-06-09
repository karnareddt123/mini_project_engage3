from abc import ABC
from abc import abstractmethod


class AbstractEndpoint(ABC):
    """
    Abstract producer for all messaging clients.
    """

    @abstractmethod
    def download_json(self,  **kwargs):
        """ send the message."""
