week_limit = float(input('Витрати на неділю: '))

days = ["пн", "вт", "ср", "чт", "пт", "сб", "нд"]
expenses = {}

for day in days:
    expenses[day] = float(input(f"Витрати на {day}: "))

all_day = sum(expenses.values())

if all_day < week_limit:
    print(f'Залишок: {week_limit - all_day}')
else:
    print('Перевищено ліміт')

print("\nВитрати по днях:")
for day in days:
    print(f"{day}: {expenses[day]}")