import sqlite3

def game():
    connection = sqlite3.connect('game.db')
    cursor = connection.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS Solutions")
    cursor.execute("DROP TABLE IF EXISTS Guests")
    cursor.execute("DROP TABLE IF EXISTS FinancialRecords")
    cursor.execute("DROP TABLE IF EXISTS Interviews")
    cursor.execute("DROP TABLE IF EXISTS SecurityFootage")
    cursor.execute("DROP TABLE IF EXISTS DiaryEntries")
    cursor.execute("DROP TABLE IF EXISTS Messages")
    cursor.execute("DROP TABLE IF EXISTS Events")
    
    cursor.execute("""
    CREATE TABLE Solutions (
        SolutionID INTEGER PRIMARY KEY,
        GuestName VARCHAR(100),
        IsCorrect BOOLEAN
    )
    """)
    
    cursor.execute("""
    CREATE TABLE Guests (
        GuestID INTEGER PRIMARY KEY,
        Name VARCHAR(100),
        RelationshipToIsabella VARCHAR(100),
        Alibi TEXT,
        Motive TEXT
    )
    """)
    
    cursor.execute("""
    CREATE TABLE FinancialRecords (
        TransactionID INTEGER PRIMARY KEY,
        Date DATE,
        Amount DECIMAL(15, 2),
        Type VARCHAR(50),
        Description TEXT
    )
    """)
    
    cursor.execute("""
    CREATE TABLE Interviews (
        InterviewID INTEGER PRIMARY KEY,
        GuestID INTEGER,
        InterviewDate DATE,
        Transcript TEXT,
        FOREIGN KEY (GuestID) REFERENCES Guests(GuestID)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE SecurityFootage (
        FootageID INTEGER PRIMARY KEY,
        Timestamp DATETIME,
        EventDescription TEXT
    )
    """)
    
    cursor.execute("""
    CREATE TABLE DiaryEntries (
        EntryID INTEGER PRIMARY KEY,
        EntryDate DATE,
        EntryText TEXT
    )
    """)
    
    cursor.execute("""
    CREATE TABLE Messages (
        MessageID INTEGER PRIMARY KEY,
        SenderID INTEGER,
        ReceiverID INTEGER,
        MessageDate DATE,
        MessageContent TEXT,
        FOREIGN KEY (SenderID) REFERENCES Guests(GuestID),
        FOREIGN KEY (ReceiverID) REFERENCES Guests(GuestID)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE Events (
        EventID INTEGER PRIMARY KEY,
        EventDate DATE,
        EventDescription TEXT
    )
    """)
    
    cursor.execute("""
    INSERT INTO Guests (GuestID, Name, RelationshipToIsabella, Alibi, Motive) VALUES
    (1, 'Edgar Hawthorne', 'Father', 'At home office', 'Displeased with Isabella’s behavior'),
    (2, 'Lydia Hawthorne', 'Mother', 'Attending charity event', 'Secretive lately'),
    (3, 'James Hawthorne', 'Brother', 'Out of town', 'Financial issues'),
    (4, 'Claire Lawson', 'Best Friend', 'In the garden', 'Mysterious connection to rival business'),
    (5, 'Henry Whitaker', 'Business Associate', 'Talking to investors', 'Falling-out with Isabella'),
    (6, 'Tommy Clarkson', 'Neighbor', 'Grocery shopping', 'No known motive'),
    (7, 'Nancy Drew', 'Private Investigator', 'At her office', 'Investigating Isabella’s case'),
    (8, 'David Green', 'Gardener', 'Working in the garden', 'Suspiciously silent')
    """)
    
    cursor.execute("""
    INSERT INTO Solutions (SolutionID, GuestName, IsCorrect) VALUES
    (1, 'Edgar Hawthorne', False),
    (2, 'Lydia Hawthorne', False),
    (3, 'James Hawthorne', False),
    (4, 'Claire Lawson', False),
    (5, 'Henry Whitaker', True),
    (6, 'Tommy Clarkson', False),
    (7, 'Nancy Drew', False),
    (8, 'David Green', False)
    """)
    
    cursor.execute("""
    INSERT INTO FinancialRecords (TransactionID, Date, Amount, Type, Description) VALUES
    (1, '2022-05-20', 50000.00, 'Withdrawal', 'Large cash withdrawal by Lydia'),
    (2, '2022-05-21', 100000.00, 'Investment', 'Investment in a rival business by Henry'),
    (3, '2022-05-22', 2000.00, 'Withdrawal', 'Small withdrawal by James'),
    (4, '2022-05-23', 15000.00, 'Deposit', 'Deposit by Edgar for home improvements'),
    (5, '2022-05-24', 30000.00, 'Withdrawal', 'Unusual withdrawal by Claire'),
    (6, '2022-05-25', 5000.00, 'Transfer', 'Transfer between Lydia and David')
    """)
    
    cursor.execute("""
    INSERT INTO Interviews (InterviewID, GuestID, InterviewDate, Transcript) VALUES
    (1, 1, '2022-05-22', 'Edgar stated he was in his home office working on papers.'),
    (2, 2, '2022-05-22', 'Lydia mentioned attending a charity event but seemed nervous.'),
    (3, 3, '2022-05-22', 'James claimed to be out of town but his alibi needs verification.'),
    (4, 4, '2022-05-22', 'Claire was in the garden and had no solid alibi. She was nervous.'),
    (5, 5, '2022-05-22', 'Henry stated he was talking to investors, but his behavior was suspicious.'),
    (6, 6, '2022-05-23', 'Tommy mentioned being grocery shopping but couldn’t recall exact time.'),
    (7, 7, '2022-05-23', 'Nancy was at her office reviewing case files.'),
    (8, 8, '2022-05-23', 'David claimed to be working in the garden all day.')
    """)
    
    cursor.execute("""
    INSERT INTO SecurityFootage (FootageID, Timestamp, EventDescription) VALUES
    (1, '2022-05-21 22:00:00', 'Claire was seen near Isabella’s room.'),
    (2, '2022-05-21 23:00:00', 'Henry was seen leaving the estate suddenly.'),
    (3, '2022-05-21 22:30:00', 'James was not on camera, but was reportedly outside.'),
    (4, '2022-05-21 21:00:00', 'Tommy was seen entering a local grocery store.'),
    (5, '2022-05-22 00:00:00', 'Nancy was seen leaving her office late at night.'),
    (6, '2022-05-22 14:00:00', 'David was seen working in the garden.')
    """)
    
    cursor.execute("""
    INSERT INTO DiaryEntries (EntryID, EntryDate, EntryText) VALUES
    (1, '2022-05-19', 'I feel like everyone is watching me. I don’t know who to trust.'),
    (2, '2022-05-20', 'Received a threatening message today. I am scared.'),
    (3, '2022-05-21', 'Had a strange conversation with Henry. Something doesn’t add up.'),
    (4, '2022-05-22', 'Claire seemed very anxious today.'),
    (5, '2022-05-23', 'Edgar’s recent behavior is quite odd.'),
    (6, '2022-05-24', 'Saw Lydia arguing with someone at the charity event.')
    """)
    
    cursor.execute("""
    INSERT INTO Messages (MessageID, SenderID, ReceiverID, MessageDate, MessageContent) VALUES
    (1, 1, 4, '2022-05-20', 'I have had enough of your meddling. Stay away from the estate.'),
    (2, 2, 3, '2022-05-21', 'I know you’re struggling financially. Be careful.'),
    (3, 4, 5, '2022-05-21', 'We need to talk about your recent investments. Something doesn’t add up.'),
    (4, 5, 1, '2022-05-22', 'Henry expressed frustration about Edgar’s involvement.'),
    (5, 3, 2, '2022-05-23', 'James warned Lydia about Edgar’s suspicious activities.'),
    (6, 6, 7, '2022-05-23', 'Tommy asked Nancy for assistance with an investigation.')
    """)
    
    cursor.execute("""
    INSERT INTO Events (EventID, EventDate, EventDescription) VALUES
    (1, '2022-05-21', 'Isabella’s 25th birthday party. Many guests present.'),
    (2, '2022-05-21', 'Unscheduled security check performed.'),
    (3, '2022-05-22', 'Unusual activity detected in the east wing.'),
    (4, '2022-05-22', 'Grocery store robbery reported in town.'),
    (5, '2022-05-23', 'Nancy Drew holds a press conference about the case.'),
    (6, '2022-05-24', 'David found with missing tools in the garden.')
    """)
    
    connection.commit()
    connection.close()