"""
  Copyright 2014 Google Inc. All rights reserved.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

"""
RLE
The absolute worst case should be the original length plus a copy_op
and 8 byte length.

RLE operands
1100-00nn copy, nn is the # of bytes in length
1100-10nn byte fill, nn is the # of bytes in repeat count, 1 byte fill value

Where nn is:
  00 1 byte length
  01 2 byte length
  10 4 byte length
  11 8 byte length
"""

from __builtin__ import bytearray


class RleFont(object):
  """Fills the file with given byte"""

  def __init__(self, filename):
    self.file = open(filename, 'r+b')

  def encode(self):
    encoded_bytes = bytearray()
    file_bytes = bytearray(self.file.read())
    repeats = self.find_repeats(file_bytes)
    print "need to build the RLE'd data"

  def find_repeats(self, arr):
    repeats = []
    repeat_start = 0
    prev_byte = None
    for i in range(len(arr)):
      cur_byte = arr[i]
      # In a repeat.
      if cur_byte == prev_byte:
        continue
      # Not in a repeat
      repeat_len = i - repeat_start
      # The minimum RLE fill overhead is:
      # 1 byte - op_code
      # 1 byte - fill value
      # 1 byte - length
      # Note: shorter versions are possible. 
      # It might be worthwhile to handle the shorter versions but it seems
      # unlikely there will be much actual gain.
      if repeat_len > 3:
        repeat_tuple = (repeat_start, repeat_len, prev_byte)
        repeats.append(repeat_tuple)
      prev_byte = cur_byte
      repeat_start = i
      
    # Close any last repeat
    repeat_len = i - repeat_start
    if repeat_len > 3:
      repeat_tuple = (repeat_start, repeat_len, prev_byte)
      repeats.append(repeat_tuple)
    
    return repeats


  def close(self):
    self.file.close()













