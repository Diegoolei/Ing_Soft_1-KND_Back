from typing import Optional
from pydantic import BaseModel, EmailStr

#users's models


#lobbies's models


#games's models


#boards's models
class Board(BaseModel):
    is_fenix: bool = false
    proclamation_promulged_fenix: int = 0
    proclamation_promulged_mortifagos: int = 0
    # 17 Cards = 17 bits for "binarie order"
    # https://www.datacamp.com/community/tutorials/python-data-type-conversion
    # 0bits a 17bits => 0 = fenix, 1 = mortifago and -1 = ¿not card?
    deck_codification: list(int) = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


#histories's models
