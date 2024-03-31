class QueueOutOfRangeException(Exception):
    def __init__(self, message="Queue Out Of Range Error"):
        self.message = message
        super().__init__(self.message)