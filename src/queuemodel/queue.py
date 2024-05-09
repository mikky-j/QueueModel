import math
from typing import Optional


class Queue:
    def __init__(
        self,
        arrival_rate: float,
        service_rate: float,
        queue_length: Optional[int] = None,
    ):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.rho = round(arrival_rate / service_rate, 4)
        self.queue_length = queue_length

    def effective_arrival_rate(self) -> float:
        answer = 0
        if self.queue_length is not None:
            answer = self.arrival_rate * (
                1 - self.probability_of_no_of_people_in_system(self.queue_length)
            )

        return round(answer, 4)

    def probability_of_no_of_people_in_system(self, no_of_person: int) -> float:
        probability = 0
        if self.queue_length is None:  # If the queue is infinite
            probability = math.pow(self.rho, no_of_person) * (1 - self.rho)
        else:
            probability = math.pow(self.rho, no_of_person) * (
                (1 - self.rho) / (1 - math.pow(self.rho, self.queue_length + 1))
            )
        return round(probability, 4)

    def length_of_the_system(self):
        length = 0
        if self.queue_length is None:  # If the queue is infinite
            length = self.rho / (1 - self.rho)
        else:
            numerator = self.rho * (
                1
                + self.queue_length * math.pow(self.rho, self.queue_length + 1)
                - (self.queue_length + 1) * math.pow(self.rho, self.queue_length)
            )
            denominator = (1 - self.rho) * (
                1 - math.pow(self.rho, self.queue_length + 1)
            )
            length = numerator / denominator
        return round(length, 4)

    def length_of_the_queue(self):
        answer = 0
        if self.queue_length is None:  # If the queue is infinite

            answer = self.length_of_the_system() - self.rho
        else:
            answer = self.length_of_the_system() - (
                self.effective_arrival_rate() / self.service_rate
            )

        return round(answer, 4)

    def waiting_time_of_system(self):
        answer = 0
        if self.queue_length is None:  # If the queue is infinite
            answer = self.length_of_the_system() / self.arrival_rate
        else:
            answer = self.length_of_the_system() / self.effective_arrival_rate()

        return round(answer, 4)

    def waiting_time_of_queue(self):
        answer = 0
        if self.queue_length is None:  # If the queue is infinite
            answer = self.length_of_the_queue() / self.arrival_rate
        else:
            answer = self.waiting_time_of_system() - (1 / self.service_rate)

        return round(answer, 4)

    def probability_that_no_queue(self):
        answer = self.probability_of_no_of_people_in_system(
            0
        ) + self.probability_of_no_of_people_in_system(1)
        return round(answer, 4)

    def at_least_people_in_system(self, people_in_system: int):
        """
        To find the probability that at least x people would be in the system
        We need to find the probability that at most x people are in the system and then
        negate it from 1
        """
        answer = 1 - self.at_most_people_in_system(people_in_system - 1)
        return round(answer, 4)

    def at_most_people_in_system(self, people_in_system: int):
        """
        To find the probability that at most x people would be in the system
        We need to sum up all the probabilities up to x people
        """
        answer = 0
        for i in range(people_in_system + 1):
            answer += self.probability_of_no_of_people_in_system(i)
        return round(answer, 4)
