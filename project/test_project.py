from project import add_transaction, show_transactions, analyze_transactions

import pytest
import csv

@pytest.fixture
def setup_transactions():
    transactions = [
        ["2024-07-01", "Food", "-100.50", "Market Shopping"],
        ["2024-07-02", "Transportation", "-50.00", "Bus Ticket"],
        ["2024-07-03", "Entertainment", "-75.00", "Cinema Ticket"],
        ["2024-07-04", "Salary", "2000.00", "July Salary"],
        ["2024-07-05", "Clothing", "-200.00", "Clothes Shopping"],
        ["2024-07-06", "Health", "-150.00", "Doctor Appointment"]
    ]
    with open('data/transactions.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(transactions)
    return transactions

def test_add_transaction(monkeypatch, setup_transactions):
    inputs = iter(["2024-07-07", "Misc", "50.00", "Misc Income"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    add_transaction()

    with open('data/transactions.csv', newline='') as file:
        reader = csv.reader(file)
        transactions = list(reader)
        assert transactions[-1] == ["2024-07-07", "Misc", "50.00", "Misc Income"]

def test_show_transactions(capsys, setup_transactions):
    show_transactions()
    captured = capsys.readouterr()
    assert "2024-07-01, Food, -100.50, Market Shopping" in captured.out
    assert "2024-07-04, Salary, 2000.00, July Salary" in captured.out
    assert "Monthly Salary" not in captured.out
    assert "Monthly Rent" not in captured.out

def test_analyze_transactions(capsys, setup_transactions):
    analyze_transactions()
    captured = capsys.readouterr()
    expected_income = "Total Income: 2000.00"
    expected_expense = "Total Expense: -575.50"
    assert expected_income in captured.out
    assert expected_expense in captured.out
