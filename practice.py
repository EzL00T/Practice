week_limit = float(input('Витрати на неділю: '))

monday = float(input("Витрати на пн: "))
tuesday = float(input("Витрати на вт: "))
wednesday = float(input("Витрати на ср: "))
thursday = float(input("Витрати на чт: "))
friday = float(input("Витрати на пт: "))
saturday = float(input("Витрати на сб: "))
sunday = float(input("Витрати на нд: "))

all_day = monday + tuesday + wednesday + thursday + friday + saturday + sunday

if all_day < week_limit:
    print(f'Залишок: {week_limit - all_day}')
else:
    print('Перевищено ліміт')