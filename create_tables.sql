-- create_tables.sql

-- Table: DailyItem
CREATE TABLE IF NOT EXISTS DailyItem (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT,
    InputType INTEGER
);

-- Table: DailyTask
CREATE TABLE IF NOT EXISTS DailyTask (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    DateCreation DATETIME,
    UserAddedItems TEXT -- Assuming JSON-like data stored as text
);

-- Table: TaskItemValue
CREATE TABLE IF NOT EXISTS TaskItemValue (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    ItemId INTEGER,
    DayId INTEGER,
    ValueTask TEXT -- Assuming long string data
);