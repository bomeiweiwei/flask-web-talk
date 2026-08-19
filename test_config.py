import os
import subprocess
import sys
import unittest


class ConfigTest(unittest.TestCase):
    def run_config(self, **environment):
        env = os.environ.copy()
        for name in (
            "APP_NAME",
            "DEBUG",
            "PROVIDER",
            "LLM_BASE_URL",
            "LLM_API_KEY",
            "LLM_MODEL",
        ):
            env.pop(name, None)
        env.update(environment)

        result = subprocess.run(
            [
                sys.executable,
                "-c",
                (
                    "import config; "
                    "print(config.APP_NAME); "
                    "print(config.DEBUG); "
                    "print(config.PROVIDER); "
                    "print(config.LLM_BASE_URL); "
                    "print(config.LLM_API_KEY); "
                    "print(config.LLM_MODEL)"
                ),
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
            [
                "Flask Azure Demo",
                "True",
                "lmstudio",
                "http://localhost:1234/v1",
                "lm-studio",
                "qwen2.5-vl-7b-instruct",
            ],
        )

    def test_reads_values_from_environment(self):
        self.assertEqual(
            self.run_config(
                APP_NAME="My Flask App",
                DEBUG="False",
                PROVIDER="custom-provider",
                LLM_BASE_URL="https://llm.example/v1",
                LLM_API_KEY="secret-key",
                LLM_MODEL="custom-model",
            ),
            [
                "My Flask App",
                "False",
                "custom-provider",
                "https://llm.example/v1",
                "secret-key",
                "custom-model",
            ],
        )


if __name__ == "__main__":
    unittest.main()
