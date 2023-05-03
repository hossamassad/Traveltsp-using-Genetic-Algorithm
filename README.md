
# Traveling Salesman Problem Solver using Genetic Algorithm

This is a Python implementation of a Genetic Algorithm to solve the Traveling Salesman Problem (TSP). Given a list of cities and the distances between them, the task is to find the shortest possible route that visits each city exactly once and returns to the origin city.

The program defines two classes: `City` and `Route`. The `City` class represents a city with `x` and `y` coordinates and a method for calculating the distance to another city. The `Route` class represents a possible solution to the TSP problem and has methods for calculating the total distance of the route and a fitness score.

The program also defines several functions for generating an initial population, selecting the best routes from the current population, performing crossover and mutation to create new offspring, and evolving the population over multiple generations to find an approximate solution to the TSP problem.

## Requirements

- Python 3.6 or higher

## Usage

To run the program with the default parameters and example cities, simply run the following command:

```
python tsp_ga.py
```

To specify your own set of cities and other parameters, you can modify the code in the `main` function or create your own script that imports the necessary classes and functions.

## Parameters

The `genetic_algorithm` function takes the following parameters:

- `cities`: a list of `City` objects representing the cities to be visited
- `population_size`: the size of the initial population of routes
- `elite_size`: the number of top routes to select as parents for the next generation
- `mutation_rate`: the probability of a mutation occurring during crossover
- `generations`: the number of generations to evolve the population

## Example Output

The program outputs the order of cities in the best route found and the total distance of that route. Here is an example output:

```
[{'x': 140, 'y': 180}, {'x': 100, 'y': 160}, {'x': 80, 'y': 180}, {'x': 60, 'y': 200}, {'x': 20, 'y': 160}, {'x': 180, 'y': 200}, {'x': 200, 'y': 160}]
666.0160150371321
```

This indicates that the best route found visits the cities in the order shown and has a total distance of approximately 666 units.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
