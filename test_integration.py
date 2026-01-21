import pytest
from bank_app import transfer, calculate_interest


# -------------------- transfer() --------------------

def test_transfer_success():
    from_balance, to_balance = transfer(1000, 500, 400)
    assert from_balance == 600
    assert to_balance == 900


def test_transfer_exact_balance():
    from_balance, to_balance = transfer(500, 200, 500)
    assert from_balance == 0
    assert to_balance == 700


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(300, 500, 600)


def test_transfer_invalid_amount():
    with pytest.raises(ValueError):
        transfer(1000, 500, -50)


# -------------------- Combined Workflow --------------------

def test_transfer_then_interest():
    from_balance, to_balance = transfer(5000, 2000, 1000)
    updated_balance = calculate_interest(to_balance, 10, 1)
    assert updated_balance == pytest.approx(3300)
