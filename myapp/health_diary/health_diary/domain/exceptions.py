class DomainFailed(Exception):
    pass


class MealNameTooLong(DomainFailed):
    pass


class DiaryDoesNotExists(DomainFailed):
    pass
