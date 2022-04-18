import connexion
import six

from swagger_server.models.user_item import UserItem  # noqa: E501
from swagger_server import util


def create_user(UserItem=None):  # noqa: E501
    """Creates or updates new User

    Creates a new user # noqa: E501

    :param UserItem: User to create
    :type UserItem: dict | bytes

    :rtype: UserItem
    """
    if connexion.request.is_json:
        UserItem = UserItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user_account(username):  # noqa: E501
    """Delete account

    Deletes the account of the user # noqa: E501

    :param username: 
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def get_user(username):  # noqa: E501
    """Get information about a specific user

    This call returns information about a specified username # noqa: E501

    :param username: 
    :type username: int

    :rtype: List[UserItem]
    """
    return 'do some magic!'
