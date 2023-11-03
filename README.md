# 🦜🔗 LangServe Replit Template

[![Run on Repl.it](https://replit.com/badge/github/langchain-ai/langserve-replit-template)](https://replit.com/new/github/langchain-ai/langserve-replit-template)

This template shows how to deploy a [LangChain Expression Language Runnable](https://python.langchain.com/docs/expression_language/) as a set of HTTP endpoints with stream and batch support using [LangServe](https://github.com/langchain-ai/langserve) onto [Replit](https://replit.com), a collaborative online code editor and platform for creating and deploying software.

## Getting started

The default chat endpoint is a chain that translates questions into pirate dialect.

1. Deploy your app to Replit by [clicking here](https://replit.com/new/github/langchain-ai/langserve-replit-template).
    - You will also need to set an `OPENAI_API_KEY` environment variable by going under `Tools > Secrets` in the bottom left corner.
2. Press `Run` on `main.py`.
3. Navigate to `https://your_url.repl.co/docs/` to see documentation for your live runnable!

// TODO: Add LangSmith tracing guide with extension

## Calling from the client

You can use the `RemoteRunnable` class in LangServe to call these hosted runnables:

```python
from langserve import RemoteRunnable

pirate_chain = RemoteRunnable("https://your_url.repl.co/pirate-speak/")

pirate_chain.invoke({"question": "how are you?"})

# or async
await pirate_chain.ainvoke({"question": "how are you?"})

# Supports astream
async for msg in pirate_chain.astream({"question": "how are you?"}):
    print(msg, end="", flush=True)
```

In TypeScript (requires [LangChain.js](https://github.com/langchain-ai/langchainjs) version 0.0.166 or later):

```typescript
import { RemoteRunnable } from "langchain/runnables/remote";

const pirateChain = new RemoteRunnable({ url: `https://your_url.repl.co/pirate-speak/` });
const result = await pirateChain.invoke({
  "question": "how are you?",
});
```

You can also use `curl`:

```curl
curl --location --request POST 'https://your_url.repl.co/pirate-speak/invoke' \
--header 'Content-Type: application/json' \
--data-raw '{
    "input": {
        "question": "how are you?"
    }
}'
```

## Adding more chains

You can add more chains from a variety of templates by using the LangChain CLI:

`$ langchain app add <template name>`

For full docs and a list of possible templates, see the [official page here](https://github.com/langchain-ai/langchain/tree/master/templates).

## API reference

LangServe makes the following endpoints available:

- `POST /my_runnable/invoke` - invoke the runnable on a single input
- `POST /my_runnable/batch` - invoke the runnable on a batch of inputs
- `POST /my_runnable/stream` - invoke on a single input and stream the output
- `POST /my_runnable/stream_log` - invoke on a single input and stream the output, including partial outputs of intermediate steps
- `GET /my_runnable/input_schema` - json schema for input to the runnable
- `GET /my_runnable/output_schema` - json schema for output of the runnable
- `GET /my_runnable/config_schema` - json schema for config of the runnable

You can navigate to `https://your_url.repl.co/docs/` to see generated documentation.

## Thank you!

Here are some convenient links:

- [LangServe](https://github.com/langchain-ai/langserve)
- [LangChain](https://github.com/langchain-ai/langchain)
- [LangChain.js](https://github.com/langchain-ai/langchainjs)

Follow LangChain on X (formerly Twitter) [@LangChainAI](https://x.com/langchainai) for more!
