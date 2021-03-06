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

from flat_api.models.score_revision_statistics import ScoreRevisionStatistics  # noqa: F401,E501


class ScoreRevision(object):
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
        'id': 'str',
        'user': 'str',
        'collaborators': 'list[str]',
        'creation_date': 'datetime',
        'description': 'str',
        'autosave': 'bool',
        'statistics': 'ScoreRevisionStatistics'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'collaborators': 'collaborators',
        'creation_date': 'creationDate',
        'description': 'description',
        'autosave': 'autosave',
        'statistics': 'statistics'
    }

    def __init__(self, id=None, user=None, collaborators=None, creation_date=None, description=None, autosave=None, statistics=None):  # noqa: E501
        """ScoreRevision - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._user = None
        self._collaborators = None
        self._creation_date = None
        self._description = None
        self._autosave = None
        self._statistics = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if collaborators is not None:
            self.collaborators = collaborators
        if creation_date is not None:
            self.creation_date = creation_date
        if description is not None:
            self.description = description
        if autosave is not None:
            self.autosave = autosave
        if statistics is not None:
            self.statistics = statistics

    @property
    def id(self):
        """Gets the id of this ScoreRevision.  # noqa: E501

        The unique identifier of the revision.  # noqa: E501

        :return: The id of this ScoreRevision.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScoreRevision.

        The unique identifier of the revision.  # noqa: E501

        :param id: The id of this ScoreRevision.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user(self):
        """Gets the user of this ScoreRevision.  # noqa: E501

        The user identifier who created the revision  # noqa: E501

        :return: The user of this ScoreRevision.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ScoreRevision.

        The user identifier who created the revision  # noqa: E501

        :param user: The user of this ScoreRevision.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def collaborators(self):
        """Gets the collaborators of this ScoreRevision.  # noqa: E501


        :return: The collaborators of this ScoreRevision.  # noqa: E501
        :rtype: list[str]
        """
        return self._collaborators

    @collaborators.setter
    def collaborators(self, collaborators):
        """Sets the collaborators of this ScoreRevision.


        :param collaborators: The collaborators of this ScoreRevision.  # noqa: E501
        :type: list[str]
        """

        self._collaborators = collaborators

    @property
    def creation_date(self):
        """Gets the creation_date of this ScoreRevision.  # noqa: E501

        The date when this revision was created  # noqa: E501

        :return: The creation_date of this ScoreRevision.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ScoreRevision.

        The date when this revision was created  # noqa: E501

        :param creation_date: The creation_date of this ScoreRevision.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def description(self):
        """Gets the description of this ScoreRevision.  # noqa: E501

        A description associated to the revision  # noqa: E501

        :return: The description of this ScoreRevision.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScoreRevision.

        A description associated to the revision  # noqa: E501

        :param description: The description of this ScoreRevision.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def autosave(self):
        """Gets the autosave of this ScoreRevision.  # noqa: E501

        True if this revision was automatically generated by Flat and not on purpose by the user.   # noqa: E501

        :return: The autosave of this ScoreRevision.  # noqa: E501
        :rtype: bool
        """
        return self._autosave

    @autosave.setter
    def autosave(self, autosave):
        """Sets the autosave of this ScoreRevision.

        True if this revision was automatically generated by Flat and not on purpose by the user.   # noqa: E501

        :param autosave: The autosave of this ScoreRevision.  # noqa: E501
        :type: bool
        """

        self._autosave = autosave

    @property
    def statistics(self):
        """Gets the statistics of this ScoreRevision.  # noqa: E501


        :return: The statistics of this ScoreRevision.  # noqa: E501
        :rtype: ScoreRevisionStatistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this ScoreRevision.


        :param statistics: The statistics of this ScoreRevision.  # noqa: E501
        :type: ScoreRevisionStatistics
        """

        self._statistics = statistics

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
        if not isinstance(other, ScoreRevision):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
