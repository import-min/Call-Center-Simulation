This project simulates call handling times in a customer service setting using a custom random number generator. It models call availability, representative response times, and hang-ups over 500 trials.

Features:
- Custom linear congruential RNG
- Discrete states for call availability (busy, unavailable, available)
- Continuous distribution for call duration
- Simulation of up to 4 unsuccessful calls before success or termination
- Statistical summary: mean, median, quartiles
- CDF plot of total call times

Usage:
- Install dependencies: pip install numpy pandas matplotlib
- Run the simulation script to see stats and CDF plot.
