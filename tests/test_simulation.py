from src.simulation import Simulation


class TestSimulation:
    def test_single_simulation_runs(self):
        sim = Simulation()
        result = sim.run_single()

        assert result is not None
        assert "result" in result
        assert result["result"] in ["predator_wins", "prey_escaped", "prey_wins"]

    def test_multiple_simulations_runs_correct_count(self):
        sim = Simulation()
        results = sim.run_multiple(5)

        assert len(results) == 5

    def test_all_simulations_have_valid_results(self):
        sim = Simulation()
        results = sim.run_multiple(10)

        for result in results:
            assert result["result"] in ["predator_wins", "prey_escaped", "prey_wins"]
