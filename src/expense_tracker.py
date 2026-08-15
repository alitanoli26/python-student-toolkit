"""Tiny CSV expense tracker using only the Python standard library."""
import csv
from pathlib import Path


FILE = Path('expenses.csv')


def add_expense(category: str, amount: float) -> None:
    exists = FILE.exists()
    with FILE.open('a', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        if not exists:
            writer.writerow(['category', 'amount'])
        writer.writerow([category, f'{amount:.2f}'])


def total() -> float:
    if not FILE.exists():
        return 0.0
    with FILE.open(newline='', encoding='utf-8') as handle:
        return sum(float(row['amount']) for row in csv.DictReader(handle))


if __name__ == '__main__':
    category = input('Category: ').strip() or 'General'
    try:
        amount = float(input('Amount: '))
        if amount < 0: raise ValueError('Amount must be positive')
        add_expense(category, amount)
        print(f'All-time total: {total():.2f}')
    except ValueError as error:
        print(f'Input error: {error}')
