import asyncio
import tomllib
import unittest
from pathlib import Path


EXPECTED_SQLALCHEMY_DEPENDENCY = "sqlalchemy[asyncio]>=2.0.30,<3.0.0"
PYPROJECT_PATH = Path(__file__).resolve().parents[1] / "pyproject.toml"


class AsyncRuntimeDependencyContract(unittest.TestCase):
    def test_asyncio_extra_declared(self) -> None:
        with PYPROJECT_PATH.open("rb") as pyproject_file:
            pyproject = tomllib.load(pyproject_file)

        dependencies = pyproject["project"]["dependencies"]
        self.assertIn(
            EXPECTED_SQLALCHEMY_DEPENDENCY,
            dependencies,
            "ROOST_ASYNC_DEPENDENCY_DECLARATION: expected "
            f"{EXPECTED_SQLALCHEMY_DEPENDENCY}",
        )

    def test_greenlet_import(self) -> None:
        import greenlet

        self.assertTrue(callable(greenlet.greenlet))

    def test_sqlalchemy_greenlet_spawn(self) -> None:
        from sqlalchemy.util.concurrency import greenlet_spawn

        async def run_bridge() -> str:
            return await greenlet_spawn(lambda: "bridge-ready")

        self.assertEqual(asyncio.run(run_bridge()), "bridge-ready")


if __name__ == "__main__":
    unittest.main(verbosity=2)
