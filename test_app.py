import unittest
from unittest.mock import patch

from app import app


class SubmitTest(unittest.TestCase):
    @patch("app.LMStudioService", create=True)
    def test_submit_displays_the_model_reply(self, lm_studio_service):
        lm_studio_service.Chat.return_value = "模型產生的內容"
        client = app.test_client()

        response = client.post("/submit", data={"message": "使用者問題"})

        self.assertEqual(response.status_code, 200)
        lm_studio_service.Chat.assert_called_once_with("使用者問題")
        self.assertIn("模型產生的內容", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
