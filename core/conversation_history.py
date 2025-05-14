# core/conversation_history.py
import time
import uuid
import threading
import json
from flask import g 
from database.database import get_db 

class ConversationHistory:
    def __init__(self):
        # No longer holds data directly, interacts with DB via get_db()
        self._lock = threading.Lock() 
        print("--- CONV_HIST: Initialized (DB Interaction Mode) ---")

    def add_event(self, session_id: str, event_type: str, source: str, content: dict, metadata: dict = None):
        """Adds a structured event to the database for a specific session."""
        if not session_id:
             print("!!! ERROR [ConvHistory]: Attempted to add event without session_id.")
             return None

        event_id = str(uuid.uuid4())
        timestamp = int(time.time() * 1000) 
        metadata = metadata or {}

        db = get_db()
        try:
            db.execute(
                """
                INSERT INTO events (event_id, session_id, timestamp, event_type, source, content, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (event_id, session_id, timestamp, event_type, source, content, metadata) 
            )
            db.commit()
            print(f"HIST DB LOG [{session_id}]: [{event_type}] Source={source}") 

            return {
                "event_id": event_id,
                "session_id": session_id, 
                "timestamp": timestamp,
                "event_type": event_type,
                "source": source,
                "content": content,
                "metadata": metadata
            }
        except Exception as e:
            print(f"!!! ERROR [ConvHistory]: Failed to add event to DB for session {session_id}: {e}")
            db.rollback() 
            return None


    def get_history(self, session_id: str, count=None):
        """Retrieves event history for a specific session from the database."""
        if not session_id:
             print("!!! ERROR [ConvHistory]: Attempted to get history without session_id.")
             return []

        db = get_db()
        query = "SELECT event_id, session_id, timestamp, event_type, source, content, metadata FROM events WHERE session_id = ? ORDER BY timestamp ASC"
        params = [session_id]

        if count:
            pass 

        try:
            cursor = db.execute(query, params)
            
            history = [dict(row) for row in cursor.fetchall()]

            if count:
                return history[-count:] 
            else:
                return history
        except Exception as e:
            print(f"!!! ERROR [ConvHistory]: Failed to get history from DB for session {session_id}: {e}")
            return []


    def get_last_event(self, session_id: str):
         """Retrieves the most recent event for a specific session."""
         if not session_id:
             print("!!! ERROR [ConvHistory]: Attempted to get last event without session_id.")
             return None

         db = get_db()
         query = "SELECT event_id, session_id, timestamp, event_type, source, content, metadata FROM events WHERE session_id = ? ORDER BY timestamp DESC LIMIT 1"
         params = [session_id]
         try:
             cursor = db.execute(query, params)
             row = cursor.fetchone()
             return dict(row) if row else None
         except Exception as e:
             print(f"!!! ERROR [ConvHistory]: Failed to get last event from DB for session {session_id}: {e}")
             return None