for i in $(seq 1 100)
do
    curl HOST_URL \
    -s -o /dev/null \
    -w "@curl-format.txt" \
    -X POST \
    -H 'Content-Type: application/json' \
    -d '{}'
done
