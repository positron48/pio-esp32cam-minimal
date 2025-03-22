#!/usr/bin/env python3
import gzip
import os
import sys

def compress_html_to_h(input_file, output_file):
    with open(input_file, 'rb') as f:
        content = f.read()
    
    # Compress the content
    compressed = gzip.compress(content)
    
    # Create the header file
    with open(output_file, 'w') as f:
        f.write('//File: {}.gz, Size: {}\n'.format(os.path.basename(input_file), len(compressed)))
        f.write('#define index_ov2640_html_gz_len {}\n'.format(len(compressed)))
        f.write('const uint8_t index_ov2640_html_gz[] = {\n ')
        
        # Write the compressed content as hex bytes
        for i, byte in enumerate(compressed):
            f.write('0x{:02X}'.format(byte))
            if i < len(compressed) - 1:
                f.write(', ')
            if (i + 1) % 16 == 0 and i < len(compressed) - 1:
                f.write('\n ')
        
        f.write('\n};\n\n')
        
        # Also provide the same data for OV3660 camera
        f.write('//File: {}.gz, Size: {}\n'.format(os.path.basename(input_file), len(compressed)))
        f.write('#define index_ov3660_html_gz_len {}\n'.format(len(compressed)))
        f.write('const uint8_t index_ov3660_html_gz[] = {\n ')
        
        # Write the compressed content as hex bytes again
        for i, byte in enumerate(compressed):
            f.write('0x{:02X}'.format(byte))
            if i < len(compressed) - 1:
                f.write(', ')
            if (i + 1) % 16 == 0 and i < len(compressed) - 1:
                f.write('\n ')
        
        f.write('\n};\n')
    
    print(f"Converted {input_file} to {output_file}")
    print(f"Compressed size: {len(compressed)} bytes")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_html_to_h.py input.html output.h")
        sys.exit(1)
    
    compress_html_to_h(sys.argv[1], sys.argv[2]) 