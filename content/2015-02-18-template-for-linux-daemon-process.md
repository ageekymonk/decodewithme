Title: A template for linux daemon process
Date: 2015-02-18 09:20
Modified: 2015-02-18 09:20
Category: Linux
Tags: Linux, C
Slug: template-for-linux-daemon-process
Authors: Ramz
Summary: A template for linux daemon process

Below is a template for creating a daemon process. The code will compile and when launched will create a daemon running.

```c

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdarg.h>
#include <unistd.h>
#include <string.h>
#include <signal.h>
#include <syslog.h>
#include <errno.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <sys/ioctl.h>


/* Global Variables */

uint8_t run_stop   = 0;
uint8_t run_daemon = 0;
uint8_t foreground = 0;

void msg(const char *fmt, ...)
{
	va_list ap;
	va_start(ap, fmt);

	if (run_daemon)
		vsyslog(LOG_INFO | LOG_USER, fmt, ap);
	else
		vfprintf(stderr, fmt, ap);

	va_end(ap);
}

void sig_teardown(int sig)
{
	run_stop = 1;
}

int main(int argc, char **argv)
{
    if (!foreground)
    {
        switch (fork())
        {
            case -1:
                msg("Unable to fork: %s\n", strerror(errno));
                return 8;

            case 0:
                umask(0077);
                chdir("/");
                freopen("/dev/null", "r", stdin);
                freopen("/dev/null", "w", stdout);
                freopen("/dev/null", "w", stderr);
                run_daemon = 1;
                break;

            default:
                msg("Daemon launched ...\n");
                return 0;
        }
    }

	signal(SIGINT, sig_teardown);
	signal(SIGTERM, sig_teardown);

	while (1)
    {
    		if (run_stop)
    		{
    		    /* clean up code */
    		}

    		/* Do somethine here */
    }

}



```