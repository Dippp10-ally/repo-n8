"""Error-reporting helpers for invalid input."""


def explain_invalid_input(value, field_name="value"):
    """Return a helpful validation message for the offending value."""
    if value is None:
        return f"{field_name} is required"
    if isinstance(value, str) and not value.strip():
        return f"{field_name} must not be empty"
    return f"invalid {field_name}: {value!r}"
