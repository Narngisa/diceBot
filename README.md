# 🎲 Dice Bot Discord

[![CI](https://github.com/Narngisa/diceBot/actions/workflows/ci.yml/badge.svg)](https://github.com/Narngisa/diceBot/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-v2.7.1-5865F2?logo=discord&logoColor=white)](https://discordpy.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern, modular Discord bot designed for Tabletop Role-Playing Games (TTRPGs) like **Dungeons & Dragons (D&D 5e)**. Built with `discord.py` slash commands (App Commands) and a dynamic Cog architecture, it makes rolling dice in Discord fast, clear, and effortless.

---

## 📸 Preview

<p align="center">
  <img width="420" alt="Dice Bot Preview" src="https://github.com/user-attachments/assets/b1345e8f-bd97-440a-8346-1f3cd26c0577" />
</p>

---

## ✨ Features

- 🎲 **Single Die Rolling (`/dice`)**: Roll standard RPG dice (`d2`, `d3`, `d4`, `d6`, `d8`, `d10`, `d12`, `d20`, `d100`) with custom modifiers.
- 🎯 **Multi-Dice Rolling (`/roll`)**: Roll batches of up to 100 dice simultaneously with total sum and breakdown.
- ⚔️ **Advantage & Disadvantage (`/adv`)**: Automatically rolls 2d20, selects the highest/lowest result, adds your modifier, and formats the output.
- 🛡️ **Saving Throws (`/saving`)**: Dedicated saving throw command for core D&D 5e abilities (`STR`, `DEX`, `CON`, `INT`, `WIS`, `CHA`).
- 👑 **Critical Success & Failure Detection**: Automatic highlighting and colored embed alerts for Natural 20s (Gold / 👑) and Natural 1s (Red / 💀).
- 🔄 **Hot-Reload System (`/reload`)**: Admin command to live-reload extensions and sync slash commands without restarting the bot process.
- ⚡ **Instant Guild Sync**: Registers slash commands directly to your target guild for instantaneous availability without waiting for global cache propagation.

---

## 📜 Slash Commands Reference

| Command | Arguments | Description | Example |
|---|---|---|---|
| `/dice` | `dice` *(Choice)*, `modifiers` *(Integer)* | Rolls a single die from d2 to d100 with modifier. | `/dice dice: 1d20 modifiers: 3` |
| `/roll` | `amount` *(1-100)*, `roll` *(Choice)*, `modifiers` *(Integer)* | Rolls multiple dice of the chosen type and calculates total. | `/roll amount: 4 roll: d6 modifiers: 2` |
| `/adv` | `dice` *("Advantage" \| "Disadvantage")*, `modifiers` *(Integer)* | Rolls 2d20 and takes the higher or lower value. | `/adv dice: Advantage modifiers: 5` |
| `/saving` | `ability` *("STR" \| "DEX" \| "CON" \| "INT" \| "WIS" \| "CHA")*, `modifiers` *(Integer)* | Rolls a d20 saving throw for a specified ability. | `/saving ability: DEX modifiers: 4` |
| `/ping` | *None* | Checks the bot's WebSocket latency in milliseconds. | `/ping` |
| `/help` | *None* | Displays a list of all registered slash commands in the server. | `/help` |
| `/reload` | *None* *(Admin Only)* | Reloads all Cogs and re-syncs slash commands to the server. | `/reload` |

---

## 📁 Project Structure

```text
diceBot/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI workflow (linting, tests)
├── cogs/                   # Modular command extensions (Cogs)
│   ├── adv.py              # Advantage / Disadvantage command
│   ├── dice.py             # Single die roll command
│   ├── help.py             # Dynamic help menu command
│   ├── ping.py             # Bot latency ping command
│   ├── roll.py             # Multi-dice roll command
│   └── saving.py           # D&D ability saving throw command
├── .env.example            # Environment variable template
├── .gitignore              # Git ignore rules
├── bot.py                  # Bot entrypoint & Cog loader
├── LICENSE                 # Project license
├── README.md               # Project documentation
└── requirements.txt        # Python package dependencies
```

---

## 🚀 Getting Started

### 1. Prerequisites

- **Python 3.10+** (Python 3.11 or 3.12 recommended)
- A **Discord Account** and a Discord Server where you have administrator permissions.

---

### 2. Discord Application Setup

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications/) and click **New Application**.
2. Navigate to the **Bot** tab on the left:
   - Click **Add Bot** (or **Reset Token**) to generate your **Bot Token**. Copy this token for later.
   - Under **Privileged Gateway Intents**, enable **Message Content Intent**.
3. Navigate to **OAuth2** > **URL Generator**:
   - Under **Scopes**, check `bot` and `applications.commands`.
   - Under **Bot Permissions**, select `Send Messages`, `Embed Links`, `Read Message History`, and `Use Slash Commands`.
   - Copy the generated URL at the bottom and open it in your browser to invite the bot to your server.
4. Enable **Developer Mode** in Discord (`User Settings` > `Advanced` > `Developer Mode`), then right-click your Discord server name and select **Copy Server ID** (`GUILD_ID`).

---

### 3. Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Narngisa/diceBot.git
   cd diceBot
   ```

2. **Create a virtual environment:**
   ```bash
   # Windows (Command Prompt / PowerShell)
   python -m venv venv

   # macOS / Linux
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD):**
     ```cmd
     .\venv\Scripts\activate.bat
     ```
   - **macOS / Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables:**
   Copy `.env.example` to `.env`:
   ```bash
   # Windows PowerShell
   Copy-Item .env.example .env

   # macOS / Linux / Bash
   cp .env.example .env
   ```
   Open `.env` in your text editor and fill in your values:
   ```env
   TOKEN=your_bot_token_here
   GUILD_ID=your_discord_server_id_here
   ```

---

### 4. Running the Bot

Run the bot script:
```bash
python bot.py
```

When started successfully, the console will output:
```text
Successfully: adv.py
Successfully: dice.py
Successfully: help.py
Successfully: ping.py
Successfully: roll.py
Successfully: saving.py
Synced: 7 command(s) to Guild ID: 123456789012345678
Successfully logged in as YourBotName#0000 !!
```

---

## 🛠️ Development & CI

This repository includes a continuous integration (CI) pipeline via **GitHub Actions** located at [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

The workflow automatically validates:
- Python syntax (`compileall`) across Python 3.10, 3.11, and 3.12
- Code linting with Flake8
- Cog module import integrity

To run checks locally:
```bash
# Verify Python syntax
python -m compileall bot.py cogs/

# Run flake8 linting
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
