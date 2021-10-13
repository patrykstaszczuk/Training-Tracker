class DomainFailed(Exception):
    pass


class NameTooShort(DomainFailed):
    pass


class SurnameTooShort(DomainFailed):
    pass


class IncorrectMainSport(DomainFailed):
    pass


class LactateThresholdNotSet(DomainFailed):
    pass


class MaxHrNotSet(DomainFailed):
    pass
