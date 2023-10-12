#!/usr/bin/env python
# 03-encapsulation-3.py

import struct

class myclass(object):
    def __init__(self, filename):
        self.filename = filename

    def get_filename(self):
        return print(self.filename)

    def set_filename(self, filename):
        self.filename = filename

    def parse_wav_method(self, printOut=None):
        filename = self.filename
        # Open the example wave file stored in the current directory.
        with open(filename, 'rb') as wav_file:
            # Main Header
            chunk_id = wav_file.read(4)
            print('''chunk_id: {chunk_id}'''.format(chunk_id=chunk_id))
            # assert chunk_id == b'RIFF', 'RIFF little endian, RIFX big endian: assume RIFF'

            chunk_size = struct.unpack('<I', wav_file.read(4))[0]
            print('''chunk_size: {chunk_size}'''.format(chunk_size=chunk_size))

            wav_format = wav_file.read(4)
            print('''wav_format: {wav_format}'''.format(wav_format=wav_format))
            # assert wav_format == b'WAVE', wav_format

            # Sub Chunk 1
            sub_chunk_1_id = wav_file.read(4)
            print('''sub_chunk_1_id: {sub_chunk_1_id}'''.format(sub_chunk_1_id=sub_chunk_1_id))
            # assert sub_chunk_1_id == b'fmt ', sub_chunk_1_id

            sub_chunk_1_size = struct.unpack('<I', wav_file.read(4))[0]
            print('''sub_chunk_1_size: {sub_chunk_1_size}'''.format(sub_chunk_1_size=sub_chunk_1_size))

            audio_format = struct.unpack('<H', wav_file.read(2))[0]
            print('''audio_format: {audio_format}'''.format(audio_format=audio_format))
            # assert audio_format == 1, '1 == PCM Format: assumed PCM'

            num_channels = struct.unpack('<H', wav_file.read(2))[0]
            print('''num_channels: {num_channels}'''.format(num_channels=num_channels))
            # assert num_channels == 1, '1 == Mono, 2 == Stereo: assumed Mono'

            sample_rate = struct.unpack('<I', wav_file.read(4))[0]
            print('''sample_rate: {sample_rate}'''.format(sample_rate=sample_rate))
            # assert sample_rate == 44100, 'assumed 44100'

            byte_rate = struct.unpack('<I', wav_file.read(4))[0]
            print('''byte_rate: {byte_rate}'''.format(byte_rate=byte_rate))
            # assert byte_rate == 32000, byte_rate

            # Could this be something other than an int?
            block_align = struct.unpack('<H', wav_file.read(2))[0]
            print('''block_align: {block_align}'''.format(block_align=block_align))
            # assert block_align == 2, block_align

            bits_per_sample = struct.unpack('<H', wav_file.read(2))[0]
            print('''bits_per_sample: {bits_per_sample}'''.format(bits_per_sample=bits_per_sample))
            # assert bits_per_sample == 16, bits_per_sample

            # Sub Chunk 2
            sub_chunk_2_id = wav_file.read(4)
            print('''sub_chunk_2_id: {sub_chunk_2_id}'''.format(sub_chunk_2_id=sub_chunk_2_id))
            # assert sub_chunk_2_id == b'data', sub_chunk_2_id

            sub_chunk_2_size = struct.unpack('<I', wav_file.read(4))[0]
            print('''sub_chunk_2_size: {sub_chunk_2_size}'''.format(sub_chunk_2_size=sub_chunk_2_size))

            samples = []
            bytes_per_sample = bits_per_sample / 8
            print('''bits_per_sample: {bits_per_sample}'''.format(bits_per_sample=bits_per_sample))
            print('''bytes_per_sample: {bytes_per_sample}'''.format(bytes_per_sample=bytes_per_sample))
            # assert (sub_chunk_2_size % bytes_per_sample) == 0, 'Uneven sample size'

            sample_count = int(sub_chunk_2_size / bytes_per_sample)
            print('''sample_count: {sample_count}'''.format(sample_count=sample_count))

            for _ in range(sample_count):
                samples.append(struct.unpack('<h', wav_file.read(2))[0])

            assert chunk_size == (
                    len(wav_format) +
                    len(sub_chunk_1_id) + sub_chunk_1_size + 4 +  # Full size of subchunk 1
                    len(sub_chunk_2_id) + sub_chunk_2_size + 4  # Full size of subchunk 2
            ), chunk_size

            assert sub_chunk_1_size == (
                    2 +  # audio_format
                    2 +  # num_channels
                    4 +  # sample_rate
                    4 +  # byte_rate
                    2 +  # block_align
                    2  # bits_per_sample
            ), sub_chunk_1_size

            bytes_per_sample = bits_per_sample / 8
            assert byte_rate == (
                    sample_rate * num_channels * bytes_per_sample
            ), byte_rate

            assert block_align == (
                    num_channels * bytes_per_sample
            ), block_align

            assert sub_chunk_2_size == (
                    len(samples) * bytes_per_sample
            ), sub_chunk_2_size

            length_in_seconds = (
                    len(samples) / sample_rate
            )

            ct = 0
            for sc in range(sample_count):
                try:
                    samples.append(struct.unpack('<h', wav_file.read(2))[0])
                except:
                    print("failed sample at:", sc) if printOut else 0
                    ct += 1

            print('''
    Parsed {filename}
    -----------------------------------------------
    Channels: {num_channels}
    Sample Rate: {sample_rate}
    First Sample: {first_sample}
    Second Sample: {second_sample}
    Onethousand Sample : {onethousand_sample}
    Length in Seconds: {length_in_seconds}'''.format(
                filename=filename,
                num_channels=num_channels,
                sample_rate=sample_rate,
                first_sample=samples[0],
                second_sample=samples[1],
                onethousand_sample=samples[10000],
                length_in_seconds=length_in_seconds))
