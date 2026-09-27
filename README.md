# AFIA MTAANI

A command-line child vaccination tracking system built for community health workers.

## Table of Contents

- [Description](#description)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Vaccination Schedule](#vaccination-schedule)
- [Data Storage](#data-storage)
- [Future Improvements](#future-improvements)
- [Author](#author)


## Description

**AFIA MTAANI** ("Community Health" in Swahili) is a Python-based console application that helps community health workers register children, record their vaccinations, and keep track of who is due, overdue, or up to date on their immunizations.

## Problem Statement

Community health workers who go door-to-door administering vaccines often have no simple, reliable way to record which children they have vaccinated and when the next dose is due. Paper records get lost or damaged, and there is no easy way to flag a child who has missed a scheduled vaccination. AFIA MTAANI closes this gap by giving health workers a lightweight digital tool to register children once and track their entire vaccination history and schedule going forward.

## Features

- **Register a child** — capture the child's name, date of birth, guardian details, and location, and assign them a unique child ID (e.g. `CH-0001`).
- **Search for a child** — look up a child's full profile by their child ID.
- **Record a vaccination** — select from the national vaccination schedule and log the dose and date administered for a specific child, with duplicate-entry protection.
- **Vaccination summary** — view a per-child breakdown of completed, upcoming, and overdue vaccinations.
- **Vaccination alerts** — get a consolidated list of every child who has an overdue vaccination, and every child with a vaccination due within the next 7 days.
- **Input validation** — names, dates of birth, phone numbers, and locations are all validated at the point of entry to keep the records clean.

## Project Structure

```
Afia_mtaani/
├── main.py                    # Entry point — menu that ties all modules together
├── registration.py            # Registers a new child
├── search.py                  # Searches for a child by ID
├── Vaccination.py             # Records a vaccination for a child
├── vaccination_summary.py     # Displays completed/upcoming/overdue summary per child
├── vaccination_alerts.py      # Displays overdue and due-soon alerts across all children
├── vaccination_status.py      # Calculates each child's vaccination status
├── vaccination_dates.py       # Calculates expected vaccination dates from date of birth
├── vaccination_schedule.py    # The national vaccination schedule (vaccine, dose, age)
├── reg_validation.py          # Input validation (name, date of birth, phone, location)
├── id_generator.py            # Generates unique, sequential child IDs
├── storage.py                 # Reads and writes child records to/from JSON
├── children.json              # Stored child records (created automatically)
├── id_counter.json            # Tracks the last issued child ID (created automatically)
├── LICENSE
└── README.md
```

## Requirements

- Python 3.10 or later (required for the dictionary-in-f-string syntax used in `id_generator.py`)
- No external packages — the project only uses Python's standard library (`json`, `re`, `datetime`, `os`)

## Installation

1. Clone or download the project:
   ```bash
   git clone <your-repository-url>
   cd Afia_mtaani
   ```
2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   ```
3. No additional dependencies are required.

## Usage

Run the application from the project's root folder:

```bash
python main.py
```

You will see the main menu:

```
===== CHILD VACCINATION TRACKER =====
1. Register a new child
2. Search for a child
3. Record a vaccination
4. View vaccination summary (all children)
5. View vaccination alerts (overdue / upcoming)
6. Exit
```

Enter the number corresponding to the action you want to perform and follow the prompts. `children.json` and `id_counter.json` are created automatically the first time you register a child, so no manual setup is needed.

## Vaccination Schedule

Vaccinations are scheduled according to the child's age in weeks, following Kenya's routine immunization schedule (defined in `vaccination_schedule.py`), including BCG, OPV, Pentavalent, PCV10, Rotavirus, IPV, Vitamin A, Measles-Rubella, and TCV.

## Data Storage

Child records are stored locally in `children.json` as a list of JSON objects, each containing the child's details and a `Vaccinations` list of administered doses. `id_counter.json` keeps track of the last child ID issued so that new registrations always receive a unique, sequential ID.

## Future Improvements

- Add the ability to edit or delete a child's record
- Add SMS/email reminders for guardians ahead of due dates
- Migrate from JSON file storage to a proper database (e.g. SQLite)
- Add a graphical or web-based interface for easier field use

## Author

Developed as a community health project by Rowan Hadegu.

## Presentation Link
- https://www.canva.com/design/DAHWaWLvu0M/B4wB6VV0LfhNyfzfu39JeA/edit?ui=eyJBIjp7fX0
  

