SELECT
  timestamp,
  json_payload
FROM
  `rocketech-de-pgcp-sandbox.log_analytics._AllLogs`
WHERE
  json_payload IS NOT NULL
  AND timestamp > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
  AND JSON_VALUE(json_payload.details.type) = 'random_text'
ORDER BY
  timestamp DESC
LIMIT
  100