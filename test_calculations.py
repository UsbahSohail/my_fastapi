import pytest
from app.calculations import add, BankAccount, divide,  InsufficientFunds, multiply, subtract

# Fixtures defined in the same file
@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected

def test_subtract():
    assert subtract(9, 5) == 4

def test_multiply():
    assert multiply(5, 5) == 25

def test_divide():
    assert divide(10, 2) == 5

def test_bank_set_initial_amount(bank_account):
    # Test initialization with 50
    assert bank_account.balance == 50

def test_bank_set_default_amount(zero_bank_account):
    # Test initialization with default value (0)
    assert zero_bank_account.balance == 0
    
def test_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.balance == 20
    
def test_deposit(bank_account):
    bank_account.deposit(30)
    assert bank_account.balance == 80
    
def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance) == 55
    
@pytest.mark.parametrize("deposited, withdraw, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
])
def test_bank_transaction(zero_bank_account, deposited, withdraw, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected
    
def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(100)    
        
        
