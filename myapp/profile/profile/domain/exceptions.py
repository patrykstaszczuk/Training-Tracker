class DomainFailed(Exception):
    pass


class IncorrectMainSport(DomainFailed):
    pass


class LactateThresholdNotSet(DomainFailed):
    pass


class FtpNotSet(DomainFailed):
    pass


class MaxHrNotSet(DomainFailed):
    pass


class MissingUserId(DomainFailed):
    pass


class ProfileAlreadyCreated(DomainFailed):
    pass
