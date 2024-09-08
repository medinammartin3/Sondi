from django import template
from hashids import Hashids
import os
from dotenv import load_dotenv

load_dotenv()

"""
Setting up custom filter to encode values with hashids in the Django templates.
"""

register = template.Library()
hashids = Hashids(salt=os.getenv("HASHID_SALT"), min_length=8)

@register.filter(name='hashid_encode')
def hashid_encode(value):
    return hashids.encode(value)
