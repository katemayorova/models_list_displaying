from datetime import datetime


class DateConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
    __FORMAT = '%Y-%m-%d'

    @staticmethod
    def to_python(value: str) -> datetime:
        return datetime.strptime(value, DateConverter.__FORMAT)

    @staticmethod
    def to_url(value: datetime) -> str:
        return value.strftime(DateConverter.__FORMAT)


