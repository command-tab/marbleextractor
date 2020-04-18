#!/usr/bin/env python3

import zlib
import os
import io

RECORD_START_OFFSET = 8
RECORD_HEADER_SIZE = 14
OUTPUT_DIRECTORY = 'extracted'


def write_decompressed_data_file(data_bytes, filename):
    data_bytesio = io.BytesIO(data_bytes)
    ZLIB_CHUNK_SIZE = 1024
    d = zlib.decompressobj()
    output_path = os.path.join(OUTPUT_DIRECTORY, filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as f:
        try:
            buf = data_bytesio.read(ZLIB_CHUNK_SIZE)
            while buf:
                decompressed_data = d.decompress(buf)
                buf = data_bytesio.read(ZLIB_CHUNK_SIZE)
                decompressed_data += d.flush()
                f.write(decompressed_data)
        except zlib.error:
            # If zlib decompression bombs, write the data as given; Some
            # files are not compressed. Maybe there's a record flag for this?
            f.write(data_bytes)


with open('marble.bza', 'rb') as f:
    bytes = f.read(4)

    record_count = int.from_bytes(bytes[0:4], byteorder='little')

    f.seek(RECORD_START_OFFSET)
    for i in range(1, record_count + 1):
        record_bytes = f.read(RECORD_HEADER_SIZE)
        data_offset = int.from_bytes(record_bytes[0:4], byteorder='little')
        compressed_size = int.from_bytes(record_bytes[4:8], byteorder='little')
        uncompressed_size = int.from_bytes(record_bytes[8:12], byteorder='little')
        filename_length = record_bytes[13]  # Filename length is stored as 1 byte
        filename = f.read(filename_length)

        # Store the current offset so we can seek back and continue reading records
        current_position = f.tell()

        # Extract and decompress the current record's payload
        f.seek(data_offset)
        data_bytes = f.read(compressed_size)
        write_decompressed_data_file(data_bytes, filename.decode('utf-8'))

        f.seek(current_position)
