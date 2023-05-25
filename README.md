

## Technology
- **Django**: The application is built using the Django web framework
- **Django Rest Framework**: API endpoints are created using Django Rest Framework
- **Celery**: Asynchronous task processing is handled using Celery
- **OpenAI API**: GPT-3.5-turbo is used for processing questions and generating standalone questions
- **Text-Embedding-ADA-002**: Text embeddings are created using OpenAI's text-embedding model
- **Pinecone**: Vector similarity search is performed using Pinecone.io
- **PostgresQL**: Default database for storing user and document information

## Installation
- Clone the repository:
```bash
git clone https://github.com/shamspias/document_ai_qa.git
```
- Create a virtual environment and activate it:
```bash
cd document_ai_qa
python -m venv venv
source venv/bin/activate
```
- Install the required dependencies:
```bash
pip install -r requirements.txt


## API Endpoints

The following API endpoints are available in the GPT-Powered-AI-Document-Chatbot-Creator application:

1. User registration

    - Endpoint: `/api/auth/register/`
    - Method: `POST`
    - Payload: `{ "username": "your_username", "password": "your_password", "email": "your_email@example.com" }`
    - Description: Register a new user account.

2. User login

    - Endpoint: `/api/auth/login/`
    - Method: `POST`
    - Payload: `{ "username": "your_username", "password": "your_password" }`
    - Description: Authenticate an existing user and return a JSON Web Token (JWT).

3. Upload a document

    - Endpoint: `/api/documents/`
    - Method: `POST`
    - Payload: `{"title": "document_title", "file": file_upload}`
    - Description: Upload a document file (PDF or other supported formats) for processing and indexing.

4. List all documents

    - Endpoint: `/api/documents/`
    - Method: `GET`
    - Description: Retrieve a list of all uploaded documents for the authenticated user.
   
5. Retrieve a document

    - Endpoint: `/api/documents/<document_id>/`
    - Method: `GET`
    - Description: Retrieve a specific document by ID.

6. Delete a document

    - Endpoint: `/api/documents/<document_id>/`
    - Method: `DELETE`
    - Description: Delete a specific document by ID.
   
7. Ask a question

   - Endpoint: `/api/questions/`
   - Method: `POST`
   - Payload: `{ "question": "your_question" }`
   - Description: Submit a question and receive an answer based on the content of the uploaded documents.
