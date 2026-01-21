import uuid

from datetime import datetime

class Payment:

    def __init__(self, amount: float, actor, target, note: str):
        self.id = str(uuid.uuid4())
        self.amount = float(amount)
        self.actor = actor
        self.target = target
        self.note = note
        self.date = datetime.now()