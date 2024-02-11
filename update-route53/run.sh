

is_ip_address() {
    local ip="$1"
    local ip_regex='^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    [[ $ip =~ $ip_regex ]]
}

export NEW_ADDRESS=`curl http://ipconfig.io -s`
export OLD_ADDRESS=`nslookup $DNS_RECORD | grep 'Address' | awk '{print $2}' | grep -v 53`

# export NEW_ADDRESS="24.135.126.207"
# export OLD_ADDRESS="24.135.126.207"

if is_ip_address "$NEW_ADDRESS"; then
    if [[ $NEW_ADDRESS != $OLD_ADDRESS ]]
    then
        echo "IP Address has been changed"
        aws route53 change-resource-record-sets --hosted-zone-id $HOSTED_ZONE_ID --change-batch "{\"Changes\":[{\"Action\":\"UPSERT\",\"ResourceRecordSet\":{\"Name\":\"$DNS_RECORD.\",\"Type\":\"A\",\"TTL\":300,\"ResourceRecords\":[{\"Value\":\"$NEW_ADDRESS\"}]}}]}"
    else
        echo "IP Address is the same"
    fi
else
    echo "It's neither an IP address nor an integer"
fi
