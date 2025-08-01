import sqlite3


def game():
    connection = sqlite3.connect("game2.db")
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Solutions")
    cursor.execute("DROP TABLE IF EXISTS Suspects")
    cursor.execute("DROP TABLE IF EXISTS Articles")
    cursor.execute("DROP TABLE IF EXISTS PhoneRecords")
    cursor.execute("DROP TABLE IF EXISTS OfficeLogs")
    cursor.execute("DROP TABLE IF EXISTS Emails")
    cursor.execute("DROP TABLE IF EXISTS Financials")
    cursor.execute("DROP TABLE IF EXISTS CrimeScene")

    cursor.execute(
        """
    CREATE TABLE Suspects (
        SuspectID INTEGER PRIMARY KEY,
        Name VARCHAR(100),
        RelationshipToVictim VARCHAR(100),
        Alibi TEXT,
        Motive TEXT,
        AccessToOffice BOOLEAN,
        CriminalRecord TEXT
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE Solutions (
        SolutionID INTEGER PRIMARY KEY,
        GuestName VARCHAR(100),
        IsCorrect BOOLEAN
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE Articles (
        ArticleID INTEGER PRIMARY KEY,
        AuthorID INTEGER,
        Title VARCHAR(255),
        PublishDate DATE,
        Content TEXT,
        IsPublished BOOLEAN,
        FOREIGN KEY (AuthorID) REFERENCES Suspects(SuspectID)
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE PhoneRecords (
        RecordID INTEGER PRIMARY KEY,
        CallerID INTEGER,
        ReceiverID INTEGER,
        CallDateTime DATETIME,
        DurationMinutes INTEGER,
        Location VARCHAR(100),
        FOREIGN KEY (CallerID) REFERENCES Suspects(SuspectID),
        FOREIGN KEY (ReceiverID) REFERENCES Suspects(SuspectID)
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE OfficeLogs (
        LogID INTEGER PRIMARY KEY,
        PersonID INTEGER,
        EntryTime DATETIME,
        ExitTime DATETIME,
        Purpose TEXT,
        Verified BOOLEAN,
        FOREIGN KEY (PersonID) REFERENCES Suspects(SuspectID)
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE Emails (
        EmailID INTEGER PRIMARY KEY,
        SenderID INTEGER,
        ReceiverID INTEGER,
        SentDateTime DATETIME,
        Subject TEXT,
        Content TEXT,
        Deleted BOOLEAN,
        FOREIGN KEY (SenderID) REFERENCES Suspects(SuspectID),
        FOREIGN KEY (ReceiverID) REFERENCES Suspects(SuspectID)
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE Financials (
        TransactionID INTEGER PRIMARY KEY,
        SuspectID INTEGER,
        Date DATE,
        Amount DECIMAL(15, 2),
        Source VARCHAR(100),
        Suspicious BOOLEAN,
        FOREIGN KEY (SuspectID) REFERENCES Suspects(SuspectID)
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE CrimeScene (
        EvidenceID INTEGER PRIMARY KEY,
        Item VARCHAR(100),
        Location VARCHAR(100),
        DNAMatch INTEGER,
        TimeFound DATETIME,
        FOREIGN KEY (DNAMatch) REFERENCES Suspects(SuspectID)
    )
    """
    )

    cursor.execute(
        """
    INSERT INTO Suspects (SuspectID, Name, RelationshipToVictim, Alibi, Motive, AccessToOffice, CriminalRecord) VALUES
    (1, 'Lydia Hawthorne', 'Source for a story', 'At a fundraising gala', 'Feared Frank would expose her past financial dealings', 1, 'Embezzlement (2008)'),
    (2, 'James Hawthorne', 'Subject of an investigation', 'At a high-stakes poker game', 'Frank was about to publish a story on his gambling debts and mob connections', 0, 'Fraud (2015)'),
    (3, 'Veronica Sterling', 'Rival Reporter', 'Working late at her own office', 'Competed with Frank for a major story; his death would benefit her career', 1, 'None'),
    (4, 'Arthur Finch', 'Frank''s Editor', 'At home with his family', 'Disagreed with Frank over the direction of the Hawthorne story; stood to inherit Frank''s research', 1, 'None'),
    (5, 'Claire Lawson', 'Interviewee', 'At a yoga class', 'Frank knew about her secret meetings with Henry Whitaker and illegal transactions', 0, 'Money laundering (2019)'),
    (6, 'Marcus Reed', 'IT Specialist', 'Watching a movie alone', 'Frank discovered he was selling confidential information to competitors', 1, 'Hacking (2017)')
    """
    )

    cursor.execute(
        """
    INSERT INTO Solutions (SolutionID, GuestName, IsCorrect) VALUES
    (1, 'Lydia Hawthorne', FALSE),
    (2, 'James Hawthorne', FALSE),
    (3, 'Veronica Sterling', FALSE),
    (4, 'Arthur Finch', TRUE),
    (5, 'Claire Lawson', FALSE),
    (6, 'Marcus Reed', FALSE)
    """
    )

    cursor.execute(
        """
    INSERT INTO Articles (ArticleID, AuthorID, Title, PublishDate, Content, IsPublished) VALUES
    (1, 3, 'The Hawthorne Scandal: A Web of Lies', '2022-10-15', 'Details on Henry Whitaker''s conviction and lingering questions about the family.', 1),
    (2, 4, 'Editor''s Note: On the Pursuit of Truth', '2022-10-16', 'A tribute to Frank Miller and his dedication to journalism.', 1),
    (3, NULL, 'The Ghost Accounts: How Money Vanishes in Elderwood', NULL, 'Expose on shell companies and hidden transactions implicating several prominent figures', 0),
    (4, NULL, 'The Informant: Who Really Runs This Town?', NULL, 'Profile of a mysterious figure controlling local businesses through intimidation', 0)
    """
    )

    cursor.execute(
        """
    INSERT INTO PhoneRecords (RecordID, CallerID, ReceiverID, CallDateTime, DurationMinutes, Location) VALUES
    (1, 2, 1, '2022-10-14 19:30:00', 15, 'Downtown'),
    (2, 5, 2, '2022-10-14 20:00:00', 5, 'Westside'),
    (3, 3, 4, '2022-10-15 10:00:00', 25, 'News Office'),
    (4, 1, 5, '2022-10-15 11:30:00', 8, 'Hawthorne Estate'),
    (5, 6, 4, '2022-10-14 21:45:00', 12, 'Near crime scene'),
    (6, 4, 3, '2022-10-14 22:30:00', 3, 'Crime scene')
    """
    )

    cursor.execute(
        """
    INSERT INTO OfficeLogs (LogID, PersonID, EntryTime, ExitTime, Purpose, Verified) VALUES
    (1, 3, '2022-10-14 21:00:00', '2022-10-14 21:15:00', 'Dropping off a file for Frank', 1),
    (2, 2, '2022-10-14 22:00:00', '2022-10-14 22:20:00', 'Heated argument with Frank', 0),
    (3, 4, '2022-10-15 09:00:00', '2022-10-15 09:10:00', 'Found the body and called the police', 1),
    (4, 6, '2022-10-14 20:30:00', '2022-10-14 21:30:00', 'Server maintenance', 1),
    (5, 4, '2022-10-14 22:15:00', '2022-10-14 22:45:00', 'Retrieve documents', 0)
    """
    )

    cursor.execute(
        """
    INSERT INTO Emails (EmailID, SenderID, ReceiverID, SentDateTime, Subject, Content, Deleted) VALUES
    (1, 4, 3, '2022-10-13 14:22:00', 'Urgent Meeting', 'We need to discuss Frank''s latest piece. It''s too dangerous to publish.', 0),
    (2, 3, 4, '2022-10-13 15:45:00', 'Re: Urgent Meeting', 'I agree. He''s digging too deep this time.', 1),
    (3, 5, 4, '2022-10-14 18:30:00', 'Information Request', 'Did you get those documents I asked for?', 0),
    (4, 1, 4, '2022-10-14 19:05:00', 'Offer', 'Name your price to make the story disappear.', 1),
    (5, 4, 6, '2022-10-14 20:15:00', 'System Access', 'Need admin privileges tonight. Urgent.', 0)
    """
    )

    cursor.execute(
        """
    INSERT INTO Financials (TransactionID, SuspectID, Date, Amount, Source, Suspicious) VALUES
    (1, 4, '2022-10-12', 25000.00, 'Unknown', 1),
    (2, 2, '2022-10-13', 5000.00, 'Casino', 0),
    (3, 1, '2022-10-14', 100000.00, 'Account Transfer', 1),
    (4, 5, '2022-10-10', 15000.00, 'Consulting', 0),
    (5, 4, '2022-10-15', 50000.00, 'Insurance Payout', 1)
    """
    )

    cursor.execute(
        """
    INSERT INTO CrimeScene (EvidenceID, Item, Location, DNAMatch, TimeFound) VALUES
    (1, 'Blood-stained envelope', 'Desk', 4, '2022-10-15 09:05:00'),
    (2, 'Broken watch', 'Floor near body', NULL, '2022-10-15 09:07:00'),
    (3, 'USB drive', 'Waste bin', 6, '2022-10-15 09:15:00'),
    (4, 'Torn document', 'Shredder', NULL, '2022-10-15 09:20:00'),
    (5, 'Partial fingerprint', 'Window sill', 3, '2022-10-15 10:30:00')
    """
    )

    connection.commit()
    connection.close()
