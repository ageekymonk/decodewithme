Title: A template for gzipping your text using zlib library
Date: 2015-02-18 09:20
Modified: 2015-02-18 09:20
Category: Linux
Tags: Linux, C
Slug: template-for-gzipping-your-text
Authors: Ramz
Summary: A template for gzipping your text using zlib library

Below is a template for gzipping your text using zlib library.
The code will compile and when launched will create a gzip file and print it.


```c

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>
#include <zlib.h>

#define MAX_GZIP_FILE_SIZE 1024*1024
#define DEF_MEM_LEVEL 8

void msg(const char *fmt, ...)
{
	va_list ap;
	va_start(ap, fmt);

	vfprintf(stderr, fmt, ap);

	va_end(ap);
}

int string_gzip (char **dest, int *destLen, char *source, unsigned long sourceLen)
{
  char *header;
  char buffer[MAX_GZIP_FILE_SIZE];
  z_stream stream;
  int err;

  stream.zalloc = Z_NULL;
  stream.zfree = Z_NULL;
  stream.opaque = Z_NULL;

  // instructs zlib not to write a zlib header
  err = deflateInit2( &stream, Z_DEFAULT_COMPRESSION, Z_DEFLATED,
                      31, DEF_MEM_LEVEL, Z_DEFAULT_STRATEGY );
  if (err != Z_OK)
    return err;

  stream.next_in = source;
  stream.avail_in = sourceLen;

  stream.next_out = buffer;
  stream.avail_out = 50*1024;

  err = deflate(&stream, Z_FINISH); // Z_FINISH or Z_NO_FLUSH if we have
                                    // more input still (we don't)
  if (err != Z_STREAM_END) {
      deflateEnd(&stream);
      return err == Z_OK ? Z_BUF_ERROR : err;
  }

  err = deflateEnd(&stream);
  *destLen = stream.total_out;
  *dest = (char *) malloc(stream.total_out);
  memcpy(*dest, buffer, stream.total_out);

  return err;
}

int main(int argc, char **argv)
{

    char *uncompressed_text = "Hello world";
    char *compressed_text;
    int compressed_text_length = 0;
    int retval;

    retval = string_gzip (&compressed_text, &compressed_text_length, uncompressed_text, strlen(uncompressed_text)+1);

    if(retval != Z_OK)
    {
      switch(retval)
      {
        case Z_MEM_ERROR:
          msg("zlib: Error allocating memory.\n");
          break;
        case Z_DATA_ERROR:
          msg("zlib: Error, deflate data is invalid or incomplete.");
          break;
        case Z_VERSION_ERROR:
          msg("zlib: Error, version mismatch between \"zlib.h\" and \"libz.so\".\n");
          break;
        case Z_ERRNO:
          msg("zlib: Error reading/writing to files.\n");
          break;
        default:
          msg("zlib: Error, unspecified.\n");
      }

    }

    /* Do something with the compressed text. Like uploading to http server ...  */
}

```
