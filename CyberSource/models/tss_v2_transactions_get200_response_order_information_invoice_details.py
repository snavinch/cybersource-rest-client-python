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


class TssV2TransactionsGet200ResponseOrderInformationInvoiceDetails(object):
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
        'sales_slip_number': 'int'
    }

    attribute_map = {
        'sales_slip_number': 'salesSlipNumber'
    }

    def __init__(self, sales_slip_number=None):
        """
        TssV2TransactionsGet200ResponseOrderInformationInvoiceDetails - a model defined in Swagger
        """

        self._sales_slip_number = None

        if sales_slip_number is not None:
          self.sales_slip_number = sales_slip_number

    @property
    def sales_slip_number(self):
        """
        Gets the sales_slip_number of this TssV2TransactionsGet200ResponseOrderInformationInvoiceDetails.
        Transaction identifier that is generated. You have the option of printing the sales slip number on the receipt. This field is supported only on Cybersource through Visanet and JCN gateway.  Optional field.  #### Card Present processing message If you included this field in the request, the returned value is the value that you sent in the request. If you did not include this field in the request, the system generated this value for you.  The difference between this reply field and the `processorInformation.systemTraceAuditNumber` field is that the system generates the system trace audit number (STAN), and you must print the receipt number on the receipt; whereas you can generate the sales slip number, and you can choose to print the sales slip number on the receipt. 

        :return: The sales_slip_number of this TssV2TransactionsGet200ResponseOrderInformationInvoiceDetails.
        :rtype: int
        """
        return self._sales_slip_number

    @sales_slip_number.setter
    def sales_slip_number(self, sales_slip_number):
        """
        Sets the sales_slip_number of this TssV2TransactionsGet200ResponseOrderInformationInvoiceDetails.
        Transaction identifier that is generated. You have the option of printing the sales slip number on the receipt. This field is supported only on Cybersource through Visanet and JCN gateway.  Optional field.  #### Card Present processing message If you included this field in the request, the returned value is the value that you sent in the request. If you did not include this field in the request, the system generated this value for you.  The difference between this reply field and the `processorInformation.systemTraceAuditNumber` field is that the system generates the system trace audit number (STAN), and you must print the receipt number on the receipt; whereas you can generate the sales slip number, and you can choose to print the sales slip number on the receipt. 

        :param sales_slip_number: The sales_slip_number of this TssV2TransactionsGet200ResponseOrderInformationInvoiceDetails.
        :type: int
        """
        if sales_slip_number is not None and sales_slip_number > 99999:
            raise ValueError("Invalid value for `sales_slip_number`, must be a value less than or equal to `99999`")

        self._sales_slip_number = sales_slip_number

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
        if not isinstance(other, TssV2TransactionsGet200ResponseOrderInformationInvoiceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
