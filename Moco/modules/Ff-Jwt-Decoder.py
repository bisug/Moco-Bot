from Moco import app
from pyrogram import filters
from pyrogram.enums import ParseMode
import re, json, jwt, base64
from datetime import datetime, timezone


def decode_segment(segment: str):
    """Base64 decode with padding and safe JSON parse"""
    segment += "=" * (-len(segment) % 4)
    try:
        return json.loads(base64.urlsafe_b64decode(segment).decode("utf-8"))
    except Exception:
        return {"error": "❌ Decode failed"}


def try_decode_jwt(token: str):
    """Decode JWT safely and determine validity"""
    try:
        header_seg, payload_seg, _ = token.split(".", 2)
    except ValueError:
        return {"error": "❌ Invalid JWT structure"}, {}, "❌ INVALID JWT TOKEN"

    header = decode_segment(header_seg)
    payload = decode_segment(payload_seg)

    # Merge verified payload (ignore signature)
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        if isinstance(decoded, dict):
            payload.update(decoded)
    except Exception:
        pass

    status = "✅ VALID (No Expiry Info)"
    if "exp" in payload:
        try:
            exp = datetime.fromtimestamp(int(payload["exp"]), tz=timezone.utc)
            payload["exp_readable"] = exp.strftime("%Y-%m-%d %H:%M:%S UTC")
            status = "✅ VALID JWT TOKEN" if exp > datetime.now(timezone.utc) else "❌ EXPIRED"
        except Exception:
            status = "⚠️ UNKNOWN EXP"

    return header, payload, status


@app.on_message(filters.command("decode", prefixes="/"))
async def decode_jwt_cmd(client, message):
    # Priority 1: replied message content
    token = None
    if message.reply_to_message:
        token = message.reply_to_message.text or message.reply_to_message.caption

    # Priority 2: argument after command
    if not token:
        parts = message.text.strip().split(maxsplit=1)
        if len(parts) > 1:
            token = parts[1].strip()

    if not token:
        return await message.reply_text(
            "⚠️ Usage:\n`/decode <jwt_token>`\nOr reply to a message containing a token.",
            quote=True,
        )

    header, payload, status = try_decode_jwt(token)

    # Format pretty JSON
    reply = (
        f"Free Fire JWT Decoder\n\n"
        f"JWT Status: {status}\n\n"
        f"Header:\n<pre>{json.dumps(header, indent=2, ensure_ascii=False)}</pre>\n\n"
        f"Payload:\n<pre>{json.dumps(payload, indent=2, ensure_ascii=False)}</pre>"
    )

    await message.reply_text(reply, parse_mode=ParseMode.HTML, quote=True)
