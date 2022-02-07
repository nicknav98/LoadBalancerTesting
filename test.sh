## simple test command to run add query to database
# shellcheck disable=SC2034
for i in {1..100}; do
  printf '{
    "name":"dead-lifts",
    "length":"5 sets of 5",
    "directions":"let the bar fall onto just above chest, and using your pecks, lift the bar to full extension",
    "body_part":"back"
}'| http  --follow --timeout 3600 POST 'http://localhost:5050/workouts' \
 Authorization:'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDc1ODc4ODEsIm5iZiI6MTYwNzU4Nzg4MSwianRpIjoiOTYxYzBjODUtYjg5ZC00Mzc2LTlkODktNTU5NmM5MzU1NTZmIiwiZXhwIjoxNjA3NTg4NzgxLCJpZGVudGl0eSI6MiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.9jNxKrz3Kj46OmH0EGkLWDn6mCs-1ZCkIToRtrGsLPU' \
 Content-Type:'application/json'; done
