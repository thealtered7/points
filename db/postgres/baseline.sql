drop index if exists user_uuid_idx;
drop table if exists point_set cascade;
drop table if exists point cascade;
drop table if exists gpx_file cascade;
drop table if exists gpx_point cascade;
drop table if exists users cascade;


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
  hash text,
  user_id text, 
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


create table if not exists users (
  id serial primary key,
  first_name text not null,
  last_name text not null,
  uuid text not null
);

create index if not exists user_uuid_idx on users (uuid);

insert into users(first_name, last_name, uuid) values ('Jeffrey', 'Keene', 'b280193a-18af-4300-9bd1-8f7feccc75f7');
insert into users(first_name, last_name, uuid) values ('Joel', 'Stoffregen', '864f1494-29d1-457b-a359-584e41c3bf22');

--psql -U postgres -h localhost -p 5432 -d points -f db/postgres/baseline.sql
