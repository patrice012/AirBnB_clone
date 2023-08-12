from models.base_model import BaseModel

"""Place Class representation"""


class Place(BaseModel):
    """
    Place Class

    Attributes:
        city_id(str): empty string
        user_id(str): empty string
        name(str): empty string
        description(str): empty string
        number_rooms(int): 0 as default value
        number_bathrooms(int): 0 as default value
        max_guest(int): 0 as default value
        price_by_night(int): 0 as default value
        latitude(float): 0.0 as default value
        longitude(float): 0.0 as default value
        amenity_ids(list): empty list
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []
