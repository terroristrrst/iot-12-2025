import sys
import os
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.max_flow import parse_csv_content, build_network


class TestMaxFlow(unittest.TestCase):
    def test_parse_csv_content(self):
        lines = [
            "F1, F2",
            "S1, S2",
            "F1, X1, 5",
            "X1, S1, 3",
        ]
        farms, shops, edges = parse_csv_content(lines)
        self.assertEqual(farms, ["F1", "F2"])
        self.assertEqual(shops, ["S1", "S2"])
        self.assertEqual(edges, [("F1", "X1", 5), ("X1", "S1", 3)])

    def test_simple_network(self):
        farms = ["F1"]
        shops = ["S1"]
        edges = [("F1", "S1", 10)]
        solver, src, sink = build_network(farms, shops, edges)
        flow = solver.max_flow(src, sink)
        self.assertEqual(flow, 10)

    def test_two_farms_one_shop(self):
        farms = ["F1", "F2"]
        shops = ["S1"]
        edges = [("F1", "S1", 5), ("F2", "S1", 7)]
        solver, src, sink = build_network(farms, shops, edges)
        flow = solver.max_flow(src, sink)
        self.assertEqual(flow, 12)

    def test_two_way_roads(self):
        farms = ["F1"]
        shops = ["S1"]
        edges = [("F1", "X1", 5), ("X1", "X2", 3), ("X2", "S1", 5)]
        solver, src, sink = build_network(farms, shops, edges)
        flow = solver.max_flow(src, sink)
        self.assertEqual(flow, 3)

    def test_full_example(self):
        csv_content = [
            "F1, F2, F3",
            "S1, S2, S3, S4, S5",
            "F1, X1, 5",
            "F2, X1, 4",
            "F3, X3, 10",
            "X1, X2, 6",
            "X2, S1, 3",
            "X2, S2, 2",
            "X1, S3, 4",
            "X3, S4, 10",
        ]
        farms, shops, edges = parse_csv_content(csv_content)
        solver, src, sink = build_network(farms, shops, edges)
        flow = solver.max_flow(src, sink)
        self.assertEqual(flow, 19)


if __name__ == "__main__":
    unittest.main()