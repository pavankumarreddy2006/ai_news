# Architecture Overview

## Backend

- `app/core`: configuration, logging, security, constants
- `app/database`: models, schemas, repositories, session
- `app/services`: aggregators, ranking, summarization, analytics, telegram, websocket
- `app/schedulers`: refresh, cleanup, telegram digest jobs
- `app/api`: routes, middleware, dependencies

## Frontend

- `src/app`: app bootstrapping
- `src/components`: reusable UI, layout, cards, dashboard widgets
- `src/features`: query hooks and domain-level feature modules
- `src/pages`: route-level composition
- `src/store`: cross-app state

