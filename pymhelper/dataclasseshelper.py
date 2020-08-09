"""Dataclasses helper stands for auto converting field types, whenever it is
possible. Usually Assets represented in JSON and strings formats."""

import logging
from dataclasses import dataclass, fields

logger = logging.getLogger(__name__)


@dataclass
class AutoConvertingField:
    """Field auto converting base class."""

    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                logger.debug('Expected %s to be %s, got %s. Converting to %s.',
                             field.name, field.type, repr(value),
                             field.type(value))
                setattr(self, field.name, field.type(value))
