from models.base_model import BaseModel

"""Review Class representation"""


class Review(BaseModel):
    """
    Review Class

    Attribute:
        place_id(str): empty string
        user_id(str): empty string
        text(str): empty string
    """

    place_id = ""
    user_id = ""
    text = ""
