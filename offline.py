import yaml
import os

if __name__ == "__main__" :
    cwd = os.getcwd()
    offline_serverless_template_path = os.path.join(cwd, 'serverless.local.yml')
    offline_serverless_path = os.path.join(cwd, 'serverless.yml')

    serverless_yml = {}
    with open(offline_serverless_template_path, 'r') as stream:
        serverless_yml = yaml.safe_load(stream)

    serverless_yml['functions'] = {}

    for dir in os.listdir(cwd):
        path = os.path.join(cwd, dir)
        if os.path.isdir(path):
            file = os.path.join(path, 'serverless.yml')
            if os.path.isfile(file):
                with open(file, 'r') as stream:
                    try:
                        data = yaml.safe_load(stream)
                        if data:
                            functions = data.get('functions')
                            for name in functions:
                                fn_name = '{0}-{1}'.format(dir, name)
                                handler_path = '{0}/{1}'.format(dir, functions[name]['handler'])

                                if 'environment' in functions[name]:
                                    for env in functions[name]['environment']:
                                        functions[name]['environment'][env] = functions[name]['environment'][env].replace('${self:service}', data.get('service'))

                                events = functions[name]['events']
                                for event in events:
                                    if 'http' in event and 'authorizer' in event['http']:
                                        event['http'].pop('authorizer', None)

                                functions[name]['handler'] = handler_path

                                serverless_yml['functions'][fn_name] = functions[name]
                    except yaml.YAMLError as exc:
                        print(exc)


    with open(offline_serverless_path, 'w+') as stream:
        stream.write(yaml.dump(serverless_yml, default_flow_style=False))
        print('serverless.yml for offline generated')