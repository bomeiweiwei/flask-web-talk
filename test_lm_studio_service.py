import unittest
from types import SimpleNamespace
from unittest.mock import patch

from services.LMStudioService import LMStudioService


class LMStudioServiceTest(unittest.TestCase):
    @patch("services.LMStudioService.OpenAI", create=True)
    def test_chat_returns_the_model_reply(self, openai_class):
        response = SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content="這是模型回覆")
                )
            ]
        )
        openai_class.return_value.chat.completions.create.return_value = response

        try:
            result = LMStudioService.Chat("你好")
        except TypeError as error:
            self.fail(f"Chat must accept the user's message: {error}")

        self.assertEqual(result, "這是模型回覆")
        openai_class.assert_called_once_with(
            base_url="http://localhost:1234/v1",
            api_key="lm-studio",
        )
        openai_class.return_value.chat.completions.create.assert_called_once_with(
            model="qwen2.5-vl-7b-instruct",
            messages=[{"role": "user", "content": "你好"}],
        )

    @patch("services.LMStudioService.OpenAI", create=True)
    def test_chat_returns_a_friendly_message_when_lm_studio_fails(
        self, openai_class
    ):
        openai_class.side_effect = RuntimeError("connection refused")

        try:
            result = LMStudioService.Chat("你好")
        except TypeError as error:
            self.fail(f"Chat must accept the user's message: {error}")

        self.assertEqual(result, "模型服務暫時無法使用，請稍後再試。")


if __name__ == "__main__":
    unittest.main()
