import math
import random
from typing import List


class City:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def distance_to(self, other_city: 'City') -> float:
        return math.sqrt((self.x - other_city.x)**2 + (self.y - other_city.y)**2)


class Route:
    def __init__(self, cities: List[City]):
        self.cities = cities
        self.distance = self._calculate_distance()
    
    def _calculate_distance(self) -> float:
        total_distance = 0.0
        for i in range(len(self.cities)):
            j = (i + 1) % len(self.cities)
            total_distance += self.cities[i].distance_to(self.cities[j])
        return total_distance

    def fitness(self) -> float:
        return 1 / self.distance if self.distance > 0 else float('inf')


def generate_initial_population(size: int, cities: List[City]) -> List[Route]:
    population = []
    for i in range(size):
        shuffled_cities = random.sample(cities, len(cities))
        population.append(Route(shuffled_cities))
    return population


def selection(population: List[Route], elite_size: int) -> List[Route]:
    sorted_population = sorted(population, key=lambda x: x.fitness(), reverse=True)
    return sorted_population[:elite_size]


def crossover(parent1: Route, parent2: Route) -> Route:
    gene1 = int(random.random() * len(parent1.cities))
    gene2 = int(random.random() * len(parent1.cities))
    start_gene = min(gene1, gene2)
    end_gene = max(gene1, gene2)

    child_cities = [None] * len(parent1.cities)
    for i in range(start_gene, end_gene + 1):
        child_cities[i] = parent1.cities[i]

    for i in range(len(parent2.cities)):
        city = parent2.cities[i]
        if city not in child_cities:
            for j in range(len(child_cities)):
                if child_cities[j] is None:
                    child_cities[j] = city
                    break

    return Route(child_cities)


def mutation(route: Route, mutation_rate: float) -> Route:
    for i in range(len(route.cities)):
        if random.random() < mutation_rate:
            j = int(random.random() * len(route.cities))
            route.cities[i], route.cities[j] = route.cities[j], route.cities[i]
    return route


def evolution(population: List[Route], elite_size: int, mutation_rate: float) -> List[Route]:
    elite_routes = selection(population, elite_size)
    offspring_size = len(population) - elite_size
    offspring = []

    for i in range(offspring_size):
        parent1 = random.choice(elite_routes)
        parent2 = random.choice(elite_routes)
        child = crossover(parent1, parent2)
        offspring.append(child)

    for i in range(len(offspring)):
        offspring[i] = mutation(offspring[i], mutation_rate)

    return elite_routes + offspring


def genetic_algorithm(cities: List[City], population_size: int, elite_size: int, mutation_rate: float, generations: int) -> Route:
    population = generate_initial_population(population_size, cities)
    best_route = None

    for i in range(generations):
        population = evolution(population, elite_size, mutation_rate)
        current_best_route = sorted(population, key=lambda x: x.fitness(), reverse=True)[0]
        if best_route is None or current_best_route.fitness() > best_route.fitness():
            best_route = current_best_route

    return best_route


if __name__ == '__main__':
    cities = [City(x=60, y=200), City(x=180, y=200),
              City(x=80, y=180), City(x=140, y=180),
              City(x=20, y=160), City(x=100, y=160),
              City(x=200, y=160)]

    best_route = genetic_algorithm(cities, population_size=100, elite_size=20, mutation_rate=0.01, generations=500)

    print([city.__dict__ for city in best_route.cities])  # print the order of cities in the best route
    print(best_route.distance)  # print the total distance of the best route