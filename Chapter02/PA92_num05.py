distance = int(input("주행거리(km): "))
fuel_efficiency = float(input("연비(km/l): "))
fuel_amount = distance / fuel_efficiency
print(f"필요한 연료량: {fuel_amount:.2f}l")