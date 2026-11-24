# Requirements: Submit and list ideas

## Introduction
Staff submit an idea with a title and a description and get the stored idea back. Anyone can list all ideas, newest first. This spec covers submitting and listing only. Opening one idea is a separate spec.

## Glossary
- **Idea**: a title and a description, with an `idea_id` and a `created_at` time set by the service.
- **Idea list**: every stored idea, newest first.
- **Newest first**: the idea submitted last comes first.

## Requirement 1: Submit an idea
**Goal:** staff can send an idea and see it stored exactly as they wrote it.

**Acceptance criteria**
1. WHEN someone submits a title of 1 to 100 characters that is not only spaces, and a description of 1 to 1000 characters, THE SYSTEM SHALL store the idea and return it with status 201.
2. WHEN an idea is stored THE SYSTEM SHALL give it a new `idea_id` and set `created_at` to the current UTC time, ending in `Z`.
3. WHEN an idea is stored THE SYSTEM SHALL keep the title and description exactly as sent.

## Requirement 2: List ideas
**Goal:** anyone can see every idea, the latest at the top.

**Acceptance criteria**
1. WHEN someone requests the list THE SYSTEM SHALL return every idea, newest first.
2. WHEN the list is returned THE SYSTEM SHALL include the number of ideas as `count`.
3. WHEN an idea is returned THE SYSTEM SHALL include its `idea_id`, `title`, `description` and `created_at`.
4. WHEN no ideas exist THE SYSTEM SHALL return an empty list with `count` 0.

## Requirement 3: Reject bad input
**Goal:** the list never holds an idea nobody can read.

**Acceptance criteria**
1. IF the title is empty, only spaces or longer than 100 characters THEN THE SYSTEM SHALL return a validation error and store nothing.
2. IF the description is missing, empty or longer than 1000 characters THEN THE SYSTEM SHALL return a validation error and store nothing.

## Out of scope
Opening one idea, voting, comments, editing, deleting, categories, authors, login, persistent storage.
