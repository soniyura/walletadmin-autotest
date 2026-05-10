# AutoTestAdmin

Pytest + Playwright autotests for the admin panel.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install
```

Create `.env` from `.env.example` and fill local credentials:

```env
BASE_URL=https://example.com
ADMIN_USER=your_username
ADMIN_PASS=your_password
```

Never commit `.env` or real credentials.

## Run tests

Headless mode is the default:

```bash
pytest
```

For local debugging with a visible browser:

```bash
pytest --headed
```

## Allure report

```bash
pytest --alluredir=allure-results --clean-alluredir
allure serve allure-results
```

Install the Allure command-line tool separately if `allure` is not available in your shell.

## Useful Playwright command

```bash
python -m playwright codegen <url>
```
