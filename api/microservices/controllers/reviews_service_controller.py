import connexion
import six

from swagger_server.models.reviews_item import ReviewsItem  # noqa: E501
from swagger_server import util


def create_review(ReviewsItem=None):  # noqa: E501
    """Creates a new Review

    Creates a new review # noqa: E501

    :param ReviewsItem: Review to create
    :type ReviewsItem: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ReviewsItem = ReviewsItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_review(id):  # noqa: E501
    """Delete a review by it´s id

    Deletes a review from the dataset # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def get_review_by_id(id):  # noqa: E501
    """Get review by id

    With this call you can get a specific review made in steam # noqa: E501

    :param id: 
    :type id: int

    :rtype: List[ReviewsItem]
    """
    return 'do some magic!'


def get_review_by_id_and_language(language, id):  # noqa: E501
    """Get review by id, in the defined language

    With this call you can get a specific review made in steam, in a specific language # noqa: E501

    :param language: 
    :type language: str
    :param id: 
    :type id: int

    :rtype: List[ReviewsItem]
    """
    return 'do some magic!'


def get_review_helpful():  # noqa: E501
    """Get all the helpful reviews

    With this call you can get all reviews which were marked as helpful # noqa: E501


    :rtype: List[ReviewsItem]
    """
    return 'do some magic!'


def set_review_helpful(id, ReviewsItem=None):  # noqa: E501
    """Set Review as helpful

    Sets a specific review as helpful # noqa: E501

    :param id: 
    :type id: int
    :param ReviewsItem: Review to set as Helpful
    :type ReviewsItem: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ReviewsItem = ReviewsItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_review(id, ReviewsItem=None):  # noqa: E501
    """Updates an existing review

    Updates a review existing in the dataset # noqa: E501

    :param id: 
    :type id: int
    :param ReviewsItem: Review to update
    :type ReviewsItem: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ReviewsItem = ReviewsItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_reviews(id):  # noqa: E501
    """Get all reviews from a specific user

    With this call you can get all the reviews that a specific user wrote # noqa: E501

    :param id: 
    :type id: int

    :rtype: List[ReviewsItem]
    """
    return 'do some magic!'
