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



create table if not exists gpx_file (
  id serial primary key,
  name text not null,
  gpx_timestamp timestamp not null,
  parsed_time timestamp not null
);


create table if not exists gpx_point (
  id serial primary key,
  latitude float,
  longitude float,
  elevation float,
  course float,
  time timestamp,
  gpx_file_id int,
  foreign key (gpx_file_id) references gpx_file(id)
);

--psql -U postgres -h localhost -p 5432 -d points -f db/postgres/baseline.sql
