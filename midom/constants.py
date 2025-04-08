"""Implementations of some of the MIDOM constants and objects"""

class DeltaStatusCodes:
    """How has a DICOM element changed?"""

    UNCHANGED = "UNCHANGED"
    CHANGED = "CHANGED"
    REMOVED = "REMOVED"
    EMPTIED = "EMPTIED"
    CREATED = "CREATED"

    ALL = {UNCHANGED, CHANGED, REMOVED, EMPTIED, CREATED}