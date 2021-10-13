class DomainFailed(Exception):
    pass


class NameTooShort(DomainFailed):
    pass


class SurnameTooShort(DomainFailed):
    pass


class IncorrectMainSport(DomainFailed):
    pass
