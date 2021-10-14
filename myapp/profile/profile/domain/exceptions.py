class DomainFailed(Exception):
    pass


class IncorrectMainSport(DomainFailed):
    pass


class LactateThresholdNotSet(DomainFailed):
    pass


class MaxHrNotSet(DomainFailed):
    pass
