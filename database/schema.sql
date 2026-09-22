-- Sports Hub PostgreSQL schema
-- Run against a dedicated database. Do not store credentials in this file.

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    display_name VARCHAR(120) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'visitor'
        CHECK (role IN ('visitor', 'admin')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    slug VARCHAR(80) UNIQUE NOT NULL,
    name VARCHAR(120) NOT NULL,
    description TEXT NOT NULL,
    icon VARCHAR(80)
);

CREATE TABLE IF NOT EXISTS sports (
    id SERIAL PRIMARY KEY,
    slug VARCHAR(80) UNIQUE NOT NULL,
    name VARCHAR(120) NOT NULL,
    tagline VARCHAR(255) NOT NULL,
    overview TEXT NOT NULL,
    history TEXT NOT NULL,
    player_count TEXT NOT NULL,
    court_dimensions TEXT NOT NULL,
    scoring_system TEXT NOT NULL,
    governing_org VARCHAR(255) NOT NULL,
    featured BOOLEAN NOT NULL DEFAULT FALSE,
    popular BOOLEAN NOT NULL DEFAULT FALSE,
    icon VARCHAR(80),
    accent_color VARCHAR(16),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS sport_categories (
    sport_id INTEGER NOT NULL REFERENCES sports(id) ON DELETE CASCADE,
    category_id INTEGER NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
    PRIMARY KEY (sport_id, category_id)
);

CREATE TABLE IF NOT EXISTS rules (
    id SERIAL PRIMARY KEY,
    sport_id INTEGER NOT NULL REFERENCES sports(id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    sort_order INTEGER NOT NULL DEFAULT 0,
    content TEXT NOT NULL,
    content_type VARCHAR(40) NOT NULL DEFAULT 'educational'
        CHECK (content_type IN ('educational', 'official_summary', 'training', 'safety')),
    source_org VARCHAR(255),
    rule_edition VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS equipment (
    id SERIAL PRIMARY KEY,
    sport_id INTEGER NOT NULL REFERENCES sports(id) ON DELETE CASCADE,
    name VARCHAR(200) NOT NULL,
    purpose TEXT NOT NULL,
    specifications TEXT,
    safety_considerations TEXT,
    icon VARCHAR(80),
    sort_order INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS techniques (
    id SERIAL PRIMARY KEY,
    sport_id INTEGER NOT NULL REFERENCES sports(id) ON DELETE CASCADE,
    name VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    steps JSONB NOT NULL DEFAULT '[]'::jsonb,
    beginner_tips TEXT,
    common_mistakes TEXT,
    safety_reminders TEXT,
    sort_order INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS safety_guidelines (
    id SERIAL PRIMARY KEY,
    sport_id INTEGER REFERENCES sports(id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    topic VARCHAR(80) NOT NULL,
    sort_order INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS terminology (
    id SERIAL PRIMARY KEY,
    sport_id INTEGER NOT NULL REFERENCES sports(id) ON DELETE CASCADE,
    term VARCHAR(160) NOT NULL,
    definition TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS faqs (
    id SERIAL PRIMARY KEY,
    sport_id INTEGER NOT NULL REFERENCES sports(id) ON DELETE CASCADE,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    sort_order INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS references_sources (
    id SERIAL PRIMARY KEY,
    sport_id INTEGER REFERENCES sports(id) ON DELETE CASCADE,
    organization VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    edition_year VARCHAR(80),
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS player_positions (
    id SERIAL PRIMARY KEY,
    sport_id INTEGER NOT NULL REFERENCES sports(id) ON DELETE CASCADE,
    name VARCHAR(160) NOT NULL,
    description TEXT NOT NULL,
    sort_order INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS fouls_violations (
    id SERIAL PRIMARY KEY,
    sport_id INTEGER NOT NULL REFERENCES sports(id) ON DELETE CASCADE,
    name VARCHAR(160) NOT NULL,
    description TEXT NOT NULL,
    kind VARCHAR(40) NOT NULL DEFAULT 'violation'
        CHECK (kind IN ('foul', 'violation', 'signal')),
    sort_order INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS bookmarks (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    sport_id INTEGER NOT NULL REFERENCES sports(id) ON DELETE CASCADE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE (user_id, sport_id)
);

CREATE INDEX IF NOT EXISTS idx_rules_sport ON rules(sport_id);
CREATE INDEX IF NOT EXISTS idx_equipment_sport ON equipment(sport_id);
CREATE INDEX IF NOT EXISTS idx_techniques_sport ON techniques(sport_id);
CREATE INDEX IF NOT EXISTS idx_terminology_sport ON terminology(sport_id);
CREATE INDEX IF NOT EXISTS idx_faqs_sport ON faqs(sport_id);
CREATE INDEX IF NOT EXISTS idx_sports_name ON sports(name);
CREATE INDEX IF NOT EXISTS idx_terminology_term ON terminology(term);

CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX IF NOT EXISTS idx_sports_name_trgm ON sports USING gin (name gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_terminology_trgm ON terminology USING gin (term gin_trgm_ops);
