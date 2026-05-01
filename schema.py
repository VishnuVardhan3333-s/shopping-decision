from pydantic import BaseModel

class DecisionOutput(BaseModel):
    product: str
    decision: str
    reason: str
    tradeoffs: list[str]
    confidence: str