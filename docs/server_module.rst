
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.6.1

.. Anchors

.. _ansible_collections.diademiemi.minecraft.server_module:

.. Anchors: short name for ansible.builtin

.. Title

diademiemi.minecraft.server module -- Manage Minecraft servers
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `diademiemi.minecraft collection <https://galaxy.ansible.com/ui/repo/published/diademiemi/minecraft/>`_ (version 0.0.1).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install diademiemi.minecraft`.

    To use it in a playbook, specify: :code:`diademiemi.minecraft.server`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Manage Minecraft servers, installing the server jar, plugins, and generating a start script.


.. Aliases


.. Requirements






.. Options

Parameters
----------

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-build"></div>

      .. _ansible_collections.diademiemi.minecraft.server_module__parameter-build:

      .. rst-class:: ansible-option-title

      **build**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-build" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The build of the server jar to install.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"latest"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-java_opts"></div>

      .. _ansible_collections.diademiemi.minecraft.server_module__parameter-java_opts:

      .. rst-class:: ansible-option-title

      **java_opts**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-java_opts" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The Java options to pass to the server.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`""`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-max_memory"></div>

      .. _ansible_collections.diademiemi.minecraft.server_module__parameter-max_memory:

      .. rst-class:: ansible-option-title

      **max_memory**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-max_memory" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The maximum amount of memory to allocate to the server.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`4096`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-min_memory"></div>

      .. _ansible_collections.diademiemi.minecraft.server_module__parameter-min_memory:

      .. rst-class:: ansible-option-title

      **min_memory**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-min_memory" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The minimum amount of memory to allocate to the server.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`2048`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-path"></div>

      .. _ansible_collections.diademiemi.minecraft.server_module__parameter-path:

      .. rst-class:: ansible-option-title

      **path**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-path" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The path to the server directory.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-plugins"></div>

      .. _ansible_collections.diademiemi.minecraft.server_module__parameter-plugins:

      .. rst-class:: ansible-option-title

      **plugins**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-plugins" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The list of plugins to install.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`[]`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-server_args"></div>

      .. _ansible_collections.diademiemi.minecraft.server_module__parameter-server_args:

      .. rst-class:: ansible-option-title

      **server_args**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-server_args" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The arguments to pass to the server.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"nogui"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-type"></div>

      .. _ansible_collections.diademiemi.minecraft.server_module__parameter-type:

      .. rst-class:: ansible-option-title

      **type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The type of server to install.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"vanilla"`
      - :ansible-option-choices-entry:`"spigot"`
      - :ansible-option-choices-entry:`"paper"`
      - :ansible-option-choices-entry:`"purpur"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-version"></div>

      .. _ansible_collections.diademiemi.minecraft.server_module__parameter-version:

      .. rst-class:: ansible-option-title

      **version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-version" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The version of the server jar to install.


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
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




.. Facts


.. Return values


..  Status (Presently only deprecated)


.. Authors



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/diademiemi/ansible_collection_diademiemi.minecraft/issues"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/diademiemi/ansible_collection_diademiemi.minecraft"
    external: true


.. Parsing errors

