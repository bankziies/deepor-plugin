"""
Deepor MCP Translation Server
Translates Thai text to English for Claude Code via an external model backend.

Supported backends (set via TRANSLATE_BACKEND in .env):
  openai     — OpenAI API (default: gpt-4o-mini)
  anthropic  — Anthropic API (claude-haiku-4-5)
  ollama     — Local Ollama instance
  deepl      — DeepL Translation API

All secrets are loaded from a .env file next to this script.
See .env.example for required variables per backend.
Never put API keys in settings.json or any version-controlled file.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load .env from the same directory as this script
load_dotenv(Path(__file__).parent / ".env")

mcp = FastMCP("deepor-translate")


# ---------------------------------------------------------------------------
# Prompt builder
# ---------------------------------------------------------------------------

_SYSTEM_PROMPT = (
    "You are a precise Thai-to-English technical translator for software development tasks. "
    "Translate the user's Thai instruction into clear, actionable English. "
    "Rules: "
    "(1) Translate meaning, not words — Thai often omits subjects; add them explicitly. "
    "(2) Keep all technical terms unchanged: function names, file paths, error messages, package names. "
    "(3) Make vague phrases concrete based on context (e.g. 'ทำให้ดีขึ้น' → 'Refactor for readability'). "
    "(4) Do NOT add requirements or assumptions not present in the original. "
    "(5) Output only the English translation — no explanation, no prefix."
)

_MODE_INSTRUCTIONS = {
    "concise": "Translate concisely — remove filler words, keep all constraints.",
    "full":    "Translate fully — preserve every nuance, may be longer than original.",
    "short":   "Translate in 1-2 sentences — omit unnecessary context.",
}


def _build_user_prompt(text: str, mode: str) -> str:
    instruction = _MODE_INSTRUCTIONS.get(mode, _MODE_INSTRUCTIONS["concise"])
    return f"{instruction}\n\nThai input:\n{text}"


# ---------------------------------------------------------------------------
# Backend implementations
# ---------------------------------------------------------------------------

def _translate_openai(text: str, mode: str) -> str:
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user",   "content": _build_user_prompt(text, mode)},
        ],
        temperature=0.1,
        max_tokens=1024,
    )
    return response.choices[0].message.content.strip()


def _translate_anthropic(text: str, mode: str) -> str:
    import anthropic

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    model = os.environ.get("ANTHROPIC_MODEL", "claude-haiku-4-5-20251001")

    message = client.messages.create(
        model=model,
        max_tokens=1024,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": _build_user_prompt(text, mode)}],
    )
    return message.content[0].text.strip()


def _translate_ollama(text: str, mode: str) -> str:
    import requests

    base_url = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
    model = os.environ.get("OLLAMA_MODEL", "llama3.2")

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user",   "content": _build_user_prompt(text, mode)},
        ],
        "stream": False,
        "options": {"temperature": 0.1},
    }
    response = requests.post(f"{base_url}/api/chat", json=payload, timeout=60)
    response.raise_for_status()
    return response.json()["message"]["content"].strip()


def _translate_deepl(text: str, mode: str) -> str:  # noqa: ARG001 — mode unused for DeepL
    import requests

    api_key = os.environ["DEEPL_API_KEY"]
    free_api = os.environ.get("DEEPL_FREE_API", "false").lower() == "true"
    endpoint = (
        "https://api-free.deepl.com/v2/translate"
        if free_api
        else "https://api.deepl.com/v2/translate"
    )

    response = requests.post(
        endpoint,
        headers={"Authorization": f"DeepL-Auth-Key {api_key}"},
        json={"text": [text], "source_lang": "TH", "target_lang": "EN"},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["translations"][0]["text"].strip()


# ---------------------------------------------------------------------------
# Backend router
# ---------------------------------------------------------------------------

_BACKENDS = {
    "openai":    _translate_openai,
    "anthropic": _translate_anthropic,
    "ollama":    _translate_ollama,
    "deepl":     _translate_deepl,
}


def _get_backend():
    name = os.environ.get("TRANSLATE_BACKEND", "openai").lower()
    fn = _BACKENDS.get(name)
    if fn is None:
        raise ValueError(
            f"Unknown TRANSLATE_BACKEND '{name}'. "
            f"Choose one of: {', '.join(_BACKENDS)}"
        )
    return name, fn


# ---------------------------------------------------------------------------
# MCP tool
# ---------------------------------------------------------------------------

@mcp.tool()
def translate_thai(text: str, mode: str = "concise") -> str:
    """Translate Thai text to English for Claude Code execution.

    Args:
        text: Thai text to translate.
        mode: Translation detail level — concise | full | short.

    Returns:
        English translation ready for Claude Code to execute.
    """
    if not text or not text.strip():
        return ""

    valid_modes = ("concise", "full", "short")
    if mode not in valid_modes:
        mode = "concise"

    backend_name, backend_fn = _get_backend()

    try:
        result = backend_fn(text.strip(), mode)
        return result
    except KeyError as exc:
        missing_var = str(exc).strip("'")
        raise RuntimeError(
            f"Backend '{backend_name}' requires environment variable {missing_var}. "
            "Set it in your MCP server configuration."
        ) from exc


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run()
