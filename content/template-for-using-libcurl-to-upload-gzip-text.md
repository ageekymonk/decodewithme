Title: A template for uploading gzipped text to http server using libcurl
Date: 2015-02-19 09:20
Modified: 2015-02-19 09:20
Category: Linux
Tags: Linux, C
Slug: template-for-using libcurl-to-upload-gzip-text
Authors: Ramz
Summary: A template for gzipping your text using zlib library

Below is a template for gzipping your text using zlib library and upload to http server using libcurl.
The code will compile and when launched will create a gzip file and upload it to http server.

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

int upload(char * host, char *data, uint32_t data_len)
{

    CURL *curl;
    CURLcode res;
    struct curl_slist *header_list=NULL;
    char contentLengthBuf[32];

    curl = curl_easy_init();
    // First set the URL that is about to receive our POST. This URL can
    // just as well be a https:// URL if that is what should receive the
    // data.
    curl_easy_setopt(curl, CURLOPT_URL, host);

    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);

    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 1L);

    // set the "Accept-Encoding: " header
    curl_easy_setopt(curl, CURLOPT_ENCODING, "gzip");

    // Set all the headers
    header_list = curl_slist_append(header_list, "Content-Encoding: gzip");

    header_list = curl_slist_append(header_list, "Content-Type: text/json");

    sprintf(contentLengthBuf, "Content-Length: %d", data_len);
    header_list = curl_slist_append(header_list, contentLengthBuf);

    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, header_list);

    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, data_len);

    curl_easy_setopt(curl, CURLOPT_USERNAME, username);
    curl_easy_setopt(curl, CURLOPT_PASSWORD, password);

    res = curl_easy_perform(curl);

    curl_slist_free_all(header_list);
    curl_easy_cleanup(curl);

    if (res == CURLE_OK)
        return 0;
    else
    {
        msg("Upload Failed. Error Code %d ...\n", res);
        return -1;
    }
}

int main(int argc, char **argv)
{

    char *uncompressed_text = "Hello world";
    char *host = "www.example.com";
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

    /* uploading to http server ...  */
    retval = upload((char *)host, compressed_text, compressed_text_length);
    if (retval == 0)
    {
        /* success */
    }
    else
    {
        /* failure */
    }
}

```