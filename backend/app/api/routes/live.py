from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.services.websocket.connection_manager import live_connection_manager

router = APIRouter(prefix="/api/live", tags=["live"])


@router.get("")
def live_status():
    return {"status": "live", "connections": len(live_connection_manager.connections)}


async def live_socket(websocket: WebSocket):
    await live_connection_manager.connect(websocket)
    try:
        await websocket.send_json({"type": "connected", "payload": {"message": "Live AI updates channel connected."}})
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        live_connection_manager.disconnect(websocket)

