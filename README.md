# Credit Rating Service API

## Overview
The Credit Rating Service API provides a RESTful endpoint for calculating credit ratings based on mortgage data. It is designed to validate input data and process risk factors using a modular design pattern for extensibility and maintainability.

## Features
- Modular risk score calculation using the Strategy design pattern.
- Input validation using Pydantic schemas.
- Error handling for validation and unexpected issues.
- Standardized API responses.

## Endpoints

### POST `/calculate_credit_rating`
Calculates the credit rating based on the provided mortgage data.

#### Request
- **Content-Type**: `application/json`

##### Example Request Body
```json
{
  "mortgages": [
    {
      "loan_amount": 250000,
      "property_value": 300000,
      "debt_amount": 50000,
      "annual_income": 75000,
      "credit_score": 720,
      "loan_type": "fixed",
      "property_type": "house"
    },
    {
      "loan_amount": 400000,
      "property_value": 500000,
      "debt_amount": 100000,
      "annual_income": 120000,
      "credit_score": 680,
      "loan_type": "variable",
      "property_type": "condo"
    }
  ]
}
```

#### Response
- **Status Code**: `200 OK`
- **Content-Type**: `application/json`

##### Example Success Response
```json
{
  "status": "success",
  "credit_rating": "BBB"
}
```

##### Example Error Responses
- **Validation Error**: `400 Bad Request`
```json
{
  "status": "error",
  "errors": [
    {
      "loc": ["mortgages", 0, "loan_amount"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

- **Unexpected Error**: `500 Internal Server Error`
```json
{
  "status": "error",
  "message": "An unexpected error occurred."
}
```

## Installation

### Prerequisites
- Python 3.12+
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/credit-rating-service.git
   cd credit-rating-service
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python main.py
   ```

## Testing
Run the test suite to ensure all components are functioning as expected:
```bash
pytest
```

## Architecture

### Core Modules
- **Risk Calculators**: Modular classes for calculating specific risk factors.
- **CreditRatingService**: Aggregates risk scores and determines credit ratings.

### API Layer
- Handles incoming requests, validates payloads, and returns appropriate responses.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any improvements or suggestions.

## Contact
For questions or support, please contact [your-email@example.com](mailto:your-email@example.com).

