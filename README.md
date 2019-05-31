# Logs Analysis Project

You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an **internal reporting tool** that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

1. What are the most popular three articles of all time? 

    Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

    Example:
    ```sh
    	"Princess Shellfish Marries Prince Handsome" — 1201 views
    	"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
    	"Political Scandal Ends In Political Scandal" — 553 views
    ```

2. Who are the most popular article authors of all time? 

    That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

    Example:

    ```sh
    	Ursula La Multa — 2304 views
    	Rudolf von Treppenwitz — 1985 views
    	Markoff Chaney — 1723 views
    	Anonymous Contributor — 1023 views
    ```

3. On which days did more than 1% of requests lead to errors? 

    The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson 	for more information about the idea of HTTP status codes.)

	Example:

    ```sh
   	July 29, 2016 — 2.5% errors
    ```

# Installation

##  Install VirtualBox

 You can download it from virtualbox.org, [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.


##  Install Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.

*If Vagrant is successfully installed, you will be able to run `vagrant --version` in your terminal to see the version number.
The shell prompt in your terminal may differ. Here, the $ sign is the shell prompt.*

## Download the VM configuration

There are a couple of different ways you can download the VM configuration.

You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with `cd`. Inside, you will find another directory called **vagrant**. Change directory to the **vagrant** directory:

*Navigating to the FSND-Virtual-Machine directory and listing the files in it.
This picture was taken on a Mac, but the commands will look the same on Git Bash on Windows.*

## Start the virtual machine

From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause **Vagrant** to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

*Starting the Ubuntu Linux installation with vagrant up.
This screenshot shows just the beginning of many, many pages of output in a lot of colors.*

When `vagrant up` is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM!

## Logged in!

If you are now looking at a shell prompt that starts with the word vagrant (as in the above screenshot), congratulations — you've gotten logged into your Linux VM.

If not, take a look at the Troubleshooting section below.

## The files for this Project

Inside the VM, change directory to `/vagrant` and look around with `ls`.

The files you see here are the same as the ones in the `vagrant` subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM.

Files in the VM's `/vagrant` directory are shared with the `vagrant` folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.

## Running the database

The PostgreSQL database server will automatically be started inside the VM. You can use the psql command-line tool to access it and run SQL statements:

*Running `psql`, the PostgreSQL command interface, inside the VM.*

## Logging out and in

If you type `exit` (or `Ctrl-D`) at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same directory and type `vagrant ssh` again.

If you reboot your computer, you will need to run `vagrant up` to restart the VM.

## Download the data

Next, download the data [here.](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) You will need to unzip this file after downloading it. The file inside is called `newsdata.sql`. Put this file into the `vagrant` directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the `psql` command in this lesson: [(FSND version)](https://classroom.udacity.com/nanodegrees/nd004-ent/parts/72d6fe39-3e47-45b4-ac52-9300b146094f/modules/0f94ae26-c39d-4231-924b-b1eb6e06cf41/lessons/96869cfc-c67e-4a6c-9df2-9f93267b7be5/concepts/0b4079f5-6e64-4dd8-aee9-5c3a0db39840?contentVersion=1.0.0&contentLocale=en-us)


To load the data, `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`.
Here's what this command does:

`psql` — the PostgreSQL command line program

`-d news` — connect to the database named news which has been set up for you.

`-f newsdata.sql` — run the SQL statements in the file `newsdata.sql`.

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

```sh
psql -d news -f newsdata.sql
```

```sh
python new.py
```

```sh
vagrant /vagrant/udacity (master) $ python news.py

1. What are the most popular three articles of all time?
 
    - "Candidate is jerk, alleges rival" - 338647 views
    - "Bears love berries, alleges bear" - 253801 views
    - "Bad things gone, say good people" - 170098 views

2. Who are the most popular article authors of all time?
 
    - Ursula La Multa - 507594 views
    - Rudolf von Treppenwitz - 423457 views
    - Anonymous Contributor - 170098 views
    - Markoff Chaney - 84557 views

3. On which days did more than 1% of requests lead to errors?
 
    - July 17, 2016 - 2.26% errors
```

