# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning) 

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProjectValidationCache(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, errors=None, project_digest=None, models_not_validated=None, stale=None):
        """
        ProjectValidationCache - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'errors': 'list[ProjectError]',
            'project_digest': 'str',
            'models_not_validated': 'list[ModelsNotValidated]',
            'stale': 'bool'
        }

        self.attribute_map = {
            'errors': 'errors',
            'project_digest': 'project_digest',
            'models_not_validated': 'models_not_validated',
            'stale': 'stale'
        }

        self._errors = errors
        self._project_digest = project_digest
        self._models_not_validated = models_not_validated
        self._stale = stale

    @property
    def errors(self):
        """
        Gets the errors of this ProjectValidationCache.
        A list of project errors

        :return: The errors of this ProjectValidationCache.
        :rtype: list[ProjectError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this ProjectValidationCache.
        A list of project errors

        :param errors: The errors of this ProjectValidationCache.
        :type: list[ProjectError]
        """

        self._errors = errors

    @property
    def project_digest(self):
        """
        Gets the project_digest of this ProjectValidationCache.
        A hash value computed from the project's current state

        :return: The project_digest of this ProjectValidationCache.
        :rtype: str
        """
        return self._project_digest

    @project_digest.setter
    def project_digest(self, project_digest):
        """
        Sets the project_digest of this ProjectValidationCache.
        A hash value computed from the project's current state

        :param project_digest: The project_digest of this ProjectValidationCache.
        :type: str
        """

        self._project_digest = project_digest

    @property
    def models_not_validated(self):
        """
        Gets the models_not_validated of this ProjectValidationCache.
        A list of models which were not fully validated

        :return: The models_not_validated of this ProjectValidationCache.
        :rtype: list[ModelsNotValidated]
        """
        return self._models_not_validated

    @models_not_validated.setter
    def models_not_validated(self, models_not_validated):
        """
        Sets the models_not_validated of this ProjectValidationCache.
        A list of models which were not fully validated

        :param models_not_validated: The models_not_validated of this ProjectValidationCache.
        :type: list[ModelsNotValidated]
        """

        self._models_not_validated = models_not_validated

    @property
    def stale(self):
        """
        Gets the stale of this ProjectValidationCache.
        If true, the cached project validation results are no longer accurate because the project has changed since the cached results were calculated

        :return: The stale of this ProjectValidationCache.
        :rtype: bool
        """
        return self._stale

    @stale.setter
    def stale(self, stale):
        """
        Sets the stale of this ProjectValidationCache.
        If true, the cached project validation results are no longer accurate because the project has changed since the cached results were calculated

        :param stale: The stale of this ProjectValidationCache.
        :type: bool
        """

        self._stale = stale

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ProjectValidationCache):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other