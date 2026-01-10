# [Draft] Database Schema

> **Note**
> For full interactivity (table relationships, references, and navigation),
> open the DBML file directly in **https://dbdiagram.io**.
>
> The diagram image below is a static representation for quick reference.

---

## Database Diagram

![Train Booking Database Diagram](images/schema.png)

---

## DBML Source Code

```dbml
Project booking_project {
  database_type: 'SQLite'
  Note: '''
  Train booking system.

  Core principles:
  - Carriage numbering is train-specific (S1, A1, etc.)
  - Carriage layout is defined by reusable templates
  - Quota and seat allocation are managed separately
  - Seat availability is segment-based and derived from bookings
  - No seat-level availability/status column is stored
  '''
}

Table users {
  user_id INTEGER [pk, increment]
  first_name TEXT
  last_name TEXT
  email TEXT [not null, unique, note: 'Primary login identifier']
  password_hash TEXT [not null, note: 'Hashed password only']
  address TEXT
  created_at DATETIME
}

Table trains {
  train_id INTEGER [pk, increment]
  train_name TEXT [not null]
  created_at DATETIME
}

Table classes {
  class_id INTEGER [pk, increment]
  class_name TEXT [not null, note: 'Sleeper, 2A, 3A, CC, etc.']
}

Table carriage_types {
  carriage_type_id INTEGER [pk, increment]
  class_id INTEGER [not null, ref: > classes.class_id]
}

Table quota {
  quota_id INTEGER [pk, increment]
  quota_name TEXT [not null, note: 'General, Tatkal, etc.']
}

Table carriage_quota {
  carriage_quota_id INTEGER [pk, increment]
  carriage_type_id INTEGER [not null, ref: > carriage_types.carriage_type_id]
  quota_id INTEGER [not null, ref: > quota.quota_id]
  seat_count INTEGER [not null]
}

Table train_carriages {
  train_carriage_id INTEGER [pk, increment]
  train_id INTEGER [not null, ref: > trains.train_id]
  carriage_type_id INTEGER [not null, ref: > carriage_types.carriage_type_id]
  carriage_label TEXT [not null]
  carriage_order INTEGER [not null]
}

Table seats {
  seat_id INTEGER [pk, increment]
  train_carriage_id INTEGER [not null, ref: > train_carriages.train_carriage_id]
  seat_number TEXT [not null]
}

Table stations {
  station_id INTEGER [pk, increment]
  station_name TEXT [not null, unique]
  created_at DATETIME
}

Table train_stations {
  train_station_id INTEGER [pk, increment]
  train_id INTEGER [not null, ref: > trains.train_id]
  station_id INTEGER [not null, ref: > stations.station_id]
  stop_order INTEGER [not null]
  arrival_time DATETIME
  departure_time DATETIME
}

Table bookings {
  booking_id INTEGER [pk, increment]
  user_id INTEGER [not null, ref: > users.user_id]
  train_id INTEGER [not null, ref: > trains.train_id]
  departure_train_station_id INTEGER [not null, ref: > train_stations.train_station_id]
  arrival_train_station_id INTEGER [not null, ref: > train_stations.train_station_id]
  class_id INTEGER [not null, ref: > classes.class_id]
  booking_status TEXT [not null]
  booked_at DATETIME
}

Table booking_seats {
  booking_seat_id INTEGER [pk, increment]
  booking_id INTEGER [not null, ref: > bookings.booking_id]
  seat_id INTEGER [not null, ref: > seats.seat_id]
}
