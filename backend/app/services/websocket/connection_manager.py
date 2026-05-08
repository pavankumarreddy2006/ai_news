from fastapi import WebSocket
from starlette.websockets import WebSocketState


class ConnectionManager:
    def __init__(self) -> None:
        self.connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        if websocket in self.connections:
            self.connections.remove(websocket)

    async def broadcast(self, payload: dict) -> None:
        stale: list[WebSocket] = []
        for connection in self.connections:
            if connection.client_state != WebSocketState.CONNECTED:
                stale.append(connection)
                continue
            try:
                await connection.send_json(payload)
            except Exception:
                stale.append(connection)
        for connection in stale:
            self.disconnect(connection)


live_connection_manager = ConnectionManager()


class WorkflowState:
    def __init__(self) -> None:
        self.state = {
            "app_started": False,
            "database_ready": False,
            "telegram_ready": False,
            "scheduler_ready": False,
            "live_updates_ready": False,
            "keys_valid": False,
            "aggregation_ready": False,
            "last_refresh_at": None,
            "last_cleanup_at": None,
            "last_digest_at": None,
            "last_refresh_result": {},
            "last_cleanup_result": {},
            "last_digest_result": {},
            "source_health": [],
        }

    def update(self, **payload) -> dict:
        self.state.update(payload)
        return self.snapshot()

    def snapshot(self) -> dict:
        return dict(self.state)


workflow_state = WorkflowState()
