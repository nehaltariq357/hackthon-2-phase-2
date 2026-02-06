# Data Model: Todo App Implementation

**Feature**: Todo App Spec | **Date**: 2026-02-05

## Entity Definitions

### User Entity
**Description**: Represents an authenticated user in the system
**Fields**:
- `id` (UUID/Integer): Unique identifier for the user (primary key)
- `email` (String): User's email address (unique, required, valid email format)
- `hashed_password` (String): Bcrypt-hashed password (required, secure storage)
- `created_at` (DateTime): Timestamp of account creation (auto-generated)
- `updated_at` (DateTime): Timestamp of last update (auto-generated)
- `is_active` (Boolean): Account status flag (default: True)

**Relationships**:
- One-to-Many: User has many Tasks
- Validations: Email format validation, password strength requirements

**State Transitions**:
- Inactive → Active (upon registration verification)
- Active → Inactive (upon account deactivation)

### Task Entity
**Description**: Represents a user's personal task with status and metadata
**Fields**:
- `id` (UUID/Integer): Unique identifier for the task (primary key)
- `user_id` (UUID/Integer): Foreign key linking to the owning user (required)
- `title` (String): Task title or description (required, max 200 characters)
- `description` (Text): Detailed task description (optional, max 1000 characters)
- `status` (Enum: 'pending', 'in_progress', 'completed'): Task completion status (default: 'pending')
- `priority` (Enum: 'low', 'medium', 'high'): Task priority level (default: 'medium')
- `due_date` (DateTime): Optional deadline for the task (nullable)
- `created_at` (DateTime): Timestamp of task creation (auto-generated)
- `updated_at` (DateTime): Timestamp of last modification (auto-generated)
- `completed_at` (DateTime): Timestamp when task was marked complete (nullable)

**Relationships**:
- Many-to-One: Task belongs to one User (user_id → users.id)
- Validations: Title required, status must be valid enum value, due_date in future if provided

**State Transitions**:
- pending → in_progress (when user starts working on task)
- in_progress → pending (when user pauses/returns to pending)
- pending → completed (when user marks task as done)
- in_progress → completed (when user finishes task)
- completed → pending (when user reopens task)

## Indexes

### User Table
- `idx_users_email`: Unique index on email for fast lookups and uniqueness enforcement
- `idx_users_created_at`: Index on created_at for sorting and time-based queries

### Task Table
- `idx_tasks_user_id`: Index on user_id for efficient user-specific queries
- `idx_tasks_status`: Index on status for filtering by task status
- `idx_tasks_due_date`: Index on due_date for deadline-based queries
- `idx_tasks_created_at`: Index on created_at for chronological sorting
- `idx_tasks_priority`: Index on priority for priority-based sorting

## Database Constraints

### User Constraints
- `users_email_unique`: UNIQUE constraint on email column
- `users_email_not_null`: NOT NULL constraint on email column
- `users_password_not_null`: NOT NULL constraint on hashed_password column

### Task Constraints
- `fk_tasks_user_id`: FOREIGN KEY constraint linking user_id to users.id
- `tasks_title_not_null`: NOT NULL constraint on title column
- `tasks_user_id_not_null`: NOT NULL constraint on user_id column
- `chk_tasks_valid_status`: CHECK constraint to ensure status is one of the allowed enum values
- `chk_tasks_valid_priority`: CHECK constraint to ensure priority is one of the allowed enum values
- `chk_tasks_due_date_future`: CHECK constraint to ensure due_date is not in the past (if implemented)

## Relationship Mapping

### User-Task Relationship
- One User can have many Tasks (1:N relationship)
- Cascade delete: When a user is deleted, all their tasks should be deleted
- Foreign key constraint ensures referential integrity
- User ID stored as user_id in tasks table

## Validation Rules

### User Validation
- Email: Must be valid email format and unique across all users
- Password: Must meet minimum security requirements (length, complexity) before hashing
- Account status: Must be either active or inactive

### Task Validation
- Title: Required field, maximum length of 200 characters
- Status: Must be one of 'pending', 'in_progress', 'completed'
- Priority: Must be one of 'low', 'medium', 'high'
- Ownership: Tasks can only be created/accessed by the owning user
- Due date: If provided, should be a valid future date (optional business rule)

## Data Access Patterns

### User Queries
- Find user by email (authentication)
- Verify user credentials (login)
- Get user profile information

### Task Queries
- Get all tasks for a specific user
- Get tasks filtered by status
- Get tasks filtered by priority
- Get tasks due by a certain date
- Search tasks by title/description (partial match)
- Get single task by ID (with user ownership verification)

## Data Migration Considerations

### Initial Schema
- Create users table with all required fields and constraints
- Create tasks table with all required fields and constraints
- Establish foreign key relationship between tables
- Create all necessary indexes

### Future Extensions
- Tags table for task categorization (many-to-many relationship with tasks)
- Task comments/revisions table for collaborative features
- Settings/preferences table for user customization