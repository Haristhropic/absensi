from datetime import date, datetime
from zoneinfo import ZoneInfo

from flask import Flask, jsonify, request

app = Flask(__name__)

WIB = ZoneInfo("Asia/Jakarta")
BASE_DATE = date(2026, 1, 1)
LEMDIK_ID = 4


def _parse_date_param(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def _resolve_wib_day():
    """Return (wib_date, created_at). ?date=YYYY-MM-DD overrides the date part (QA rollover simulation)."""
    now = datetime.now(WIB)
    raw = request.args.get("date")
    if raw:
        parsed = _parse_date_param(raw)
        if parsed is None:
            return None, None
        created_at = "%s %s" % (parsed.isoformat(), now.strftime("%H:%M:%S"))
        return parsed, created_at
    return now.date(), now.strftime("%Y-%m-%d %H:%M:%S")


def _payload(wib_date, created_at, id_value, type_label):
    return {"id": id_value, "lemdikId": LEMDIK_ID, "createdAt": created_at, "type": type_label}


@app.get("/api/qr-datang")
def qr_datang():
    wib_date, created_at = _resolve_wib_day()
    if wib_date is None:
        return jsonify({"error": "Invalid ?date=, expected YYYY-MM-DD"}), 400
    days = (wib_date - BASE_DATE).days
    return jsonify(_payload(wib_date, created_at, 3290 + days, "QR Datang"))


@app.get("/api/qr-pulang")
def qr_pulang():
    wib_date, created_at = _resolve_wib_day()
    if wib_date is None:
        return jsonify({"error": "Invalid ?date=, expected YYYY-MM-DD"}), 400
    days = (wib_date - BASE_DATE).days
    return jsonify(_payload(wib_date, created_at, 3374 + days, "QR Pulang"))


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})
