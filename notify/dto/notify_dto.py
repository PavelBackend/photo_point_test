from dataclasses import dataclass
from typing import Optional


@dataclass
class Recipient:
    email: Optional[str] = None
    chat_id: Optional[int] = None
    phone: Optional[str] = None
