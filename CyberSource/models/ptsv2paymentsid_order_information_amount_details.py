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


class Ptsv2paymentsidOrderInformationAmountDetails(object):
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
        'additional_amount': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'additional_amount': 'additionalAmount',
        'currency': 'currency'
    }

    def __init__(self, additional_amount=None, currency=None):
        """
        Ptsv2paymentsidOrderInformationAmountDetails - a model defined in Swagger
        """

        self._additional_amount = None
        self._currency = None

        if additional_amount is not None:
          self.additional_amount = additional_amount
        if currency is not None:
          self.currency = currency

    @property
    def additional_amount(self):
        """
        Gets the additional_amount of this Ptsv2paymentsidOrderInformationAmountDetails.
        Additional charges that have to be authorized against a lodging or auto-rental order. This value cannot be negative. You can include a decimal point (.), but no other special characters. 

        :return: The additional_amount of this Ptsv2paymentsidOrderInformationAmountDetails.
        :rtype: str
        """
        return self._additional_amount

    @additional_amount.setter
    def additional_amount(self, additional_amount):
        """
        Sets the additional_amount of this Ptsv2paymentsidOrderInformationAmountDetails.
        Additional charges that have to be authorized against a lodging or auto-rental order. This value cannot be negative. You can include a decimal point (.), but no other special characters. 

        :param additional_amount: The additional_amount of this Ptsv2paymentsidOrderInformationAmountDetails.
        :type: str
        """
        if additional_amount is not None and len(additional_amount) > 19:
            raise ValueError("Invalid value for `additional_amount`, length must be less than or equal to `19`")

        self._additional_amount = additional_amount

    @property
    def currency(self):
        """
        Gets the currency of this Ptsv2paymentsidOrderInformationAmountDetails.
        Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  #### Used by **Authorization** Required field.  **Authorization Reversal** For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### GPX This field is optional for reversing an authorization or credit.  #### DCC for First Data Your local currency. 

        :return: The currency of this Ptsv2paymentsidOrderInformationAmountDetails.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Ptsv2paymentsidOrderInformationAmountDetails.
        Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  #### Used by **Authorization** Required field.  **Authorization Reversal** For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### GPX This field is optional for reversing an authorization or credit.  #### DCC for First Data Your local currency. 

        :param currency: The currency of this Ptsv2paymentsidOrderInformationAmountDetails.
        :type: str
        """
        if currency is not None and len(currency) > 3:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")

        self._currency = currency

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
        if not isinstance(other, Ptsv2paymentsidOrderInformationAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
