Beta User Guide
===============

Installing Quipucords
---------------------
Quipucords is delivered in two parts, an RPM command line tool and a server container image. The following instructions describe how to install the parts of Quipucords.

Installing the Command Line Tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
qpc, the command line tool that is installed by RPM, is available for `download <https://copr.fedorainfracloud.org/coprs/chambridge/qpc/>`_ from the Fedora COPR build and repository system.

1. Enable the EPEL repo for the server. You can find the appropriate architecture and version on the `EPEL wiki <https://fedoraproject.org/wiki/EPEL>`_.

  - For Red Hat Enterprise Linux 7, enter the following command:
    ``# rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm``

  - For Red Hat Enterprise Linux 6, enter the following command:
    ``# rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm``

2. Add the COPR repo to your server. You can find the appropriate architecture and version on the `COPR qpc page <https://copr.fedorainfracloud.org/coprs/chambridge/qpc/>`_.


  - For Red Hat Enterprise Linux 7, enter the following command:
    ``# wget -O /etc/yum.repos.d/chambridge-qpc-epel-7.repo https://copr.fedorainfracloud.org/coprs/chambridge/qpc/repo/epel-7/chambridge-qpc-epel-7.repo``

  - For Red Hat Enterprise Linux 6, enter the following command:
    ``# wget -O /etc/yum.repos.d/chambridge-qpc-epel-6.repo https://copr.fedorainfracloud.org/coprs/chambridge/qpc/repo/epel-6/chambridge-qpc-epel-6.repo``

3. Install the qpc beta package:

  - For Red Hat Enterprise Linux 7, enter the following command:
    ``# yum -y install qpc-0.0.1-1.git.227.d622e53.el7.centos``

  - For Red Hat Enterprise Linux 6, enter the following command:
    ``# yum -y install qpc-0.0.1-1.git.227.d622e53.el6``

Installing the Server Container Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Quipucords server is delivered as a container image that runs on your server. First you must install and start the necessary prerequisite, Docker, to run the container. Then you can obtain and install the server container image.

Installing the Docker Prerequisite
""""""""""""""""""""""""""""""""""
The instructions for installing Docker vary according to your system configuration.

Installing Docker on Red Hat Enterprise Linux 6.6 or later
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To install Docker on Red Hat 6.6 or later, you must have kernel 2.6.32-431 or later installed.

To check the current kernel release, open a terminal session and use the ``uname`` command to display the kernel release information, as shown in the following example::

  # uname -r

The output of this command is similar to the following example::

  3.10.0-229.el7.x86_64

**TIP:** After you confirm that you have at least the minimum required kernel release, it is recommended that you fully update your system. Having a fully patched system can help you avoid kernel bugs that have already been fixed on the latest kernel packages.

When your system meets the minimum required kernel release, you can use the following steps to install Docker:

1. Log in to your machine as a user with ``sudo`` or ``root`` privileges.

2. Download the Docker RPM to the current directory:

  ``# curl -O -sSL https://yum.dockerproject.org/repo/main/centos/6/Packages/docker-engine-1.7.1-1.el6.x86_64.rpm``

3. Install the Docker package with yum:

  ``# sudo yum localinstall --nogpgcheck docker-engine-1.7.1-1.el6.x86_64.rpm``


Starting Docker on Red Hat Enterprise Linux 6.6 or later
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
After you install Docker, you must start it and verify that it is running.

1. Start the Docker daemon:

  ``# sudo service docker start``

2. Verify that Docker is installed correctly by running the hello-world image:

  ``# sudo docker run hello-world``

This command displays output similar to the following example::

  Unable to find image 'hello-world:latest' locally
  latest: Pulling from hello-world
  a8219747be10: Pull complete
  91c95931e552: Already exists
  hello-world:latest: The image you are pulling has been verified. Important: image verification is a tech preview feature and should not be relied on to provide security.
  Digest: sha256:aa03e5d0d5553b4c3473e89c8619cf79df368babd18681cf5daeb82aab55838d
  Status: Downloaded newer image for hello-world:latest
  Hello from Docker.
  This message shows that your installation appears to be working correctly.


  To generate this message, Docker took the following steps:
   1. The Docker client contacted the Docker daemon.
   2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
          (Assuming it was not already locally available.)
   3. The Docker daemon created a new container from that image which runs the
          executable that produces the output you are currently reading.
   4. The Docker daemon streamed that output to the Docker client, which sent it
          to your terminal.


  To try something more ambitious, you can run an Ubuntu container with:
   $ docker run -it ubuntu bash


  For more examples and ideas, visit:
   http://docs.docker.com/userguide/

3. To ensure that Docker starts when you start your system, enter the following command:

  ``# sudo chkconfig docker on``

After you complete the steps to install Docker for Red Hat Enterprise Linux 6.6 or later, you can continue with the steps to obtain the Quipucords server container image.

Installing Docker on Red Hat Enterprise Linux 7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can install Docker in different ways, depending on your needs:

- Most users set up the Docker repositories and install from them, for ease of installation and upgrade tasks. This choice is the recommended approach.

- Other users download the RPM package, install it manually, and manage upgrades manually. This choice is useful when Docker is installed on air-gapped systems with no access to the internet.

Installing from the repository
++++++++++++++++++++++++++++++
1. Log in to your machine as a user with ``sudo`` or ``root`` privileges.

2. Install the required packages:

  ``# sudo yum install -y yum-utils device-mapper-persistent-data lvm2``

3. Add the repository:

  ``# sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo``

4. Install Docker from the repository:

  ``# sudo yum install docker-ce``

Installing from a package
+++++++++++++++++++++++++
1. Go to https://download.docker.com/linux/centos/7/x86_64/stable/Packages/. For the Docker version that you want to install, download the RPM file to the intended installation system.

2. Log in to your machine as a user with ``sudo`` or ``root`` privileges.

3. Install Docker, changing the path in the following example to the path where you downloaded the Docker package:

 ``# sudo yum install /path/to/package.rpm``

Starting Docker on Red Hat Enterprise Linux 7
+++++++++++++++++++++++++++++++++++++++++++++
After you install Docker, you must start it and verify that it is running.

1. Start Docker:

  ``# sudo systemctl start docker``

2. Verify that Docker is installed correctly by running the hello-world image:

  ``# sudo docker run hello-world``

After you complete the steps to install Docker for Red Hat Enterprise Linux 7 or later, you can continue with the steps to obtain the Quipucords server container image.

Installing the Quipucords Server Container Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
After Docker is installed, you can obtain and install the container image that enables the use of the Quipucords server.

**TBD**


Configuring and Starting Quipucords
-----------------------------------
After you install the Quipucords server container image in the image registry, you must select configuration options to be used at the time that you start the server and the command line tool. When you are sure of the options that you want to use, you can start Quipucords by starting the server and the command line tool.

Selecting the Quipucords Server Configuration Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When you run the command to start the Quipucords server, you supply values for several options that affect the configuration of that server. You must make the following decisions:

- Accepting or changing the default exposed server port
- Selecting a directory for SSH keys
- Selecting a directory for the SQLlite database
- Selecting a directory for log output

The following steps guide you through those choices.

1. Accept or change the default exposed server port to use for HTTPS communication. By default, the server exposes port 443, which is the standard HTTPS port. You can choose to use that port or remap the port to be used on your server.

   - If you select to expose port 443, you would use the following option when you run the Docker command to start the server: ``-p 443:443``.
   - If you want to remap the port on your system, you would supply a new value for port when you run the Docker command to start the server. The syntax of this option is  ``-p <host_port>:<container_port>``. For example, to remap the port to ``8443``, you would enter the followng option in the command: ``-p 8443:443``. Additionally, Docker supplies an option to select a free port for all exposed ports by using the ``-P`` option; the port mapping is then available from the ``sudo docker ps`` command.

2. Select values for the directory for SSH keys, the directory for the SQLlite database, and the directory for the log output. The most efficient way to configure these options is to create a home directory for the Quipucords server and then use that home directory for each of thse three options.

   \a. Create the home directory. The following example command creates the home directory  ``~/quipucords``:

    ``# mkdir -p ~/quipucords``

   \b. Change to that home directory. For example:

    ``# cd ~/quipucords``

   \c. Create subdirectories to house the SSH keys, (``~/quipucords/sshkeys``), database (``~/quipucords/data``), and log output (``~/quipucords/log``). For example::

      # mkdir sshkeys
       # mkdir data
       # mkdir log

Starting the Quipucords Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
After you make the decisions on the configuration options for the server, you can start the Quipucords server.

If your system does not have SELinux enabled, you can start the Quipucords server with the following Docker command::

  # sudo docker run --name quipucords -d -p 443:443 -v ~/quipucords/sshkeys:/sshkeys -v ~/quipucords/data:/var/data -v ~/quipucords/log:/var/log -i quipucords:latest

If your system does have SELinux enabled, you must append ``:z`` to each volume as follows::
  
  # sudo docker run --name quipucords -d -p 443:443 -v ~/quipucords/sshkeys:/sshkeys:z -v ~/quipucords/data:/var/data:z -v ~/quipucords/log:/var/log:z -i quipucords:latest

These commands start the server on port ``443`` and map the ``sshkeys``, ``data``, and ``log`` directories to the ``~/quipucords`` home directory for the server.

To view the status of the server after it is running, enter the following command::

  docker ps

Changing the Default Password for the Quipucords Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Quipucords server has a default administrator user with a default user name of ``admin`` and a default password of ``pass``. To ensure the security of your Quipucords server, it is recommended that you change the default password to a different password.

To change the default password for the Quipucords server, use the following steps:

1. In a browser window, enter the URL to the Quipucords server. When you enter the URL to the Quipucords server, the browser loads a web page that shows an administrative login dialog box.

   - If the browser window is running on the same system as the server and you used the default port of ``443`` for the server, the URL is ``https://localhost/admin``.
   - If the browser window is running on a remote system, or if it is on the same system but you changed the default HTTPS port, enter the URL in the following format: ``https://ip_address:port/admin``. For example, if the IP address for the server is 192.0.2.0 and the port is remapped to ``8443``, you would enter ``https://192.0.2.0:8443/admin`` in the browser window.

2. In the resulting web page with the Quipucords administrative login dialog box, enter the default user name ``admin`` and the default password ``pass`` to log in to the Quipucords server.

3. Click **Change password** to enter a new password for the Quipucords server. Record the new password in an enterprise password management solution or other password management tool, as determined by the best practices for your organization.

**TIP:** You can also enter the local or remote URL (as applicable) for the Quipucords server in a browser window to verify that the Quipucords server is responding.

Configuring the qpc Command Line Tool Connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
After the Quipucords server is running, you can configure the qpc command line tool to work with the server. The ``qpc server config`` command configures the connection between the qpc command line tool and the Quipucords server.

The ``qpc server config`` command takes the following options:

- The ``--host`` option is required. If you are using the qpc command line tool on the same system where the server is running, you can supply the loopback address ``127.0.0.1`` as the value. Otherwise, supply the IP address for your Quipucords server.
- The ``--port`` option is optional. The default value for this option is ``443``. If you decided to remap the Quipucords default exposed server port to another port, the port option is required. You must supply the remapped value in the command. to the port option (i.e. ``--port 8443``).

For example, if you are configuring the command line tool on the same system as the server and the server uses the default exposed server port, you would enter the following command to configure the qpc command line tool:

  ``# qpc server config --host 127.0.0.1``

However, if you are configuring the command line tool on a system that is remote from the server, the Quipucords server is running on the IP address 192.0.2.0, and the port is remapped to 8443, you would enter the following command to configure the qpc command line tool:

  ``# qpc server config --host 192.0.2.0 --port 8443``

Logging in to and Logging out of the qpc Command Line Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
After the connection between the qpc command line tool and the Quipcords server is configured on the system where you want to use the qpc command line interface, you can log in to the interface and begin using it to run qpc commands.

To log in to the qpc command line interface, enter the following command:

  ``# qpc server login``

The ``qpc server login`` command retrieves a token that is used for authentication with subsequent command line interface commands. That token is removed when you log out of the server. To log out of the server, enter the following command:

``qpc server logout``

Getting Started with Quipucords
-------------------------------
You use the capabilities of Quipucords to inspect and gather information on your IT infrastructure. The following information describes how you use the qpc command line interface to complete common Quipucords tasks.

Quipucords requires the configuration of two basic structures to manage the inspection process. A *credential* contains the access credentials, such as the username and password or SSH key of the user, with sufficient authority to run the inspection process on a particular source. A *source* defines the entity or entities to be inspected, such as a host, subnet, network, or systems management solution such as vCenter Server or Satellite. When you create a source, you also include one or more of the configured credentials to use to access the individual entities in the source during the inspection process.

You can save multiple credentials and sources to use with Quipucords in various combinations as you run inspection processes, or *scans*. When you have completed a scan, you can access the collection of *facts* in the output as a *report* to review the results.

Creating credentials and sources for the different source types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The type of source that you are going to inspect determines the type of data that is required for credential and source configuration. Quipucords currently supports the following source types:

- Network
- vCenter Server
- Satellite

Network sources are composed of one or more host names, one or more IP addresses, IP ranges, or a combination of these. vCenter Server and Satellite sources are both created with the IP address or host name of that system management solution server. The source creation command references one or more credentials. Typically, a Network source might include multiple credentials because it is expected that many credentials would be needed to access a broad IP range. Conversely, a vCenter Server or  Satellite source would typically use a single credential to access a particular system management solution server.

The following scenarios provide examples of how you would create a network source, vCenter Server source, or Satellite source and the credentials required for each.

Creating a Network Source
"""""""""""""""""""""""""
To create a network source, use the following steps:

1. Create at least one network credential with root-level access:

   ``# qpc cred add --type network --name cred_name --username root_name [--sshkeyfile key_file] [--password]``

   If you did not use the ``sshkeyfile`` option to provide an SSH key for the username value, enter the password of the user with root-level access at the connection password prompt.
   
   If you want to use SSH keyfiles in the credential, you must copy the keys into the directory that you mapped to ``/sshkeys`` during Quipucords server configuration. In the example information for that procedure, that directory is ``~/quipucords/sshkeys``. The server references these files locally, so refer to the keys as if they are in the ``/sshkeys`` directory from the qpc command.

   For example, for a network credential where the ``/sshkeys`` directory for the server is mapped to ``~/quipucords/sshkeys``, the credential name is ``roothost1``, the user with root-level access is ``root``, and the SSH key for the user is in the ``~/.ssh/id_rsa`` file, you would enter the following commands:

   ``# cp ~/.ssh/id_rsa ~/quipucords/sshkeys   
     # qpc cred add --type network --name roothost1 --username root --sshkeyfile /sshkeys/id_rsa``

   qpc also supports privilege escalation with the ``become-method``, ``become-user``, and ``become-password`` options to create a network credential for a user to obtain root-level access. You can use the ``become-*`` options with either the ``sshkeyfile`` or the ``password`` option.

   For example, for a network credential where the credential name is ``sudouser1``, the user with root-level access is ``sysadmin``, and the access is obtained through the password option, you would enter the following command:

   ``# qpc cred add --type network --name sudouser1 --username sysadmin --password --become-password``

   After you enter this command, you are prompted to enter two passwords. First, you would enter the connection password for the ``username`` user, and then you would enter the password for the ``become-method``, which is the ``sudo`` command by default.

2. Create at least one network source that specifies one or more network identifiers, such as a host name or host names, an IP address, a list of IP addresses, or an IP range, and one or more network credentials to be used for the scan:

   ``# qpc source add --type network --name source_name --hosts host_name_or_file --cred cred_name``

   For example, for a network source where the source name is ``mynetwork``, the network to be scanned is the ``192.0.2.0/24`` subnet, and the network credentials that are used to run the scan are ``roothost1`` and ``roothost2``, you would enter the following command:

   ``# qpc source add --type network --name mynetwork --hosts 192.0.2.[1:254] --cred roothost1 roothost2``

   You can also use a file to pass in the network identifiers. If you use a file to enter multiple network identifiers, such as multiple individual IP addresses, enter each on a single line. For example, for a network profile where the path to this file is ``/home/user1/hosts_file``, you would enter the following command::

   ``# qpc source add --type network --name mynetwork --hosts /home/user1/hosts_file --cred roothost1 roothost2``


Creating a vCenter Server Source
""""""""""""""""""""""""""""""""
To create a vCenter Server source, use the following steps:

1. Create at least one vcenter credential:

   ``# qpc cred add --type vcenter --name cred_name --username vcenter_user --password``

   Enter the password of the user with access to vCenter Server at the connection password prompt.

   For example, for a vcenter credential where the credential name is ``vcenter_admin`` and the user with access to the vCenter Server server is ``admin``, you would enter the following command::

   ``# qpc cred add --type vcenter --name vcenter_admin --username admin --password``

2. Create at least one vcenter source that specifies the host name or IP address of the server for vCenter Server and one vcenter credential to be used for the scan:

   ``# qpc source add --type vcenter --name source_name --hosts host_name --cred cred_name``

   For example, for a vcenter source where the source name is ``myvcenter``, the server for the vCenter Server is located at the ``192.0.2.10`` IP address, and the vcenter credential for that server is ``vcenter_admin``, you would enter the following command:

   ``# qpc source add --type vcenter --name myvcenter --hosts 192.0.2.10 --cred vcenter_admin``
   
   **IMPORTANT:** By default, sources are scanned with full SSL validation, but you might need to adjust the level of SSL validation to connect properly to the server for vCenter Server. The ``source add`` command supports options that are commonly used to downgrade the SSL validation. The ``--ssl-cert-verify`` option can take a value of ``False`` to disable SSL certificate validation; this option would be used for any server with a self-signed certificate. The ``--disable-ssl`` option can take a value of ``True`` to connect to the server over standard HTTP. 

Creating a Satellite Source
"""""""""""""""""""""""""""
To create a Satellite source, use the following steps:

1. Create at least one satellite credential:

   ``# qpc cred add --type satellite --name cred_name --username satellite_user --password``

   Enter the password of the user with access to the Satellite server at the connection password prompt.

   For example, for a Satellite credential where the credential name is ``satellite_admin`` and the user with access is to the Satellite server is ``admin``, you would enter the following command:

   ``# qpc cred add --type satellite --name satellite_admin --username admin --password``

2. Create at least one satellite source that specifies the host name or IP address of the Satellite server, one satellite credential to be used for the scan, and the version of the Satellite server (supported version values are ``5``, ``6.2``, ``6.3``):

   ``# qpc source add --type satellite --name source_name --hosts host_name --cred cred_name --satellite-version sat_ver``

   For example, for a satellite source where the source name is ``mysatellite6``, the Satellite server is located at the ``192.0.2.15`` IP address, the satellite credential for that server is ``satellite_admin``, and the version of the Satellite server is ``6.2``, you would enter the following command:

   ``# qpc source add --type satellite --name mysatellite6 --hosts 192.0.2.15 --cred satellite_admin --satellite-version 6.2``
   
   **IMPORTANT:** By default, sources are scanned with full SSL validation, but you might need to adjust the level of SSL validation to connect properly to the Satellite server. The ``source add`` command supports options that are commonly used to downgrade the SSL validation. The ``--ssl-cert-verify`` option can take a value of ``False`` to disable SSL certificate validation; this option would be used for any server with a self-signed certificate. The Satellite server does not support disabling SSL, so the ``--disable-ssl`` option has no effect.

Running a scan
^^^^^^^^^^^^^^
After you set up your credentials and sources, you can run a Quipucords scan to inspect your IT environment. You can run a scan on a single source or combine sources, even sources of different types. To run a scan, use the following steps:

Run the scan by using the ``scan start`` command, specifying one or more sources for the ``sources`` option:

  ``# qpc scan --sources source_name1 source_name2``

For example, if you want to scan the network source ``mynetwork`` and the Satellite source ``mysatellite6``, you would enter the following command:

  ``# qpc scan start --sources mynetwork mysatellite6``

Viewing scan results
^^^^^^^^^^^^^^^^^^^^
When you run the ``scan start`` command, the output provides an identifier for that scan. You can follow the status of the scan by using the ``scan show`` command and specifying the provided identifier.

For example, you could run the following scan as the first scan in your environment:

  ``# qpc scan start --sources mynetwork mysatellite6``

The output for the command shows the following information, with ``1`` listed as the scan identifier.

  ``Scan "1" started``

To follow the status of that scan, you would enter the following command:

  ``# qpc scan show --id 1``

Viewing the scan report
^^^^^^^^^^^^^^^^^^^^^^^
When the scan completes, you have the capability to produce a report for that scan. You can request a report with all the details of the scan or a report with a summary. The summary report process attempts to deduplicate and merge the facts found during the inspection of the various hosts that are contacted during the scan. You can produce a report in JavaScript Object Notation (JSON) format or comma-separated values (CSV) format.

To generate a summary report, enter the ``report summary`` command and specify the identifier for the scan and the format for the output file.

For example, if you want to create the report summary for a scan with the scan identifier of ``1`` and you wanted to generate that report in CSV format in the ``~/scan_result.csv`` file, you would enter the following command:

  ``# qpc report summary --id 1 --csv --output-file=~/scan_result.csv``

However, if you want to create the detailed report, you would use the ``report detail`` command.  This command takes the same options as the ``report summary`` command. The output is not deduplicated and merged, so it contains all facts from each source. To create the detailed report for a scan with the scan identifer ``1``, with CSV output in the ``~/scan_result.csv`` file, you would enter the following command:

  ``# qpc report detail --id 1 --csv --output-file=~/scan_result.csv``
