kubectl -n jobs create secret generic update-route53 \
    --from-literal=HOSTED_ZONE_ID="Z07778391PJPKVVOR0GGP" \
    --from-literal=DNS_RECORD="api.stanisavljevic.org" \
    --from-literal=AWS_ACCESS_KEY_ID="" \
    --from-literal=AWS_SECRET_ACCESS_KEY=""