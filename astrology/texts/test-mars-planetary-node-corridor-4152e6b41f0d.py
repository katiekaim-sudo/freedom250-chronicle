import json
import unittest
from pathlib import Path

import build_mars_planetary_node_corridor as corridor


HERE = Path(__file__).resolve().parent


class MarsPlanetaryNodeCorridorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = corridor.build_payload()

    def test_generated_artifact_matches_builder(self):
        stored = json.loads((HERE / "mars_planetary_node_corridor.json").read_text())
        self.assertEqual(stored, self.payload)

    def test_exact_crossing_order_and_residuals(self):
        rows = self.payload["exact_crossings"]
        self.assertEqual([row["node_body"] for row in rows], ["Jupiter", "Pluto", "Saturn", "Neptune"])
        self.assertTrue(all(row["residual_arcsec"] < 0.01 for row in rows))
        self.assertEqual([row["node"]["sign"] for row in rows], ["Cancer", "Cancer", "Cancer", "Leo"])

    def test_full_moon_contains_the_saturn_node_hit_but_opposition_does_not(self):
        full = self.payload["full_moon_saturn_node_snapshot"]
        opposition = self.payload["opposition_saturn_node_snapshot"]
        self.assertAlmostEqual(full["orb_deg"], 0.487819, places=6)
        self.assertTrue(full["inside_chart_bone_orb"])
        self.assertAlmostEqual(opposition["orb_deg"], 3.189738, places=5)
        self.assertFalse(opposition["inside_chart_bone_orb"])

    def test_crossing_sits_between_full_moon_and_sign_change(self):
        sequence = [row["event"] for row in self.payload["anchor_sequence"]]
        self.assertLess(sequence.index("Aries Full Moon"), sequence.index("Mars conjunct Saturn NN"))
        self.assertLess(sequence.index("Mars conjunct Saturn NN"), sequence.index("Mars enters Leo"))
        self.assertLess(sequence.index("Mars enters Leo"), sequence.index("Mars opposite Pluto"))
        self.assertAlmostEqual(self.payload["intervals_hours"]["full_moon_to_saturn_node"], 21.417219, places=3)

    def test_corridor_is_deduplicated_and_controlled(self):
        clustering = self.payload["clustering_control"]
        self.assertTrue(clustering["jupiter_pluto_saturn_nodes_all_in_cancer"])
        self.assertEqual(clustering["neptune_node_sign"], "Leo")
        control = self.payload["registered_chart_control"]
        self.assertEqual(control["registered_chart_count"], 30)
        self.assertEqual(control["all_node_hit_count"], 30)
        self.assertEqual(control["mars_node_hit_count"], 5)
        self.assertEqual(control["flag_counts"], {"escalation": 19, "resolution": 4, "unflagged": 7})

    def test_hypothesis_is_not_promoted(self):
        boundaries = " ".join(self.payload["interpretive_boundaries"])
        self.assertIn("escalation rule null", boundaries)
        self.assertIn("no evidence, convergence, causation or Forecast Ledger credit", boundaries)


if __name__ == "__main__":
    unittest.main()
