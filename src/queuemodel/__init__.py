import math
import rich
from rich.console import Console
from rich.prompt import Confirm, FloatPrompt, IntPrompt


def model_queue(console: Console):
    arrival_rate = FloatPrompt.ask("[blue]Enter arrival rate per hour")

    while arrival_rate <= 0:
        console.print("[red]Arrival rate must be greater than 0")
        arrival_rate = FloatPrompt.ask("[blue]Enter arrival rate per hour")

    service_rate = FloatPrompt.ask("[blue]Enter service rate: ")

    while service_rate <= 0:
        console.print("[red]Service rate must be greater than 0")
        service_rate = FloatPrompt.ask("[blue]Enter service rate per hour")

    pho = arrival_rate / service_rate

    n = IntPrompt.ask("[blue]Input the number of people: ")

    p = 1 - pho

    pn = math.pow(p, n) * p

    console.print(f"\n[green]For {n} number of people, the answer is {pn}")

    len_of_system = pho / p
    len_of_queue = len_of_system - pho
    wait_of_system = len_of_system / arrival_rate
    wait_of_queue = len_of_queue / arrival_rate

    console.print(f"\n[green]The length of the system is {len_of_system}")
    console.print(f"[green]The length of the queue is {len_of_queue}")
    console.print(f"[green]The waiting time of the system is {wait_of_system}")
    console.print(f"[green]The waiting time of the queue is {wait_of_queue}")


def main():
    console = rich.get_console()
    running = True
    while running:
        console.clear()
        model_queue(console)
        running = Confirm.ask("\nDo you still want to continue")
    console.print("\n[green]Thank you for running")
