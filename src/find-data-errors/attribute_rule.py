"""
Attribute rules for validating values.
"""

import re
import sys
import unicodedata

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

class NonVisibleCodepointsRule(AttributeRule):
    """
    Defines an attribute rule for non visible characters.
    """
    def __init__(self):
        """
        Initializes this unicode rule.
        """
        chars = [chr(charCode) for charCode in range(sys.maxunicode)]
        chars = [char for char in chars if unicodedata.category(char) == u"Cc"]
        pattern = u"[%s]" % re.escape(u"".join(chars))
        super(NonVisibleCodepointsRule, self).__init__(pattern)
