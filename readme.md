# xAi Playground

Welcome to the **xAi Playground**!  
This repository is designed as a comprehensive playground to experiment with and test all the major features of the [xAi API](https://github.com/xai/xai-sdk). Here you’ll find practical scripts demonstrating synchronous and asynchronous usage, tool integrations, function calling, and more.

---

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Examples](#examples)
  - [Basic Chat](#1-basic-chat)
  - [Tools Integration](#2-tools-integration)
  - [Function Calling](#3-function-calling)
  - [Async Requests](#4-async-requests)
- [Configuration](#configuration)
- [License](#license)

---

## Features

- Synchronous and asynchronous chat requests  
- System and user prompt support  
- API tool integrations: web search, X search, code execution  
- Function calling with parameter schemas  
- Token and usage reporting  
- Ready to hack, extend, and learn!

---

## Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/your-username/xai-playground.git
cd xai-playground
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API Key

Create a `.env` file in the project root:

```
XAI_API_KEY=your_xai_api_key_here
```

---

## Examples

### 1. Basic Chat

Interact with Grok-4 or Grok-4-fast using a simple user/system dialogue.

File: `main.py`

### 2. Tools Integration

Make use of built-in tools like web search and code execution.

File: `tools.py`

### 3. Function Calling

Test function calling with parameter schemas using Pydantic and custom tool definitions.

File: `function_calling.py`

### 4. Async Requests

Fire off multiple concurrent chat completions with async/await.

File: `async_requests.py`

---

## Configuration

- All behavior is driven by `.env` variables; your main requirement is a valid `XAI_API_KEY`.
- Adjust settings like model selection, timeout, and concurrency directly in the source files for quick experimenting.
- Extend or adapt the scripts to try custom tools or prompt engineering strategies.

---

## License

MIT

---

**Happy hacking!**  
Feel free to submit issues or PRs to expand the coverage of the playground.


