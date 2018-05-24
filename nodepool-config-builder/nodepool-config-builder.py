#!/usr/bin/env python3

import sys
import socket

import yaml

import paramiko

def retrieve_host_key(host, port=22):
    transport = paramiko.Transport(host, port)
    transport.connect()
    try:
        return transport.get_remote_server_key()
    finally:
        transport.close()

def main(in_stream, out_stream):
    config = yaml.load(in_stream)

    for provider in config['providers']:
        if provider['driver'] == 'dns':
            provider['driver'] = 'static'

            for pool in provider['pools']:
                labels = pool.pop('labels')
                username = pool.pop('username')
                fqdn = pool.pop('fqdn')
                connection_port = pool.pop('connection-port', 22)
                timeout = pool.pop('timeout', 5)
                max_parallel_jobs = pool.pop('max-parallel-jobs', 1)

                (_, _, addresses) = socket.gethostbyname_ex(fqdn)

                pool['nodes'] = []

                for address in addresses:
                    host_key = retrieve_host_key(address)
                    host_key_name = host_key.get_name()
                    host_key_value = host_key.get_base64()

                    pool['nodes'].append({
                        'name': address,
                        'labels': labels,
                        'username': username,
                        'host-key': "{} {}".format(host_key_name, host_key_value),
                        'connection-port': connection_port,
                        'connection-type': 'ssh',
                        'timeout': timeout,
                        'max-parallel-jobs': max_parallel_jobs,
                    })

    yaml.dump(config, out_stream, default_flow_style=False)

if __name__ == '__main__':
    main(sys.stdin, sys.stdout)
