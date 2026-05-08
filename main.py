import sentry_sdk
from app.converter import celsius_to_fahrenheit

sentry_sdk.init(
    dsn="https://d27258db425273c83ad2628bee2c90cd@o4511296908427264.ingest.de.sentry.io/4511296918257744",
    traces_sample_rate=1.0,
)


def main():
    try:
        user_input = input("Введіть температуру у Цельсіях: ")

        celsius = float(user_input)

        fahrenheit = celsius_to_fahrenheit(celsius)

        print(f"Температура у Фаренгейтах: {fahrenheit}")

    except ValueError as e:
        sentry_sdk.capture_exception(e)
        sentry_sdk.flush()
        print("Помилка: введіть коректне число")


if __name__ == "__main__":
    main()
