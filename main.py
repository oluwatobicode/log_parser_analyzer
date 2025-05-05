with open('./logs/nginx_json_logs.txt') as file:
    logs = [file.read()]
print(logs)