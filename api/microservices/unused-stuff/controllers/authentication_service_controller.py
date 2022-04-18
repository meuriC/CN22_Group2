import connexion
import six

from swagger_server.models.token_item import TokenItem  # noqa: E501
from swagger_server.models.user_auth_item import UserAuthItem  # noqa: E501
from swagger_server import util


def user_delete_account(UserItem=None):  # noqa: E501
    """Deletes account

    Deletes the account of the user from the authentication service # noqa: E501

    :param UserItem: User to delete
    :type UserItem: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        UserItem = UserAuthItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_log_out(UserItem=None):  # noqa: E501
    """Log out

    The user logs out of his account # noqa: E501

    :param UserItem: User to create
    :type UserItem: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        UserItem = TokenItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_login(UserItem=None):  # noqa: E501
    """User logs in

    User logs in # noqa: E501

    :param UserItem: User to create
    :type UserItem: dict | bytes

    :rtype: TokenItem
    """
    if connexion.request.is_json:
        UserItem = UserAuthItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_register(UserItem=None):  # noqa: E501
    """Register a new User

    User sign up # noqa: E501

    :param UserItem: User to create
    :type UserItem: dict | bytes

    :rtype: UserAuthItem
    """
    if connexion.request.is_json:
        UserItem = UserAuthItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
