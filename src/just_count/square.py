import click 

# Voeg click toe en pas het script aan zodat je het getal zelf kan kiezen
@click.command()
@click.argument("number")

def square(x):
    return x**2


if __name__ == "__main__":
    print(f"The square of {number} is {square(number)}")
