# guardian
Simplistic anti-flooding mechanism for limiting chatbot responses, etc..

## Use

```python
anti_flood = guardian.Guardian()

if anti_flood.is_flooding(username, OPTIONAL_FLOOD_LIMIT_INTEGER):
    reply = "You are sending too many requests too quickly."
else:
    reply = "Here is the response you requested."
```
