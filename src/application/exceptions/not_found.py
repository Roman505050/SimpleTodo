class TodoNotFound(Exception):
    def __init__(self, message: str = "Todo not found"):
        super().__init__(message)
