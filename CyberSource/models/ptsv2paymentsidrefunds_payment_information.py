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


class Ptsv2paymentsidrefundsPaymentInformation(object):
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
        'card': 'Ptsv2paymentsidrefundsPaymentInformationCard',
        'bank': 'Ptsv2paymentsPaymentInformationBank',
        'tokenized_card': 'Ptsv2paymentsPaymentInformationTokenizedCard',
        'fluid_data': 'Ptsv2paymentsPaymentInformationFluidData',
        'customer': 'Ptsv2paymentsPaymentInformationCustomer',
        'payment_type': 'Ptsv2paymentsPaymentInformationPaymentType'
    }

    attribute_map = {
        'card': 'card',
        'bank': 'bank',
        'tokenized_card': 'tokenizedCard',
        'fluid_data': 'fluidData',
        'customer': 'customer',
        'payment_type': 'paymentType'
    }

    def __init__(self, card=None, bank=None, tokenized_card=None, fluid_data=None, customer=None, payment_type=None):
        """
        Ptsv2paymentsidrefundsPaymentInformation - a model defined in Swagger
        """

        self._card = None
        self._bank = None
        self._tokenized_card = None
        self._fluid_data = None
        self._customer = None
        self._payment_type = None

        if card is not None:
          self.card = card
        if bank is not None:
          self.bank = bank
        if tokenized_card is not None:
          self.tokenized_card = tokenized_card
        if fluid_data is not None:
          self.fluid_data = fluid_data
        if customer is not None:
          self.customer = customer
        if payment_type is not None:
          self.payment_type = payment_type

    @property
    def card(self):
        """
        Gets the card of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The card of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsidrefundsPaymentInformationCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this Ptsv2paymentsidrefundsPaymentInformation.

        :param card: The card of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsidrefundsPaymentInformationCard
        """

        self._card = card

    @property
    def bank(self):
        """
        Gets the bank of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The bank of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationBank
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """
        Sets the bank of this Ptsv2paymentsidrefundsPaymentInformation.

        :param bank: The bank of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationBank
        """

        self._bank = bank

    @property
    def tokenized_card(self):
        """
        Gets the tokenized_card of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The tokenized_card of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationTokenizedCard
        """
        return self._tokenized_card

    @tokenized_card.setter
    def tokenized_card(self, tokenized_card):
        """
        Sets the tokenized_card of this Ptsv2paymentsidrefundsPaymentInformation.

        :param tokenized_card: The tokenized_card of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationTokenizedCard
        """

        self._tokenized_card = tokenized_card

    @property
    def fluid_data(self):
        """
        Gets the fluid_data of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The fluid_data of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationFluidData
        """
        return self._fluid_data

    @fluid_data.setter
    def fluid_data(self, fluid_data):
        """
        Sets the fluid_data of this Ptsv2paymentsidrefundsPaymentInformation.

        :param fluid_data: The fluid_data of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationFluidData
        """

        self._fluid_data = fluid_data

    @property
    def customer(self):
        """
        Gets the customer of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The customer of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this Ptsv2paymentsidrefundsPaymentInformation.

        :param customer: The customer of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationCustomer
        """

        self._customer = customer

    @property
    def payment_type(self):
        """
        Gets the payment_type of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The payment_type of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationPaymentType
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """
        Sets the payment_type of this Ptsv2paymentsidrefundsPaymentInformation.

        :param payment_type: The payment_type of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationPaymentType
        """

        self._payment_type = payment_type

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
        if not isinstance(other, Ptsv2paymentsidrefundsPaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
