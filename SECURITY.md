# Security Policy

## Supported Versions

This project is actively maintained. Please use the latest version from the `main` branch.

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability within this project, please follow these steps:

1. **Do NOT** open a public issue
2. Send an email to the repository owner or create a private security advisory on GitHub
3. Include the following information:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We will respond to security reports within 48 hours and will work with you to understand and resolve the issue promptly.

## Security Best Practices

When using this project:

1. **API Keys**: Never commit `.env` files or API keys to the repository
2. **Dependencies**: Keep dependencies updated to their latest secure versions
3. **Input Validation**: Be cautious when processing untrusted input (especially PDFs in Task 2)
4. **File Paths**: Validate file paths before processing to prevent directory traversal attacks

## Acknowledgments

We appreciate the security research community's efforts in responsibly disclosing vulnerabilities.
