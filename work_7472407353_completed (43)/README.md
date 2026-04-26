# AI Personal Server & Dev Monitor

A self-hosted system for monitoring server health and AI-assisted insights.

## Project Structure
- `/backend`: FastAPI service, PostgreSQL, and Nginx configuration.
- `/agent`: Python-based system monitor for Linux servers.
- `/android`: Kotlin-based Android app with Material 3 UI.

## Installation Instructions

### 1. Backend
- Navigate to `/backend`.
- Run `docker-compose up -d`.
- API will be available at `http://localhost:8000`.

### 2. Server Agent
- Navigate to `/agent`.
- Run `bash install_agent.sh` to install as a systemd service.

### 3. Android App Build
- Navigate to `/android`.
- Ensure Java 17 is installed.
- Build APK: `./gradlew assembleDebug`.
- The APK will be located in `app/build/outputs/apk/debug/`.