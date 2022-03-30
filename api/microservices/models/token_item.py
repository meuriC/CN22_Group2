# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
import util


class TokenItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, token: str=None):  # noqa: E501
        """TokenItem - a model defined in Swagger

        :param token: The token of this TokenItem.  # noqa: E501
        :type token: str
        """
        self.swagger_types = {
            'token': str
        }

        self.attribute_map = {
            'token': 'token'
        }

        self._token = token

    @classmethod
    def from_dict(cls, dikt) -> 'TokenItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TokenItem of this TokenItem.  # noqa: E501
        :rtype: TokenItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this TokenItem.


        :return: The token of this TokenItem.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this TokenItem.


        :param token: The token of this TokenItem.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token
