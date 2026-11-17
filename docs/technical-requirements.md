# Technical requirements

These are the rules Kiro must follow in both parts of the workshop. The same rules are in each project's `.kiro/steering/tech.md`, so Kiro loads them automatically.

| Rule | Detail |
|---|---|
| Language | Python 3.12 |
| Architecture | Clean Architecture: domain, application (use cases), adapters |
| Testing | Test-Driven Development: write a failing test first, then make it pass, then refactor (red → green → refactor) |
| Tests | pytest |
| HTTP API | FastAPI, run locally with uvicorn |
| Storage | In-memory repository behind a repository interface (port) |
| Scope | One feature at a time; start with "add items to cart" |
| Running | Everything runs on your laptop. No cloud deployment. |

## Why an in-memory repository?

This version of the workshop runs entirely on your laptop. Keeping storage behind a repository interface means a real database (for example Amazon DynamoDB) can be added later as a new adapter, without changing the domain or the use cases.

## Adapted from

The AWS Code Challenge asks for Python, Clean Architecture, TDD, AWS CDK, API Gateway, Lambda and DynamoDB. This workshop keeps the first three and replaces the AWS hosting with a local FastAPI app and in-memory storage.

Source: AWS workshop *Kiro – Getting Started*, Code Challenge (catalog.workshops.aws/q-zero2hero/en-US/96-code-challenge).
