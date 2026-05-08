from app.converter import celsius_to_fahrenheit


def main():
    try:
        user_input = input("Введіть температуру у Цельсіях: ")

        celsius = float(user_input)

        fahrenheit = celsius_to_fahrenheit(celsius)

        print(f"Температура у Фаренгейтах: {fahrenheit}")

    except ValueError:
        print("Помилка: введіть коректне число")


if __name__ == "__main__":
    main()