# Personal Finance Tracker

A comprehensive personal finance management application built in Python. Track your income, expenses, and generate detailed financial reports to better understand your spending habits and financial health.

## Features

### 💰 Transaction Management
- Record income and expenses with detailed categorization
- Support for multiple transaction types (deposits, withdrawals, transfers, payments)
- Automatic transaction validation and status tracking
- Bulk transaction import and export capabilities

### 👤 User Management
- Multi-user support with secure profile management
- User authentication and account activation/deactivation
- Email validation and profile customization

### 📊 Financial Reporting
- Generate comprehensive financial reports
- Track spending patterns and trends
- Calculate averages, totals, and percentage changes
- Export reports to text files for record keeping

### 🔧 Utility Functions
- Robust file handling with error management
- Mathematical calculations for financial metrics
- Data persistence and backup capabilities

## Quick Start

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd personal-finance-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. **Run the application:**
```bash
python src/main.py
```

2. **Run tests:**
```bash
python -m unittest discover tests -v
```

3. **Run specific test modules:**
```bash
python tests/test_utils.py
python tests/test_services.py
```

## Example Usage

The application will automatically:
- Load sample user data and transactions
- Generate comprehensive financial reports
- Save reports to `user_report.txt` and `transaction_summary.txt`
- Demonstrate mathematical calculations for financial metrics

## Sample Output

```
Starting Personal Finance Tracker...
Loaded 5 users and 15 transactions
Sample calculation: (10 + 5) * 2 = 30
Successfully wrote file: user_report.txt
Successfully wrote file: transaction_summary.txt
Personal Finance Tracker completed successfully!
```

## Technical Details

### Dependencies
- **Python 3.7+**: Core runtime
- **pytest**: Testing framework
- **black**: Code formatting (development)
- **flake8**: Code linting (development)
- **mypy**: Type checking (development)

### Architecture
- **Models**: Define core data structures (User, Transaction)
- **Services**: Business logic for data management and reporting
- **Utils**: Reusable utility functions for file operations and calculations
- **Tests**: Comprehensive unit test coverage

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`python -m unittest discover tests`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue on the GitHub repository or contact the development team.
Hello from GitHub Actions 🚀

Message: Hello from GitHub Actions 🚀
Reversed PAT (safe for testing): BjRzURooQDXIR2IH20ClWhXM2smhItdhfQeOFlrv08waB6DWSN7JJ29wE0D_LSwrxfsPpd3Y0IR5FREB11_tap_buhtig
