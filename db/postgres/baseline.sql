create table if not exists point_set (
  id serial primary key,
  name text,
  created timestamp
);

create table if not exists point (
  id serial primary key,
  x float not null default 0.0,
  y float not null default 0.0,
  z float not null default 0.0,
  point_set_id int,
  FOREIGN KEY (point_set_id) REFERENCES point_set (id)
);

--psql -U postgres -h localhost -p 5432 -d points -f db/postgres/baseline.sql
