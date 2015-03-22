Title: A template for parsing config file using libconfig
Date: 2015-02-20 09:21
Modified: 2015-02-20 09:21
Category: Linux
Tags: Linux, C
Slug: template-for-parsing-config-file-using-libconfig
Authors: Ramz
Summary: A template for parsing config file using libconfig

Below is a template for parsing a config file using libconfig.
The code will compile and when launched will parse a given config file .

Let the config file be

            url = "www.example.com"
            username = "ramz"
            password = "password"
            interval = 10

``` c

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <libconfig.h>

#ifndef TRUE
#define TRUE  1
#endif

#ifndef FALSE
#define FALSE 0
#endif

#ifndef OK
#define OK 0
#endif

#ifndef ERR
#define ERR -1
#endif



void msg(const char *fmt, ...)
{
	va_list ap;
	va_start(ap, fmt);

	vfprintf(stderr, fmt, ap);

	va_end(ap);
}


int main(int argc, char **argv)
{
	int i, n;
    int opt;
    char *conffile = NULL;
    config_t cfg;

    char *username, *password, *host;
    int interval;

	while ((opt = getopt(argc, argv, "c:h")) != -1)
	{
		switch (opt)
		{
            case 'c':
                conffile = optarg;
                break;

            case 'h':
            default:
                msg(
                    "Usage:\n"
                    "  %s -c configfile \n"
                    "\n"
                    "  -c configfile\n"
                    "    Specify the config file to use \n\n"
                    "  -h\n"
                    "    Display this help.\n\n",
                    argv[0]);
                return 1;
		}
	}

    if (conffile == NULL)
    {
        msg("config file not given\n");
    }

    config_init(&cfg);

    if(! config_read_file(&cfg, conffile))
    {
        msg("%s:%d - %s\n", config_error_file(&cfg), config_error_line(&cfg), config_error_text(&cfg));
        config_destroy(&cfg);
        return(ERR);
    }

     /* Get the url */
    if(!(config_lookup_string(&cfg, "url", &host)))
    {
        msg("No 'url' setting in configuration file.\n");
        return(ERR);
    }

     /* Get the username */
    if(!(config_lookup_string(&cfg, "username", &username)))
    {
        msg("No 'username' setting in configuration file.\n");
        return(ERR);
    }

     /* Get the password */
    if(!(config_lookup_string(&cfg, "password", &password)))
    {
        msg("No 'password' setting in configuration file.\n");
        return(ERR);
    }

     /* Get the batch time  */
    if(!(config_lookup_int(&cfg, "interval", &interval)))
    {
        msg("No 'batchinterval' setting in configuration file. using default value %d\n", batch_interval);
    }

    return 0;
}

```