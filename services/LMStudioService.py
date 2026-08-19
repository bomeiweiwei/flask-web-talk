import config
from openai import OpenAI


class LMStudioService:
    @classmethod
    def Chat(cls, message):
        try:
            provider = config.PROVIDER
            client = OpenAI(
                base_url=config.LLM_BASE_URL,
                api_key=config.LLM_API_KEY,
            )
            response = client.chat.completions.create(
                model=config.LLM_MODEL,
                messages=[{"role": "user", "content": message}],
            )

            return response.choices[0].message.content
        except Exception:
            return "模型服務暫時無法使用，請稍後再試。"
