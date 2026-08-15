"""Explain password strength using simple, transparent rules."""
import string


def assess(password: str) -> list[str]:
    checks = []
    if len(password) >= 10: checks.append('10+ characters')
    if any(char.isupper() for char in password): checks.append('uppercase letter')
    if any(char.islower() for char in password): checks.append('lowercase letter')
    if any(char.isdigit() for char in password): checks.append('number')
    if any(char in string.punctuation for char in password): checks.append('symbol')
    return checks


if __name__ == '__main__':
    value = input('Password to assess (not stored): ')
    checks = assess(value)
    print(f'{len(checks)}/5 rules passed')
    print('Passed: ' + (', '.join(checks) if checks else 'none'))
