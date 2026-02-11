from src.constants import NUM_SIMULATIONS
from src.simulation import Simulation


def main():
    sim = Simulation()
    results = sim.run_multiple(NUM_SIMULATIONS)

    print(f"\n{'=' * 50}")
    print("FINAL RESULTS")
    print("=" * 50)

    predator_wins = sum(1 for r in results if r["result"] == "predator_wins")
    prey_escapes = sum(1 for r in results if r["result"] in ["prey_escaped", "prey_wins"])

    print(f"Predator wins: {predator_wins}")
    print(f"Prey escapes: {prey_escapes}")


if __name__ == "__main__":
    main()
