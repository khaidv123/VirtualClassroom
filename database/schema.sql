-- schema.sql
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS sessions;

CREATE TABLE sessions (
  session_id TEXT PRIMARY KEY,      
  user_name TEXT NOT NULL,          
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  problem_description TEXT,         
  current_phase_id TEXT,           
  metadata JSON_TEXT         
);

CREATE TABLE events (
  event_id TEXT PRIMARY KEY,        
  session_id TEXT NOT NULL,        
  timestamp INTEGER NOT NULL,      
  event_type TEXT NOT NULL,         -- e.g., 'new_message'
  source TEXT NOT NULL,           
  content JSON_TEXT NOT NULL,     
  metadata JSON_TEXT,         
  FOREIGN KEY (session_id) REFERENCES sessions (session_id)
);

-- Optional: Add indexes for faster querying
CREATE INDEX idx_events_session_id_timestamp ON events (session_id, timestamp);