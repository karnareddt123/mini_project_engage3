from abc import ABC
from abc import abstractmethod


class AbstractAwsS3(ABC):
    """
    Abstract producer for all messaging clients.
    """

    @abstractmethod
    def pre_send(self, *args, **kwargs):
        """ operations to be performed before send method call """

    @abstractmethod
    def upload(self, message, **kwargs):
        """ send the message."""

    @abstractmethod
    def post_send(self, *args, **kwargs):
        """ operations to be performed after send method call """

    @abstractmethod
    def close(self, *args, **kwargs):
        """ close the producer. if timeout is specified for the producer client pass the timeout
            option. otherwise sleep up to timeout value.
        """


