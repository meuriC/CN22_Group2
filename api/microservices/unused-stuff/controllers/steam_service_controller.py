import connexion
import six

from models.games_item import GamesItem  # noqa: E501
from models.user_item import UserItem  # noqa: E501
import util


def get_active_users():  # noqa: E501
    """Get most active users

    Get the top 10 most active users # noqa: E501


    :rtype: List[UserItem]
    """
    return 'do some magic!'


def get_recommended_games():  # noqa: E501
    """Get recommended games

    Get the games that were more recommended by the users # noqa: E501


    :rtype: List[GamesItem]
    """
    return 'do some magic!'


def get_recommended_games_amount(amount):  # noqa: E501
    """Get a specific number of recommended games

    Get the games that were more recommended by the users # noqa: E501

    :param amount: 
    :type amount: int

    :rtype: List[GamesItem]
    """
    return 'do some magic!'
