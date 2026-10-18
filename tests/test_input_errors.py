from src.input_errors import explain_invalid_input


def test_reports_none_as_missing():
    assert explain_invalid_input(None, "name") == "name is required"


def test_reports_blank_value():
    assert explain_invalid_input("   ", "name") == "name must not be empty"


def test_reports_invalid_value():
    assert "invalid name" in explain_invalid_input(5, "name")
