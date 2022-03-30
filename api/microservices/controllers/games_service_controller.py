import connexion
import six

from swagger_server.models.games_item import GamesItem  # noqa: E501
from swagger_server.models.reviews_item import ReviewsItem  # noqa: E501
from swagger_server import util


def create_game(GamesItem=None):  # noqa: E501
    """Creates a new game on the list

    Creates a new game # noqa: E501

    :param GamesItem: Game to create
    :type GamesItem: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        GamesItem = GamesItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_game(id):  # noqa: E501
    """Delete a game by it´s id

    Deletes a game from the dataset # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def get_searched_game(id):  # noqa: E501
    """Search for a game

    The user gets the game he searched # noqa: E501

    :param id: 
    :type id: int

    :rtype: List[GamesItem]
    """
    return 'do some magic!'


def set_recommend_true(id, ReviewsItem=None):  # noqa: E501
    """Recommend a game

    Recommend the game based on the review status # noqa: E501

    :param id: 
    :type id: int
    :param ReviewsItem: Set recommended to true or false
    :type ReviewsItem: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ReviewsItem = ReviewsItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
