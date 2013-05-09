from django.forms.widgets import Input


class NumberInput(Input):
    """HTML5 Number Input."""
    input_type = 'number'


class SearchInput(Input):
    """HTML5 Search Input."""
    input_type = 'search'


class EmailInput(Input):
    """HTML5 Email Input."""
    input_type = 'email'


class URLInput(Input):
    """HTML5 URL Input."""
    input_type = 'url'


class RangeInput(Input):
    """HTML5 Range Input."""
    input_type = 'range'