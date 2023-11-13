import click 

def square(number):
    return number**2
# Voeg click toe en pas het script aan zodat je het getal zelf kan kiezen
@click.command()
# @click.argument("number")
@click.option( 
    "-n",
    "--number",
    default=1,
    help="Number that you want the square of",
    show_default=True,  # show default in help
    )
def square(number):
    return print(f"The square of {number} is {(number)**2}")

if __name__ == "__main__":
    square()
    # print(f"The square of {number} is {square(number)}")
