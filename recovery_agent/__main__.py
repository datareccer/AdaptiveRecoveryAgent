import argparse
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path


def now():
    return datetime.now(timezone.utc).isoformat()


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save(path, data):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def new_case(args):
    case_id = uuid.uuid4().hex[:12]
    data = {
        "case_id": case_id,
        "created_at": now(),
        "provider": args.provider,
        "account": args.account,
        "attempts": [],
        "secrets_stored": False,
    }
    path = Path(args.output or f"cases/{case_id}.json")
    save(path, data)
    print(path)


def add_attempt(args):
    data = load(args.case)
    data.setdefault("attempts", []).append({
        "timestamp": now(),
        "method": args.method,
        "outcome": args.outcome,
        "notes": args.notes or "",
    })
    save(args.case, data)
    print(args.case)


def show(args):
    print(json.dumps(load(args.case), indent=2))


def main():
    parser = argparse.ArgumentParser(description="Adaptive Recovery Agent - safe recovery case manager")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("new-case")
    p.add_argument("--provider", required=True)
    p.add_argument("--account", required=True)
    p.add_argument("--output")
    p.set_defaults(func=new_case)

    p = sub.add_parser("add-attempt")
    p.add_argument("--case", required=True)
    p.add_argument("--method", required=True)
    p.add_argument("--outcome", required=True, choices=["pending", "success", "failed", "locked", "escalated"])
    p.add_argument("--notes")
    p.set_defaults(func=add_attempt)

    p = sub.add_parser("show")
    p.add_argument("--case", required=True)
    p.set_defaults(func=show)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
