import calculator

if __name__ == '__main__':
    calc = calculator.Calculator(years=3)
    calc.add_car(
        calculator.Car('Toyota Corolla', price=120000,
                       fuel_economy=7, service_cost=1200, insurance_cost=2500)
    )

    calc.add_car(
        calculator.Car('Tesla', price=120000,
                       fuel_economy=7, service_cost=1200, insurance_cost=2500)
    )
    calc.add_car(
        calculator.Car('Audi A1', price=500000,
                       fuel_economy=3, service_cost=300, insurance_cost=7000)
    )

calc.print_cars()