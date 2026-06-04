"""UI Track · boundary · U-OUT-01~02."""

from boundary.solve_gateway import solve_partial


def test_u_out_01_g1_solution_length_six(grid_g1):
    """TestID: U-OUT-01 | G1 Golden · len(result)==6."""
    result = solve_partial(grid_g1)
    assert len(result) == 6


def test_u_out_02_g1_solution_field_order(grid_g1):
    """TestID: U-OUT-02 | [r1,c1,n1,r2,c2,n2]."""
    assert solve_partial(grid_g1) == [2, 2, 10, 3, 3, 7]
