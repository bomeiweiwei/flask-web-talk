import os
import subprocess
import sys
import unittest


class ConfigTest(unittest.TestCase):
    def run_config(self, **environment):
        env = os.environ.copy()
        env.pop("APP_NAME", None)
        env.pop("DEBUG", None)
        env.update(environment)

        result = subprocess.run(
            [
                sys.executable,
                "-c",
                "import config; print(config.APP_NAME); print(config.DEBUG)",
            ],
            capture_output=True,
            check=False,
            env=env,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.splitlines()

    def test_uses_default_values_when_environment_is_empty(self):
        self.assertEqual(
            self.run_config(),
            ["Flask Azure Demo", "True"],
        )

    def test_reads_values_from_environment(self):
        self.assertEqual(
            self.run_config(APP_NAME="My Flask App", DEBUG="False"),
            ["My Flask App", "False"],
        )


if __name__ == "__main__":
    unittest.main()
