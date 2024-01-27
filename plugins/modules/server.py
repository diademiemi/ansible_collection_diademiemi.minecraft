#!/usr/bin/python
# -*- coding: utf-8 -*-

#  MIT License
# SPDX-License-Identifier: MIT

# Notice: This file has been created with the help of AI.
# This is pre-release, no guarantees are made of its stability or security.

from ansible.module_utils.basic import AnsibleModule
import os
import requests
import hashlib
import re
from bs4 import BeautifulSoup

DOCUMENTATION = '''
module: server
short_description: Manage Minecraft servers
description:
    - Manage Minecraft servers, installing the server jar, plugins, and generating a start script.
options:
    path:
        description:
            - The path to the server directory.
        required: true
        type: str
    type:
        description:
            - The type of server to install.
        required: true
        type: str
        choices: ['vanilla', 'spigot', 'paper', 'purpur']
    version:
        description:
            - The version of the server jar to install.
        required: true
        type: str
    build:
        description:
            - The build of the server jar to install.
        required: false
        type: str
        default: 'latest'
    plugins:
        description:
            - The list of plugins to install.
        required: false
        type: list
        elements: dict
        default: []
    min_memory:
        description:
            - The minimum amount of memory to allocate to the server.
        required: false
        type: int
        default: 2048
    max_memory:
        description:
            - The maximum amount of memory to allocate to the server.
        required: false
        type: int
        default: 4096
    java_opts:
        description:
            - The Java options to pass to the server.
        required: false
        type: str
        default: ''
    server_args:
        description:
            - The arguments to pass to the server.
        required: false
        type: str
        default: 'nogui'

'''

EXAMPLES = '''
    - name: Install a Purpur server
      diademiemi.minecraft.server:
        path: "{{ lookup('env', 'HOME') }}/purpur"
        type: purpur  # purpur/paper/spigot/vanilla
        version: 1.20.2  # Server version
        build: latest  # Build number, "latest" fetches the latest build
        java_opts: 'aikar'  # empty string defaults to just memory opts, "aikar" adds Aikar's flags, any other string adds that string to the flags
        min_memory: "8192"  # In MB
        max_memory: "16384"  # In MB
        plugins:
          - name: EssentialsX
            source: https://ci.ender.zone/job/EssentialsX/1531/artifact/jars/EssentialsX-2.21.0-dev+24-0af4436.jar
            type: url  # Downloads straight from the URL
            state: present
          - name: Vault
            source: https://www.spigotmc.org/resources/vault.34315/
            type: spigot  # Does not support downloading specific versions
            state: present
          - name: WorldGuard
            source: https://dev.bukkit.org/projects/worldguard
            type: bukkit
            # version: 4675318
            version: latest
            state: present
          - name: WorldEdit
            source: https://dev.bukkit.org/projects/worldedit
            type: bukkit
            # version: 4954432
            version: latest
            state: present
          - name: ViaVersion
            source: https://hangar.papermc.io/ViaVersion/ViaVersion
            type: hangar
            # version: 4.9.2
            version: latest
            state: present
'''

USER_AGENT = "Ansible/diademiemi.minecraft/1.0"

def file_checksum(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def download_file(url, dest):
    if not os.path.exists(os.path.dirname(dest)):
        os.makedirs(os.path.dirname(dest))
    headers = {'User-Agent': USER_AGENT}
    response = requests.get(url, headers=headers, stream=True)

    if response.status_code == 404:
        raise ValueError(f"File not found at URL: {url}")

    with open(dest, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

def get_spigot_resource_id(url):
    return url.rstrip('/').split('.')[-1]

def get_latest_spigot_version(resource_id):
    headers = {'User-Agent': USER_AGENT}
    response = requests.get(f'https://api.spiget.org/v2/resources/{resource_id}/versions/latest', headers=headers)
    if response.status_code == 200:
        return response.json()['id']
    else:
        raise ValueError(f"Could not fetch latest version for Spigot resource ID {resource_id}")

def get_latest_hangar_version(plugin_name):
    try:
        headers = {'User-Agent': USER_AGENT}
        page = requests.get(f'https://hangar.papermc.io/{plugin_name}/{plugin_name}', headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        version_link = soup.find('a', class_='btn')['href']
        version_match = re.search(r'versions/(\d+\.\d+\.\d+)/', version_link)
        return version_match.group(1) if version_match else None
    except Exception as e:
        print(f"Error fetching latest version for Hangar plugin {plugin_name}: {e}")
        return None

def get_download_url(plugin, path):
    plugin_dest = os.path.join(path, 'plugins', f'{plugin["name"]}.jar')

    # Default return value
    default_return = (None, plugin_dest)

    if plugin.get('state', 'present') == 'absent':
        return default_return

    if plugin['type'] == 'url':
        return (plugin['source'], plugin_dest)

    elif plugin['type'] == 'bukkit':
        headers = {'User-Agent': USER_AGENT}
        if plugin.get('version', 'latest') == 'latest':
            # Scrape the Bukkit project page for the latest file ID
            project_page_url = f'{plugin["source"]}/files'
            page = requests.get(project_page_url, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            latest_file_element = soup.select_one('a.overflow-tip')
            print(latest_file_element)
            print(f'{plugin["source"]}/files')
            if latest_file_element:
                latest_file_id = latest_file_element['href'].split('/')[-1]
                return (f'https://dev.bukkit.org/projects/{plugin["name"]}/files/{latest_file_id}/download', plugin_dest)
            else:
                raise ValueError(f"Could not find the latest file for Bukkit plugin {plugin['name']}")
        else:
            return (f'{plugin["source"]}/files/{plugin["version"]}/download', plugin_dest)

    elif plugin['type'] == 'spigot':
        resource_id = get_spigot_resource_id(plugin['source'])
        if resource_id:
            # Use Spiget API to download the plugin
            url = f"https://api.spiget.org/v2/resources/{resource_id}/download"
            return (url, plugin_dest)
        else:
            return default_return

    elif plugin['type'] == 'hangar':
        version = plugin.get('version', 'latest')
        if version == 'latest':
            version = get_latest_hangar_version(plugin['name'])
        return (f'https://hangarcdn.papermc.io/plugins/{plugin["name"]}/{plugin["name"]}/versions/{version}/PAPER/{plugin["name"]}-{version}.jar', plugin_dest)

    else:
        return default_return
    
def main():
    module_args = dict(
        path=dict(type='str', required=True),
        type=dict(type='str', required=True, choices=['vanilla', 'spigot', 'paper', 'purpur']),
        version=dict(type='str', required=True),
        build=dict(type='str', default='latest'),
        plugins=dict(type='list', elements='dict', default=[]),
        min_memory=dict(type='int', default=2048),  # Default 2GB
        max_memory=dict(type='int', default=4096),  # Default 4GB
        java_opts=dict(type='str', default=''),
        server_args=dict(type='str', default='nogui')  # Default server arguments
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    server_type = module.params['type']
    version = module.params['version']
    build = module.params['build']
    plugins = module.params['plugins']
    min_memory = module.params['min_memory']
    max_memory = module.params['max_memory']
    java_opts = module.params['java_opts']
    server_args = module.params['server_args']

    changed = False
    changes = []

    # Create necessary directories
    if not os.path.exists(path):
        os.makedirs(path)
        changed = True
    if not os.path.exists(os.path.join(path, 'plugins')):
        os.makedirs(os.path.join(path, 'plugins'))
        changed = True

    # Server download URL mapping
    server_urls = {
        'vanilla': f'https://launcher.mojang.com/v1/objects/{version}/server.jar',
        'spigot': f'https://download.getbukkit.org/spigot/spigot-{version}.jar',
        'paper': f'https://papermc.io/api/v2/projects/paper/versions/{version}/builds/{build}/downloads/paper-{version}-{build}.jar',
        'purpur': f'https://api.purpurmc.org/v2/purpur/{version}/{build}/download'
    }

    # Download server
    server_url = server_urls[server_type]
    server_dest = os.path.join(path, 'server.jar')
    if version in ['latest', 'present'] and not os.path.exists(server_dest):
        download_file(server_url, server_dest)
        changed = True
        changes.append(f"Server jar downloaded: {server_dest}")
    elif version == 'absent' and os.path.exists(server_dest):
        os.remove(server_dest)
        changed = True
        changes.append(f"Server jar removed: {server_dest}")

    # Download plugins
    for plugin in plugins:
        try:
            plugin_url, plugin_dest = get_download_url(plugin, path)
            plugin_exists = os.path.exists(plugin_dest)
            existing_plugin_checksum = file_checksum(plugin_dest) if plugin_exists else None

            if plugin.get('state', 'present') in ['present', 'download'] and (not plugin_exists or plugin.get('state') == 'download'):
                download_file(plugin_url, plugin_dest)
                new_plugin_checksum = file_checksum(plugin_dest)
                if not plugin_exists or existing_plugin_checksum != new_plugin_checksum:
                    changed = True
                    change_type = "downloaded" if not plugin_exists else "updated"
                    changes.append(f"Plugin {change_type}: {plugin_dest}")
            elif plugin.get('state') == 'absent' and plugin_exists:
                os.remove(plugin_dest)
                changed = True
                changes.append(f"Plugin removed: {plugin_dest}")
        except ValueError as e:
            module.fail_json(msg=str(e))

    # Generate start.sh script
    start_script_path = os.path.join(path, 'start.sh')
    if java_opts == 'aikar':
        java_opts = ("-Xms{}M -Xmx{}M -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 "
                     "-XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch "
                     "-XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M "
                     "-XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 "
                     "-XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 "
                     "-XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem "
                     "-XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs "
                     "-Daikars.new.flags=true --add-modules=jdk.incubator.vector").format(min_memory, max_memory)
    elif not java_opts:
        java_opts = "-Xms{}M -Xmx{}M".format(min_memory, max_memory)

    start_script_content = "#!/bin/bash\njava {} -jar server.jar {}\n".format(java_opts, server_args)
    existing_start_script_checksum = file_checksum(start_script_path) if os.path.exists(start_script_path) else None
    new_start_script_checksum = hashlib.sha256(start_script_content.encode()).hexdigest()

    if not os.path.exists(start_script_path) or existing_start_script_checksum != new_start_script_checksum:
        with open(start_script_path, 'w') as start_script:
            start_script.write(start_script_content)
        os.chmod(start_script_path, 0o755)  # Make the script executable
        changed = True
        change_type = "created" if not os.path.exists(start_script_path) else "modified"
        changes.append(f"start.sh script {change_type}: {start_script_path}")

    if changed:
        module.exit_json(changed=True, changes=changes)
    else:
        module.exit_json(changed=False)

if __name__ == '__main__':
    main()

