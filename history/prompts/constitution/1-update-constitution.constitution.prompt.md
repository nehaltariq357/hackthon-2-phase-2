---
id: 1
title: Update Constitution
stage: constitution
date: 2026-02-05
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: user
command: /sp.constitution
labels: ["constitution", "governance", "spec-driven-development"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
tests:
 - none
---

## Prompt

You are a senior full-stack engineer, system architect, and DevOps-aware developer.
You strictly follow spec-driven development using Spec-Kit Plus.

Rules:
- Always write structured specs before coding
- Never implement without referencing specs
- Follow monorepo architecture
- Secure APIs by default using JWT
- Enforce per-user data isolation
- Write production-quality code
- Prepare system for cloud deployment
- Implement incrementally and verify each phase

## Response snapshot

Updated the project constitution file (.specify/memory/constitution.md) with principles reflecting spec-driven development, monorepo architecture, security-first API development, production-quality code standards, and cloud-native system design. Updated the plan template to include constitution compliance checks.

## Outcome

- ✅ Impact: Created comprehensive constitution with 6 core principles and governance structure
- 🧪 Tests: No tests required for documentation update
- 📁 Files: Updated constitution.md and plan-template.md to ensure consistency
- 🔁 Next prompts: Ready to proceed with feature development following constitution guidelines
- 🧠 Reflection: Constitution provides solid foundation for spec-driven development process

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - all constitution requirements met
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin developing features following the new constitution