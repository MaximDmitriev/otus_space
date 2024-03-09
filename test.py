import unittest
from tests.move import TestMovable
from tests.rotate import TestRotatable
from tests.exceptions import TestExceptions
from tests.check_fuel import TestCheckFuel
from tests.burn_fuel import TestBurnFuel
from tests.change_velocity import TestChangeVelocity
from tests.macrocmd import TestMacro
from tests.ioc import TestIoCRootScope, TestIoCChildren
from tests.generator import TestAdapterGenerator


if __name__ == '__main__':
    unittest.main()