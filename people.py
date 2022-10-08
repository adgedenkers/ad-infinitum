from datetime import datetime


def get_timestamp():
    """Returns the current timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Data to serve with our API

PEOPLE = {
    "Adge": {
        "id": 1,
        "name": "Adge",
        "first_name": "Adriaan",
        "last_name": "Denkers",
        "middle_name": "Harold",
        "suffix": "",
        "birth_date": "1977-11-22 08:45:22-0500",
    },
    "Becky": {
        "id ": 2,
        "name": "Becky",
        "first_name": "Rebecca",
        "last_name": "Denkers",
        "middle_name": "Lydia",
        "suffix": "",
        "birth_date": "1978-08-19 14:02:22-0400",
    },
    "Fitz": {
        "id": 3,
        "name": "Fitz",
        "first_name": "Fitzgerald",
        "last_name": "Denkers",
        "middle_name": "Adriaan",
        "suffix": "",
        "birth_date": "2010-09-08 14:19:22-0400",
    },
}
# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
