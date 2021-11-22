from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class Customer(BaseModel):
    name: str
    representative: str
    contract_start: Optional[date] = None
    Branches: Optional[List[str]] = None
    Country: str


class UpdateCustomer(BaseModel):
    name: Optional[str] = None
    representative: Optional[str] = None
    contract_start: Optional[date] = None
    Branches: Optional[List[str]] = None
    Country: Optional[str] = None
