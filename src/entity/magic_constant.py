"""Magic constant SSOT (R-04 / INV-04)."""

from entity.constants import MAGIC_CONSTANT


class MagicConstant:
    """Derived magic line sum — no literal 34."""

    @property
    def value(self) -> int:
        return MAGIC_CONSTANT
