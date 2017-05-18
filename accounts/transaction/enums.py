from django.utils.translation import gettext as _
from enumerify.enum import Enum

class AccountType(Enum):
    CASH = 1
    BANK = 2   
    IOU = 3

    i18n = (
        _('Cash'),
        _('Bank'),
        _('IOU'),        
    )