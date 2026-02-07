# Adaptive Recovery Agent

This repository is a lightweight documentation hub for setting up a clean workspace, tracking dependencies, and safely guiding a Gmail account recovery process using **official Google flows**.

## 0) Scope and safety boundaries

This project does **not** include or support tooling intended to bypass security controls (for example, device unlockers, password cracking, or account compromise). If you need account access, follow the **official Google Account Recovery** process and associated security guidance below. This repo is intentionally documentation-only and focused on compliant recovery steps.

## 1) Dependency checklist

Use this checklist before you start:

- [ ] **Git** (version control)
- [ ] **GitHub account** (for hosting the repo)
- [ ] **Terminal** (macOS Terminal, Windows PowerShell, or Linux shell)
- [ ] **Nano** (terminal text editor; usually preinstalled on macOS/Linux)
- [ ] **Web browser** (for GitHub and Google Account Recovery)

Optional but helpful:

- [ ] **SSH keys** (recommended for GitHub authentication)
- [ ] **2FA app** (Google Authenticator or similar)

## 2) Set up Git and GitHub (easy steps)

### 2.1 Install Git

**macOS**

```bash
git --version
```

If Git is not installed, macOS will prompt you to install the Command Line Tools.

**Windows**

Download and install **Git for Windows** from https://git-scm.com/download/win.

**Linux (Debian/Ubuntu)**

```bash
sudo apt-get update
sudo apt-get install -y git
```

### 2.2 Configure Git (one-time)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 2.3 Create a GitHub account

1. Go to https://github.com and sign up.
2. Verify your email address.

### 2.4 Create and link the repository

```bash
mkdir AdaptiveRecoveryAgent
cd AdaptiveRecoveryAgent
git init
git remote add origin git@github.com:YOUR_USERNAME/AdaptiveRecoveryAgent.git
```

> If you prefer HTTPS, replace the remote URL with:
> `https://github.com/YOUR_USERNAME/AdaptiveRecoveryAgent.git`

### 2.5 First commit and push

```bash
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

## 3) Editing files with Nano (simple)

Open a file with Nano:

```bash
nano README.md
```

Nano tips:

- **Save**: press `CTRL + O`, then `Enter`
- **Exit**: press `CTRL + X`
- **Search**: press `CTRL + W`

## 4) Build instructions (current repo)

This repository is documentation-only, so there is **no build step** yet.

If you add code later, document it in this section using a simple checklist like:

- [ ] Install runtime dependencies
- [ ] Create required directories (for example, `mkdir -p app/src/main/res/xml`)
- [ ] Run `npm install` or `pip install -r requirements.txt`
- [ ] Run `npm run build` or `make build`

### 4.1 Example Android network security config (debug only)

If you add an Android app later, you may need a debug-only network security config.
Save it as `app/src/main/res/xml/network_security_config.xml`:

Then reference it from your `app/src/main/AndroidManifest.xml`:

```xml
<application
    android:allowBackup="true"
    android:icon="@mipmap/ic_launcher"
    android:label="@string/app_name"
    android:networkSecurityConfig="@xml/network_security_config"
    android:theme="@style/Theme.AppCompat.DayNight">
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <debug-overrides>
        <trust-anchors>
            <certificates src="user" />
        </trust-anchors>
    </debug-overrides>
    <base-config cleartextTrafficPermitted="true">
        <trust-anchors>
            <certificates src="system" />
            <certificates src="user" />
        </trust-anchors>
    </base-config>
</network-security-config>
```

## 5) How to use this tool to recover a Gmail account (safe + official)

**Important:** Only use official Google flows. Never share passwords, recovery codes, or 2FA secrets with anyone.

### 5.1 Official Google Account Recovery

1. Go to **https://accounts.google.com/signin/recovery**.
2. Enter your Gmail address.
3. Follow the prompts. Use a device and location you’ve used before if possible.
4. Provide any recovery email/phone you still control.
5. If asked, answer security questions as accurately as possible.

### 5.2 Increase your chances of success

- Use a **trusted device** and **usual Wi‑Fi network**.
- Try at a time when you typically access your account.
- If you recently changed your password, wait 24–72 hours.
- Check your recovery email/phone for verification codes.

### 5.3 If recovery fails

- Try again later from the same device and network.
- Use the **"Try another way"** option when offered.
- Make sure your recovery email/phone is still active.

### 5.4 After recovery (security hardening)

- Change your password to something **strong and unique**.
- Review **Account Security** at https://myaccount.google.com/security.
- Enable **2‑Step Verification** if not already enabled.
- Remove any unknown devices or third‑party app access.

---

## 6) Notes

This repository intentionally avoids any automation that could bypass or weaken account security. It is focused on **clear, safe instructions** and good security hygiene.
