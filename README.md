# ✈️ Flight Planner — Optimal Route Recommendation System

A graph-based flight planning system that selects the best travel itineraries based on different optimization goals: fewest connections, lowest cost, and earliest arrival. Built using Python with efficient traversal algorithms and a custom min-heap implementation.

## 📌 Project Overview

This project simulates a real-world flight booking assistant that supports:
- **Minimum Connections**: Route with the least number of flights and earliest arrival.
- **Cheapest Fare**: Route with the lowest total cost.
- **Hybrid Optimization**: Route with the fewest flights and, among them, the cheapest.

It respects layover constraints (minimum 20-minute gap between connections) and time-window preferences.

---

## 🛠️ Features

- Efficient **graph representation** using adjacency lists (`O(m)` initialization).
- Custom **min-heap** implementation for multi-criteria priority queues.
- Realistic **connection rules** (e.g. layover times, time window limits).
- Modular code: `Flight`, `Planner`, and `Heap` classes for clarity and reusability.
- Optimal algorithm runtimes for different use-cases:
  - `least_flights_earliest_route`: `O(m)` — BFS with priority on fewest hops and early arrival.
  - `cheapest_route`: `O(m log m)` — Dijkstra’s algorithm minimizing fare.
  - `least_flights_cheapest_route`: `O(m log m)` — BFS variant with dual-priority (hop count, fare).

---

## 🧱 Project Structure

── flight.py # Flight data class with attributes: start_city, end_city, times, fare
├── planner.py # Core logic for route planning using BFS and Dijkstra variants
├── main.py # Driver code to test routes and display outputs

📈 Complexity Analysis
Function	Time Complexity
__init__	O(m)
least_flights_earliest_route	O(m)
cheapest_route	O(m log m)
least_flights_cheapest_route	O(m log m)

Where m is the number of flights in the system.

🧠 Concepts Used
Graph traversal (BFS, Dijkstra)

Min-heaps and custom comparators

Object-oriented design

Real-world constraints modeling

Space-time tradeoffs in route optimization.
