"""
157. Read N Characters Given Read4
Easy

Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

Method read4:

The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].
"""


class Solution:
    def read(self, buf: List[str], n: int) -> int:
        """
        Read file into a temp buffer buf4 and copy content to buf.
        """

        res, k = 0, 4
        buf4 = [" "] * 4
        while res < n and k == 4:
            k = read4(buf4)
            buf[res: res+4] = buf4
            res += k
        return min(n, res)
