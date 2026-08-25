# Adaptive Recovery Agent

**Digital Damage approved recovery workflow for authorized account and device recovery.**

Adaptive Recovery Agent is a documentation-first recovery assistant. It helps an authorized owner organize evidence, select official recovery paths, record attempts, and harden an account after recovery. It does **not** bypass authentication, defeat MFA, crack passwords, extract credentials, or unlock devices without authorization.

## What it does

- Guides recovery through the provider's official recovery process.
- Builds a local recovery case record without storing passwords or MFA secrets.
- Tracks recovery attempts and outcomes.
- Provides post-recovery security-hardening checklists.
- Keeps an auditable, reproducible workflow suitable for professional support work.

## What it does not do

- Password cracking or credential stuffing.
- MFA bypass or token theft.
- Security-question bypass.
- Session-cookie extraction.
- Device-lock bypass.
- Account takeover automation.

## Quick start

```bash
git clone https://github.com/datareccer/AdaptiveRecoveryAgent.git
cd AdaptiveRecoveryAgent
python3 -m recovery_agent --help
```

Python 3.11+ is recommended. The core workflow uses only the Python standard library.

## Case workflow

1. Confirm that the requester owns or is explicitly authorized to recover the account/device.
2. Create a case identifier.
3. Record only non-secret facts: provider, account identifier, date, known recovery channels, and outcome.
4. Open the provider's official recovery page manually.
5. Follow the provider's verification process.
6. Record the outcome without recording passwords, recovery codes, session tokens, or MFA seeds.
7. After successful recovery, change the password, enable MFA, review sessions, remove unknown devices/apps, and rotate exposed credentials.

## Commands

Create a case:

```bash
python3 -m recovery_agent new-case --provider google --account example@example.com
```

Record an attempt:

```bash
python3 -m recovery_agent add-attempt --case cases/<case-id>.json --method official-recovery --outcome pending
```

Show a case:

```bash
python3 -m recovery_agent show --case cases/<case-id>.json
```

## Data handling

Case files intentionally exclude passwords, MFA secrets, recovery codes, cookies, access tokens, and private keys. Treat case metadata as sensitive and store it with appropriate filesystem permissions.

## Provider guidance

For Google accounts, use the official Google Account Recovery flow: https://accounts.google.com/signin/recovery

For Microsoft accounts, use the official Microsoft account recovery flow: https://account.live.com/password/reset

For Apple Accounts, use the official Apple account recovery flow: https://iforgot.apple.com/

Never ask a user to send you their password, recovery code, authenticator seed, or session cookie.

## Testing

```bash
python3 -m unittest discover -s tests -v
```

## Digital Damage standard

A release is considered ready when it is reproducible, documented, testable, auditable, secret-safe, and incapable of silently bypassing an authentication control.
