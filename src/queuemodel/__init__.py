import queuemodel.queue as queuelib


def main():
    running = True
    while running:
        try:
            queue_length = int(
                input("What is the length of the queue (0 for infinite):")
            )

            arrival_rate = float(input("What is the arrival rate: "))
            while arrival_rate < 0:
                print("Arrival rate must be greater than 0")
                arrival_rate = float(input("What is the arrival rate: "))

            service_rate = float(input("What is the service rate: "))
            while service_rate < 0:
                print("Service rate must be greater than 0")
                service_rate = float(input("What is the service rate: "))

            queue = queuelib.Queue(
                arrival_rate,
                service_rate,
                queue_length=queue_length if queue_length > 0 else None,
            )

            print("The length of the queue", queue.length_of_the_queue())
            print("The length of the system", queue.length_of_the_system())
            print("The waiting time of the queue", queue.waiting_time_of_queue())
            print("The waiting time of the system", queue.waiting_time_of_system())

            no_person_in_queue = queue.probability_that_no_queue()
            people_in_system = int(input("\nHow many people are in the system: "))

            if queue.queue_length is not None:  # If the queue is finite
                while queue.queue_length > people_in_system:
                    print("Too large to be in system")
                    people_in_system = int(
                        input("\nHow many people are in the system: ")
                    )

            prob_people_in_system = queue.probability_of_no_of_people_in_system(
                people_in_system
            )

            at_least_people_in_system = queue.at_least_people_in_system(
                people_in_system
            )
            at_most_people_in_system = queue.at_most_people_in_system(people_in_system)

            print(f"The probablity of nobody in the queue is {no_person_in_queue}")

            print(
                f"The probablity of {people_in_system} in the system is {prob_people_in_system}"
            )

            print(
                f"The probablity of at least {people_in_system} in the system is {at_least_people_in_system}"
            )

            print(
                f"The probablity of at most {people_in_system} in the system is {at_most_people_in_system}"
            )
            if queue.queue_length is not None:  # If the queue is finite
                doesnt_join = queue.probability_of_no_of_people_in_system(10)
                join = round(1 - doesnt_join, 4)
                print(
                    f"The probablity of a person that comes doesn't the queue is {doesnt_join}"
                )

                print(
                    f"The probablity of a person that comes joining the queue is {join}"
                )

            print("\nYou have reached the end of the program\n")

            running = (
                input("Press enter to start again (back to quit): ").lower() != "back"
            )

        except Exception:
            print("Something went wrong")
            running = False
