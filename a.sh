#!/usr/bin/bash
reg() {
    set -e
    keypair=$(openssl genpkey -algorithm X25519|openssl pkey -text -noout)
    private_key=$(echo "$keypair" | awk '/priv:/{flag=1; next} /pub:/{flag=0} flag' | tr -d '[:space:]' | xxd -r -p | base64)
    public_key=$(echo "$keypair" | awk '/pub:/{flag=1} flag' | tr -d '[:space:]' | xxd -r -p | base64)
    curl -X POST 'https://api.cloudflareclient.com/v0a2158/reg' -sL --tlsv1.3 \
    -H 'CF-Client-Version: a-7.21-0721' -H 'Content-Type: application/json' \
    -d \
   '{
        "key":"'${public_key}'",
        "tos":"'$(date +"%Y-%m-%dT%H:%M:%S.000Z")'"
    }' \
        | ${jq} | sed "/\"account_type\"/i\         \"private_key\": \"$private_key\","
}
warp_info=$(reg)
echo "$warp_info"
