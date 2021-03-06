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

from flat_api.models.google_classroom_submission import GoogleClassroomSubmission  # noqa: F401,E501
from flat_api.models.media_attachment import MediaAttachment  # noqa: F401,E501


class AssignmentSubmission(object):
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
        'classroom': 'str',
        'assignment': 'str',
        'creator': 'str',
        'creation_date': 'str',
        'attachments': 'list[MediaAttachment]',
        'submission_date': 'str',
        'student_comment': 'str',
        'return_date': 'str',
        'return_feedback': 'str',
        'return_creator': 'str',
        'google_classroom': 'GoogleClassroomSubmission'
    }

    attribute_map = {
        'id': 'id',
        'classroom': 'classroom',
        'assignment': 'assignment',
        'creator': 'creator',
        'creation_date': 'creationDate',
        'attachments': 'attachments',
        'submission_date': 'submissionDate',
        'student_comment': 'studentComment',
        'return_date': 'returnDate',
        'return_feedback': 'returnFeedback',
        'return_creator': 'returnCreator',
        'google_classroom': 'googleClassroom'
    }

    def __init__(self, id=None, classroom=None, assignment=None, creator=None, creation_date=None, attachments=None, submission_date=None, student_comment=None, return_date=None, return_feedback=None, return_creator=None, google_classroom=None):  # noqa: E501
        """AssignmentSubmission - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._classroom = None
        self._assignment = None
        self._creator = None
        self._creation_date = None
        self._attachments = None
        self._submission_date = None
        self._student_comment = None
        self._return_date = None
        self._return_feedback = None
        self._return_creator = None
        self._google_classroom = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if classroom is not None:
            self.classroom = classroom
        if assignment is not None:
            self.assignment = assignment
        if creator is not None:
            self.creator = creator
        if creation_date is not None:
            self.creation_date = creation_date
        if attachments is not None:
            self.attachments = attachments
        if submission_date is not None:
            self.submission_date = submission_date
        if student_comment is not None:
            self.student_comment = student_comment
        if return_date is not None:
            self.return_date = return_date
        if return_feedback is not None:
            self.return_feedback = return_feedback
        if return_creator is not None:
            self.return_creator = return_creator
        if google_classroom is not None:
            self.google_classroom = google_classroom

    @property
    def id(self):
        """Gets the id of this AssignmentSubmission.  # noqa: E501

        Unique identifier of the submission  # noqa: E501

        :return: The id of this AssignmentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssignmentSubmission.

        Unique identifier of the submission  # noqa: E501

        :param id: The id of this AssignmentSubmission.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def classroom(self):
        """Gets the classroom of this AssignmentSubmission.  # noqa: E501

        Unique identifier of the classroom where the assignment was posted   # noqa: E501

        :return: The classroom of this AssignmentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._classroom

    @classroom.setter
    def classroom(self, classroom):
        """Sets the classroom of this AssignmentSubmission.

        Unique identifier of the classroom where the assignment was posted   # noqa: E501

        :param classroom: The classroom of this AssignmentSubmission.  # noqa: E501
        :type: str
        """

        self._classroom = classroom

    @property
    def assignment(self):
        """Gets the assignment of this AssignmentSubmission.  # noqa: E501

        Unique identifier of the assignment  # noqa: E501

        :return: The assignment of this AssignmentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._assignment

    @assignment.setter
    def assignment(self, assignment):
        """Sets the assignment of this AssignmentSubmission.

        Unique identifier of the assignment  # noqa: E501

        :param assignment: The assignment of this AssignmentSubmission.  # noqa: E501
        :type: str
        """

        self._assignment = assignment

    @property
    def creator(self):
        """Gets the creator of this AssignmentSubmission.  # noqa: E501

        The User identifier of the student who created the submission  # noqa: E501

        :return: The creator of this AssignmentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this AssignmentSubmission.

        The User identifier of the student who created the submission  # noqa: E501

        :param creator: The creator of this AssignmentSubmission.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def creation_date(self):
        """Gets the creation_date of this AssignmentSubmission.  # noqa: E501

        The date when the submission was created  # noqa: E501

        :return: The creation_date of this AssignmentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this AssignmentSubmission.

        The date when the submission was created  # noqa: E501

        :param creation_date: The creation_date of this AssignmentSubmission.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

    @property
    def attachments(self):
        """Gets the attachments of this AssignmentSubmission.  # noqa: E501


        :return: The attachments of this AssignmentSubmission.  # noqa: E501
        :rtype: list[MediaAttachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this AssignmentSubmission.


        :param attachments: The attachments of this AssignmentSubmission.  # noqa: E501
        :type: list[MediaAttachment]
        """

        self._attachments = attachments

    @property
    def submission_date(self):
        """Gets the submission_date of this AssignmentSubmission.  # noqa: E501

        The date when the student submitted his work  # noqa: E501

        :return: The submission_date of this AssignmentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._submission_date

    @submission_date.setter
    def submission_date(self, submission_date):
        """Sets the submission_date of this AssignmentSubmission.

        The date when the student submitted his work  # noqa: E501

        :param submission_date: The submission_date of this AssignmentSubmission.  # noqa: E501
        :type: str
        """

        self._submission_date = submission_date

    @property
    def student_comment(self):
        """Gets the student_comment of this AssignmentSubmission.  # noqa: E501

        An optionnal comment sent by the student when submitting his work   # noqa: E501

        :return: The student_comment of this AssignmentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._student_comment

    @student_comment.setter
    def student_comment(self, student_comment):
        """Sets the student_comment of this AssignmentSubmission.

        An optionnal comment sent by the student when submitting his work   # noqa: E501

        :param student_comment: The student_comment of this AssignmentSubmission.  # noqa: E501
        :type: str
        """

        self._student_comment = student_comment

    @property
    def return_date(self):
        """Gets the return_date of this AssignmentSubmission.  # noqa: E501

        The date when the teacher returned the work  # noqa: E501

        :return: The return_date of this AssignmentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._return_date

    @return_date.setter
    def return_date(self, return_date):
        """Sets the return_date of this AssignmentSubmission.

        The date when the teacher returned the work  # noqa: E501

        :param return_date: The return_date of this AssignmentSubmission.  # noqa: E501
        :type: str
        """

        self._return_date = return_date

    @property
    def return_feedback(self):
        """Gets the return_feedback of this AssignmentSubmission.  # noqa: E501

        The feedback associated with the return  # noqa: E501

        :return: The return_feedback of this AssignmentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._return_feedback

    @return_feedback.setter
    def return_feedback(self, return_feedback):
        """Sets the return_feedback of this AssignmentSubmission.

        The feedback associated with the return  # noqa: E501

        :param return_feedback: The return_feedback of this AssignmentSubmission.  # noqa: E501
        :type: str
        """

        self._return_feedback = return_feedback

    @property
    def return_creator(self):
        """Gets the return_creator of this AssignmentSubmission.  # noqa: E501

        The User unique identifier of the teacher who returned the submission   # noqa: E501

        :return: The return_creator of this AssignmentSubmission.  # noqa: E501
        :rtype: str
        """
        return self._return_creator

    @return_creator.setter
    def return_creator(self, return_creator):
        """Sets the return_creator of this AssignmentSubmission.

        The User unique identifier of the teacher who returned the submission   # noqa: E501

        :param return_creator: The return_creator of this AssignmentSubmission.  # noqa: E501
        :type: str
        """

        self._return_creator = return_creator

    @property
    def google_classroom(self):
        """Gets the google_classroom of this AssignmentSubmission.  # noqa: E501


        :return: The google_classroom of this AssignmentSubmission.  # noqa: E501
        :rtype: GoogleClassroomSubmission
        """
        return self._google_classroom

    @google_classroom.setter
    def google_classroom(self, google_classroom):
        """Sets the google_classroom of this AssignmentSubmission.


        :param google_classroom: The google_classroom of this AssignmentSubmission.  # noqa: E501
        :type: GoogleClassroomSubmission
        """

        self._google_classroom = google_classroom

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
        if not isinstance(other, AssignmentSubmission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
