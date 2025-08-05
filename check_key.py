import requests

res = requests.get(
    "https://openrouter.ai/api/v1/auth/verify",
    headers={"Authorization": "Bearer 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"}
)

print(res.status_code)
print(res.text)

