# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML or MIDI files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and interoduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html)   # noqa: E501

    OpenAPI spec version: 2.6.0
    Contact: developers@flat.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ScoreCommentsCounts(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'total': 'float',
        'unique': 'float',
        'weekly': 'float',
        'monthly': 'float'
    }

    attribute_map = {
        'total': 'total',
        'unique': 'unique',
        'weekly': 'weekly',
        'monthly': 'monthly'
    }

    def __init__(self, total=None, unique=None, weekly=None, monthly=None):  # noqa: E501
        """ScoreCommentsCounts - a model defined in Swagger"""  # noqa: E501

        self._total = None
        self._unique = None
        self._weekly = None
        self._monthly = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if unique is not None:
            self.unique = unique
        if weekly is not None:
            self.weekly = weekly
        if monthly is not None:
            self.monthly = monthly

    @property
    def total(self):
        """Gets the total of this ScoreCommentsCounts.  # noqa: E501

        The total number of comments added on the score  # noqa: E501

        :return: The total of this ScoreCommentsCounts.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ScoreCommentsCounts.

        The total number of comments added on the score  # noqa: E501

        :param total: The total of this ScoreCommentsCounts.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def unique(self):
        """Gets the unique of this ScoreCommentsCounts.  # noqa: E501

        The unique (1/user) number of comments added on the score  # noqa: E501

        :return: The unique of this ScoreCommentsCounts.  # noqa: E501
        :rtype: float
        """
        return self._unique

    @unique.setter
    def unique(self, unique):
        """Sets the unique of this ScoreCommentsCounts.

        The unique (1/user) number of comments added on the score  # noqa: E501

        :param unique: The unique of this ScoreCommentsCounts.  # noqa: E501
        :type: float
        """

        self._unique = unique

    @property
    def weekly(self):
        """Gets the weekly of this ScoreCommentsCounts.  # noqa: E501

        The weekly unique number of comments added on the score  # noqa: E501

        :return: The weekly of this ScoreCommentsCounts.  # noqa: E501
        :rtype: float
        """
        return self._weekly

    @weekly.setter
    def weekly(self, weekly):
        """Sets the weekly of this ScoreCommentsCounts.

        The weekly unique number of comments added on the score  # noqa: E501

        :param weekly: The weekly of this ScoreCommentsCounts.  # noqa: E501
        :type: float
        """

        self._weekly = weekly

    @property
    def monthly(self):
        """Gets the monthly of this ScoreCommentsCounts.  # noqa: E501

        The monthly unique number of comments added on the score  # noqa: E501

        :return: The monthly of this ScoreCommentsCounts.  # noqa: E501
        :rtype: float
        """
        return self._monthly

    @monthly.setter
    def monthly(self, monthly):
        """Sets the monthly of this ScoreCommentsCounts.

        The monthly unique number of comments added on the score  # noqa: E501

        :param monthly: The monthly of this ScoreCommentsCounts.  # noqa: E501
        :type: float
        """

        self._monthly = monthly

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScoreCommentsCounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
