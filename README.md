# dexec (Docker exec)

dexec allows you to easily run commands inside project-based Docker containers.

Simply create a `.dexec` file like this:

~~~
[dexec]
container=my_container
path=/data
~~~

Where container is the name of the container, and path the path inside the
container of the directory in which the `.dexec` file is placed.

Now, just run:

~~~
dexec ls -l
~~~

And you'll see the directory listing from inside the container. Other commands
can be executed just the same, and they can be relative to the path:

~~~
dexec ./bin/my-script
~~~
