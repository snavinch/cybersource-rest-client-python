# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InvoicingV2InvoiceSettingsGet200Response(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'submit_time_utc': 'str',
        'invoice_settings_information': 'InvoicingV2InvoiceSettingsGet200ResponseInvoiceSettingsInformation'
    }

    attribute_map = {
        'submit_time_utc': 'submitTimeUtc',
        'invoice_settings_information': 'invoiceSettingsInformation'
    }

    def __init__(self, submit_time_utc=None, invoice_settings_information=None):
        """
        InvoicingV2InvoiceSettingsGet200Response - a model defined in Swagger
        """

        self._submit_time_utc = None
        self._invoice_settings_information = None

        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if invoice_settings_information is not None:
          self.invoice_settings_information = invoice_settings_information

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this InvoicingV2InvoiceSettingsGet200Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by authorization service. 

        :return: The submit_time_utc of this InvoicingV2InvoiceSettingsGet200Response.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this InvoicingV2InvoiceSettingsGet200Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by authorization service. 

        :param submit_time_utc: The submit_time_utc of this InvoicingV2InvoiceSettingsGet200Response.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def invoice_settings_information(self):
        """
        Gets the invoice_settings_information of this InvoicingV2InvoiceSettingsGet200Response.

        :return: The invoice_settings_information of this InvoicingV2InvoiceSettingsGet200Response.
        :rtype: InvoicingV2InvoiceSettingsGet200ResponseInvoiceSettingsInformation
        """
        return self._invoice_settings_information

    @invoice_settings_information.setter
    def invoice_settings_information(self, invoice_settings_information):
        """
        Sets the invoice_settings_information of this InvoicingV2InvoiceSettingsGet200Response.

        :param invoice_settings_information: The invoice_settings_information of this InvoicingV2InvoiceSettingsGet200Response.
        :type: InvoicingV2InvoiceSettingsGet200ResponseInvoiceSettingsInformation
        """

        self._invoice_settings_information = invoice_settings_information

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
        if not isinstance(other, InvoicingV2InvoiceSettingsGet200Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
