"""
Attribute rules for validating values.
"""

import re

class AttributeRule:
    """
    Defines an attribute rule.
    """

    def __init__(self, pattern):
        """
        Initializes this rule with a pattern.
        """
        self.matcher = re.compile(pattern)

    def matches(self, value):
        """
        True if the value matches this rule.
        """
        return self.matcher.match(value) is None
