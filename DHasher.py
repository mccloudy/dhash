#!/usr/bin/python
from PIL import Image

class DHasher(object):

   def __init__(self): return

   #######################################################################
   def hamming(self, x, y):
      """
      Compares two different items on an index-by-index basis, and
      reporting the number of per-index differences.  If one sequence
      is larger than another, those additional indices all count as a
      difference.

      Arguments:
         x (Sequence) -- Some iterable sequence with comparable indices 
         y (Sequence) -- Some iterable sequence with comparable indices 

      Returns:
         An integer denoting the number of differences between
         the first and second objects passed-in.
      """
      hd = 0
      maxrange = max([len(x), len(y)])
      for i in range(maxrange):
         if i > len(x) or i > len(y): 
            hd += abs(len(x)-len(y))
            break
         if x[i] != y[i]: hd += 1

      return hd

   #######################################################################
   def get_image_hash(self, im, sz=32):
      """
      Takes in a PIL image and produces a hash value from it using the 
      dhash method.

      Arguments:
         im (PIL.Image) -- An image which will be used to generate a 
                           bitstring based on the dhash algorithm.
         sz (Int) -- An integer describing the resize dimensions for 
                     the image (sz-by-sz+1).  Default value is 32.
      Returns:
         A list, which is the resulting hash of the encoded grayscale
         vector corresponding to the reduced, grayscale image.
      """
      if im.size[0] < sz or im.size[1] < sz: return None
      im = im.convert("L").resize((sz, sz+1), Image.ANTIALIAS)

      bsh = [] #Binary hash; just a bit vector, really
      for i in range(sz):
         for j in range(sz):
            bsh.append(int(im.getpixel((i,j)) < im.getpixel((i,j+1))))
      return bsh



   

if __name__ == "__main__":

   import sys

   def print_help():
      print "\tUSAGE: ./DHasher.py  <Image>  <Size>"
      
   if len(sys.argv) != 3:
      print_help()
      sys.exit(-1)

   dh = DHasher()
   im = Image.open(sys.argv[1])
   hval = dh.get_image_hash(im, int(sys.argv[2]))
   print "".join(map(str, hval))
