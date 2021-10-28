class DomainException(Exception):
    pass


class AnnualPlanStartingInThePast(DomainException):
    pass


class InvalidSportDiscipline(DomainException):
    pass


class VolumeExceeded(DomainException):
    pass


class RaceStartInThePast(DomainException):
    pass


class InvalidPriority(DomainException):
    pass
