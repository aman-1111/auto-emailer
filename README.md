# 📧 Auto Emailer

Auto Emailer is a Python-based utility that automates the sending of emails via SMTP. It's designed for sending scheduled or bulk emails using customizable templates and recipient lists. This tool is ideal for sending newsletters, reports, alerts, or any recurring emails with minimal effort.

## 🚀 Features

- Send emails using SMTP (Gmail, Outlook, etc.)
- Support for plain text and HTML content
- Dynamic email body templating
- Read recipients from CSV or JSON
- Logging of email delivery status
- Schedule email jobs (using `schedule` or cron)
- Environment variable support for secure credentials

## 📦 Tech Stack

- Python 3.x
- `smtplib`, `email`, `ssl`
- `pandas` (optional, for handling recipient lists)
- `schedule` (optional, for time-based automation)

## 🛠 Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/auto-emailer.git
cd auto-emailer

2. Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies

pip install -r requirements.txt

4. Configure your environment

Create a .env file (or edit config in the script) with the following details:

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=465
EMAIL_ADDRESS=your-email@example.com
EMAIL_PASSWORD=your-app-password

5. Prepare recipients

Create a CSV file named recipients.csv like this:

name,email
John Doe,john@example.com
Jane Smith,jane@example.com

6. Run the script

python auto_emailer.py

Or if scheduled:

python scheduler.py

📄 Example Email Template

You can use a .html or .txt file as a message body:

<!DOCTYPE html>
<html>
<body>
  <p>Hello {{name}},</p>
  <p>This is your scheduled update.</p>
</body>
</html>

The script will replace {{name}} with values from the CSV.
🛡️ Security Note

Use App Passwords instead of real email passwords. Avoid committing .env files to version control.
📝 License

MIT License
