def check_risks(usage_data, limits):
    risks = []
    for item in usage_data:
        service = item["service"]
        usage = item["usage"]
        if service in limits:
            limit_key = list(limits[service].keys())[0]
            limit_value = list(limits[service].values())[0]
            if usage >= limit_value * 0.9:  # 90% threshold
                risks.append({
                    "service": service,
                    "message": f"⚠️ {service} usage at {usage} {item['unit']} approaching limit {limit_value} {item['unit']}"
                })
    return risks
